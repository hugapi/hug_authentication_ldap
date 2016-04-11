hug_authentication_ldap
===================

[![PyPI version](https://badge.fury.io/py/hug_authentication_ldap.svg)](http://badge.fury.io/py/hug_authentication_ldap)
[![Build Status](https://travis-ci.org/timothycrosley/hug_authentication_ldap.svg?branch=master)](https://travis-ci.org/timothycrosley/hug_authentication_ldap)
[![Coverage Status](https://coveralls.io/repos/timothycrosley/hug_authentication_ldap/badge.svg?branch=master&service=github)](https://coveralls.io/github/timothycrosley/hug_authentication_ldap?branch=master)
[![License](https://img.shields.io/github/license/mashape/apistatus.svg)](https://pypi.python.org/pypi/hug_authentication_ldap/)
[![Join the chat at https://gitter.im/timothycrosley/hug](https://badges.gitter.im/Join%20Chat.svg)](https://gitter.im/timothycrosley/hug?utm_source=badge&utm_medium=badge&utm_campaign=pr-badge&utm_content=badge)

Easy to use LDAP based authentication support for hug:

```py
import hug
import hug_authentication_ldap


authentication = hug_authentication_ldap.basic('myldap.server.net', 'uid={user_name},ou=people')


@hug.get(requires=authentication)
def say_hello(hug_user):
    return 'Hello {}!'.format(hug_user.name)
```

Or, for general reusable LDAP password verification within hug:

```py
import hug
import hug_authentication_ldap


ldap_check = hug_authentication_ldap.verify('myldap.server.net', 'uid={user_name},ou=people')


@hug.get()
def check(user_name, password):
    if ldap_check(user_name, password):
        return True

    return False
```

Installing hug_authentication_ldap
===================

Installing hug_authentication_ldap is as simple as:

```bash
pip3 install hug_authentication_ldap --upgrade
```

Ideally, within a virtual environment.


What is hug_authentication_ldap?
===================

An extension for hug that provides LDAP based authentication support

--------------------------------------------

Thanks and I hope you find hug_authentication_ldap helpful!

~Timothy Crosley
