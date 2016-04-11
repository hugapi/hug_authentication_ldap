"""hug_authentication_ldap/authentication.py

LDAP based authentication support for hug

Copyright (C) 2016  Timothy Edmund Crosley

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated
documentation files (the "Software"), to deal in the Software without restriction, including without limitation
the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and
to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or
substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED
TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL
THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF
CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR
OTHER DEALINGS IN THE SOFTWARE.

"""
from collections import namedtuple

import hug
import ldap3

user = namedtuple('User', ('name', 'connection'))


def server(url, get_info=ldap3.ALL, **kwargs):
    """Returns an ldap3 server reference with the provided parameters"""
    return ldap3.Server(url, get_info=get_info, **kwargs)


def verify(server, user_template="uid={user_name},ou=people", authentication=ldap3.AUTH_SIMPLE, auto_bind=True,
            **kwargs):
    """Returns an authentication verification callback that enforces ldap authentication passing in the
       user_template with the passed in user overriding any in-string placement of {user_name}

       passes any extra **kwargs parameters to the ldap3.Connection method used for authentication
    """
    def verify_user(user_name, password):
        try:
            connection = ldap3.Connection(server, authentication=authentication, auto_bind=auto_bind,
                                          user=user_template.format(user_name=user_name), password=password, **kwargs)
            return user(user_name, connection)
        except ldap3.core.exceptions.LDAPBindError:
            return False
    return verify_user


def basic(server_url, user_template="uid={user_name},ou=people", server_info=None, **kwargs):
    """Creates a basic HTTP authenticator that checks credentials against an ldap server"""
    return hug.authentication.basic(verify(server(server_url, **(server_info or {})), user_template=user_template,
                                           **kwargs))
