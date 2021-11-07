"""Structural Patterns

@see https://legacy.python.org/workshops/1997-10/proceedings/savikko.html#gof
@see https://www.toptal.com/python/python-design-patterns
@see https://github.com/faif/python-patterns

Being one of software engineering's main fields of work, software design patterns are a general, reusable solution to a commonly occurring software design problem.
A design pattern can be understood as a description or template, guiding an engineer when solving a problem through best practices and well-known standards.
On top, design patterns make code easier to understand and maintainable.

Structural design patterns - a subcategory of design patterns - are patterns dealing with object relations. They ease the design by identifying a simple way to
realize relationships among entities.

Typical Structural design patterns are:

- Adapter
- Aggregate
- Facade
- Bridge
- Flyweight
- Decorator
- Marker
- Proxy

Note: Design patterns fit a special role in python because everything in python is an object, even functions are objects. Some design patterns are already implemented in python,
others are not necessary due to python's nature.
"""


# Facade
class Car(object):
	"""Streamlining an interface by creating a client-facing facade which hides multiple other objects"""

    def __init__(self):
        self._tyres = [Tyre('front_left'),
                             Tyre('front_right'),
                             Tyre('rear_left'),
                             Tyre('rear_right'), ]
        self._tank = Tank(70)

    def tyres_pressure(self):
        return [tyre.pressure for tyre in self._tyres]

    def fuel_level(self):
        return self._tank.level




# Adapter --> similar to Bridge and Proxy
import socket

class SocketWriter(object):
	"""Altering an interface by translating a new interface to a known one"""

    def __init__(self, ip, port):
        self._socket = socket.socket(socket.AF_INET,
                                     socket.SOCK_DGRAM)
        self._ip = ip
        self._port = port

    def write(self, message):
        self._socket.send(message, (self._ip, self._port))

def log(message, destination):
    destination.write('[{}] - {}'.format(datetime.now(), message))

upd_logger = SocketWriter('1.2.3.4', '9999')
log('Something happened', udp_destination)




# Decorator
	"""Introducing additional functionality without inheritance"""

def execute(action, *args, **kwargs):
    return action()

def autheticated_only(method):
    def decorated(*args, **kwargs):
        if check_authenticated(kwargs['user']):
            return method(*args, **kwargs)
        else:
            raise UnauthenticatedError
    return decorated

def authorized_only(method):
    def decorated(*args, **kwargs):
        if check_authorized(kwargs['user'], kwargs['action']):
            return method(*args, **kwargs)
        else:
            raise UnauthorizeddError
    return decorated

execute = authenticated_only(execute)
execute = authorized_only(execute)

# We can also use the core-python integrated syntax
def autheticated_only(method):
    def decorated(*args, **kwargs):
        if check_authenticated(kwargs['user']):
            return method(*args, **kwargs )
        else:
            raise UnauthenticatedError
    return decorated


def authorized_only(method):
    def decorated(*args, **kwargs):
        if check_authorized(kwargs['user'], kwargs['action']):
            return method(*args, **kwargs)
        else:
            raise UnauthorizedError
    return decorated


@authorized_only
@authenticated_only
def execute(action, *args, **kwargs):
    return action()