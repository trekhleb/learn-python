"""Behavioral Patterns

@see https://legacy.python.org/workshops/1997-10/proceedings/savikko.html#gof
@see https://www.toptal.com/python/python-design-patterns
@see https://github.com/faif/python-patterns

Being one of software engineering's main fields of work, software design patterns are a general, reusable solution to a commonly occurring software design problem.
A design pattern can be understood as a description or template, guiding an engineer when solving a problem through best practices and well-known standards.
On top, design patterns make code easier to understand and maintainable.

Behavioral design patterns - a subcategory of design patterns - are design patterns that identify common communication patterns among objects.
By doing so, these patterns increase flexibility in carrying out inter-object-communication.

Typical Behavioral design patterns are:

- Blackboard
- Command
- Chain of Responsibility
- Interpretar
- Iterator
- Mediator
- Memento
- Observer
- Protocol Stack
- State
- Strategy
- Visitor
- Scheduled-Task

Note: Design patterns fit a special role in python because everything in python is an object, even functions are objects. Some design patterns are already implemented in python,
others are not necessary due to python's nature.
"""


# Chain of Responsibility
class ContentFilter(object):
	"""Every code element has one - and only one - specific job"""

    def __init__(self, filters=None):
        self._filters = list()
        if filters is not None:
            self._filters += filters

    def filter(self, content):
        for filter in self._filters:
            content = filter(content)
        return content

filter = ContentFilter([
                offensive_filter,
                ads_filter,
                porno_video_filter])

filtered_content = filter.filter(content)


# Command
class RenameFileCommand(object):
	"""Command execution when needed"""

    def __init__(self, from_name, to_name):
        self._from = from_name
        self._to = to_name

    def execute(self):
        os.rename(self._from, self._to)

    def undo(self):
        os.rename(self._to, self._from)

class History(object):
    def __init__(self):
        self._commands = list()

    def execute(self, command):
        self._commands.append(command)
        command.execute()

    def undo(self):
        self._commands.pop().undo()

history = History()
history.execute(RenameFileCommand('docs/cv.doc', 'docs/cv-en.doc'))
history.execute(RenameFileCommand('docs/cv1.doc', 'docs/cv-bg.doc'))
history.undo()
history.undo()
