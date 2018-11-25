"""Packages.

@see: https://docs.python.org/3/tutorial/modules.html#packages

Packages are a way of structuring Python’s module namespace by using “dotted module names”. For
example, the module name A.B designates a submodule named B in a package named A. Just like the
use of modules saves the authors of different modules from having to worry about each other’s
global variable names, the use of dotted module names saves the authors of multi-module packages
like NumPy or Pillow from having to worry about each other’s module names.

The __init__.py files are required to make Python treat the directories as containing packages;
this is done to prevent directories with a common name, such as string, from unintentionally hiding
valid modules that occur later on the module search path. In the simplest case, __init__.py can
just be an empty file, but it can also execute initialization code for the package or set the
__all__ variable, described later.

When the interpreter executes the import statement, it searches for module in a list of
directories assembled from the following sources:

- The directory from which the input script was run or the current directory if the interpreter is
being run interactively
- The list of directories contained in the PYTHONPATH environment variable, if it is set. (The
format for PYTHONPATH is OS-dependent but should mimic the PATH environment variable.)
- An installation-dependent list of directories configured at the time Python is installed

The resulting search path is accessible in the Python variable sys.path, which is obtained from a
module named sys:

>>> import sys
>>> sys.path

@see: https://realpython.com/python-modules-packages/
"""

# Users of the package can import individual modules from the package, for example.
import sound_package.effects.echo

# An alternative way of importing the submodule is:

# pylint: disable=reimported
from sound_package.effects import echo

# Yet another variation is to import the desired function or variable directly:
from sound_package.effects.echo import echo_function

# Note that when using from package import item, the item can be either a submodule (or subpackage)
# of the package, or some other name defined in the package, like a function, class or variable.
# The import statement first tests whether the item is defined in the package; if not, it assumes
# it is a module and attempts to load it. If it fails to find it, an ImportError exception is
# raised.

# Contrarily, when using syntax like import item.subitem.subsubitem, each item except for the last
# must be a package; the last item can be a module or a package but can’t be a class or function or
# variable defined in the previous item.


def test_packages():
    """Packages."""
    assert sound_package.effects.echo.echo_function() == 'Do echo effect'
    assert echo.echo_function() == 'Do echo effect'
    assert echo_function() == 'Do echo effect'
