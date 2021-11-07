"""Creational Patterns

@see https://legacy.python.org/workshops/1997-10/proceedings/savikko.html#gof
@see https://www.toptal.com/python/python-design-patterns
@see https://github.com/faif/python-patterns

Being one of software engineering's main fields of work, software design patterns are a general, reusable solution to a commonly occurring software design problem.
A design pattern can be understood as a description or template, guiding an engineer when solving a problem through best practices and well-known standards.
On top, design patterns make code easier to understand and maintainable.

Creational design patterns - a subcategory of design patterns - are patterns dealing with object creation mechanisms (often in OOP environments),
trying to create objects in a manner suitable to the situation. The basic form of object creation could result in design problems or in added complexity to the design.
Creational design patterns aim to solve this problem by somehow controlling this object creation.

Typical Creational design patterns are:

- Abstract Factory
- Builder
- Dependency Injection
- Factory Method
- Lazy Initialization
- Multition
- Object Pool
- Prototype
- Singleton

Note: Design patterns fit a special role in python because everything in python is an object, even functions are objects. Some design patterns are already implemented in python,
others are not necessary due to python's nature. Creational patterns are rather uncommon in python, since it already is a very dynamic language.
"""


# Singleton
class Logger(object):
	"""Making sure that only one instance of a given class exists during runtime"""
    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, '_logger'):
            cls._logger = super(Logger, cls
                    ).__new__(cls, *args, **kwargs)
        return cls._logger


# Dependency Injection
class Command:
	"""Creating object outside of where it is used"""

    def __init__(self, authenticate=None, authorize=None):
        self.authenticate = authenticate or self._not_authenticated
        self.authorize = authorize or self._not_autorized

    def execute(self, user, action):
        self.authenticate(user)
        self.authorize(user, action)
        return action()

if in_sudo_mode:
    command = Command(always_authenticated, always_authorized)
else:
    command = Command(config.authenticate, config.authorize)

command.execute(current_user, delete_user_action)


# Alternative Dependency Injection
command = Command()

if in_sudo_mode:
    command.authenticate = always_authenticated
    command.authorize = always_authorized
else:
    command.authenticate = config.authenticate
    command.authorize = config.authorize

command.execute(current_user, delete_user_action)