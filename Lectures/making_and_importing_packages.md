# Making and Importing Packages

As shared in [modules.md](modules.md), we can import modules for use in our
code from:
* the Python Standard Library, 
* third-party packages that we install in our virtual environment, and 
* our own modules containing Python code.

In the examples shared up to this point in the class, it was required that our
own modules which we wanted to import needed to be in the same directory as our
base code for the `import` statement to work. However, when our projects get
larger, we may want to better organize our code files into different folders.
And, we may want to share some of this code with others for them to use. So, we
need to learn more about how to use the `import` statement when we want to
import across different directories and how we can make packages that are
easily distributable.

## Modules vs. Package
Python documentation provides "official" definitions about what a module and
package are.  (See resources below.)  But, in practical terms, a module is 
a Python code file that contains a variety of global variables and functions.
A package is a directory that contains one or more modules or subpackages.

Below we show some examples of how we can create a package with modules and
import those packages and modules into our code.

## Creating and Using a Package

Assume we are writing software to do some scientific modeling, and we have a
variety of utility functions that will provide a variety of unit conversions,
simple calculations, etc. Up to this point, we might have put those utility
functions in a different Python file in the same directory as our main code and
then imported those modules. For example, our code directory would be setup
like this:

```
model_development/
├── run_model.py
├── flow_calculations.py
└── unit_conversions.py
```
And, we would import the utility code into our main code as follows:
```python
# run_model.py

import flow_calculations
import unit_conversions

pipe_db_psi = flow_calculations.pressure_drop(*args)
pipe_db_bar = unit_conversions.convert_pressure(pipe_db_psi, "psi", "bar")
```

Now, let's say we would like to organize our utility modules.  Rather 
than have multiple Python module files in the same directory as the main 
code, we could place them into a subdirectory that we could call our 
"toolbox" package.
```
model_development/
├── run_model.py
└── toolbox/
    ├── flow_calculations.py
    └── unit_conversions.py
```
Now, we would import the code such as this:
```python
# run_model.py

from toolbox import flow_calculations
from toolbox import unit_conversions

pipe_db_psi = flow_calculations.pressure_drop(*args)
pipe_db_bar = unit_conversions.convert_pressure(pipe_db_psi, "psi", "bar")
```
The names `flow_calculations` and `unit_conversions` are defined in the 
code and can be used to call functions inside them.

Let's say we wanted to make the import even easier.  Let's look at this code:
```python
# run_model.py

import toolbox

pipe_db_psi = toolbox.flow_calculations.pressure_drop(*args)
pipe_db_bar = toolbox.unit_conversions.convert_pressure(pipe_db_psi, "psi", 
                                                      "bar")
```
In this code, we are importing the `toolbox` itself and then using that 
name to access the submodules. If we run this code given the file setup above,
we will get an `AttributeError`:
```
AttributeError: module 'toolbox' has no attribute 'flow_calculations'
```
The reason for this is that we have defined the name `toolbox` in the code, but
that name is not yet linked to its submodules.  To do that, we need to create a
Python file called  `__init__.py` file in the directory:
```
model_development/
├── run_model.py
└── toolbox/
    ├── __init__.py
    ├── flow_calculations.py
    └── unit_conversions.py
```
In this file, we then need to `import` the modules that we want to access 
through the `toolbox` name.

```python
# toolbox/__init__.py

from . import flow_calculations
from . import unit_conversions
```
With this addition, the code above with the statement `import toolbox` will 
work.  Note that in the `__init__.py` file, you must use the `from . import 
<module_name>` syntax.  (See the section on Absolute vs. Relative imports 
below for more information.)

The imports in `run_model.py` code could also be written as this:
```python
# run_model.py

from toolbox import flow_calculations, unit_conversions

pipe_db_psi = flow_calculations.pressure_drop(*args)
pipe_db_bar = unit_conversions.convert_pressure(pipe_db_psi, "psi", 
                                                      "bar")
```
thereby, not needing to use the `toolbox` name when accessing the modules.

Finally, let's say you did not want the user of the package to have to know
anything about the individual modules, but just want them to have access to
the functions in those modules directly through the `toolbox` name.  The
`__init__.py` file could be modified as follows:

```python
# toolbox/__init__.py

from .flow_calculations import pressure_drop
from .unit_conversions import convert_pressure
```
Then, the `run_model.py` file can simply import and use `toolbox` as follows:

```python
# run_model.py

import toolbox

pipe_db_psi = toolbox.pressure_drop(*args)
pipe_db_bar = toolbox.convert_pressure(pipe_db_psi, "psi", "bar")

```
Note that in the `__init__.py` file, the modules had the period (`.`) in front
of their names.  This was required to notify Python that the module to be 
imported was in the same folder as the `__init__.py` file.  See the section 
below on relative imports.

## Absolute vs. Relative Imports
When using the `import` statement, Python generally assumes that an
"absolute" import is being done, meaning that the import specifies the entire
package name. Assume we have the following file structure:

```
model_development/
├── run_model.py
├── pipe_works/
│   ├── __init__.py
│   ├── pipe_model.py
│   ├── subpackage1/
│   │   └── module_sub1.py
│   └── subpackage2/
│       └── module_sub2.py
└── toolbox/
    ├── __init__.py
    ├── flow_calculations.py
    └── unit_conversions.py
```
In `run_model.py`, if we wanted to access the `module_sub2.py` file, we
would use:
```python
# run_model.py

import pipe_works.subpackage2.module_sub2
```
It is an "absolute" reference because it contains the entire package pathway.

Now, let's say that we want the `module_sub1.py` function to be able to 
import the `module_sub2` module in a different folder.  We could again use an 
absolute reference. 
```python
# pipe_works/subpackage1/module_sub1.py

import pipe_works.subpackage2.module_sub2
```
Absolute imports are the preferred import method given that they 
are unambiguous and do not depend on the their location for reaching the 
correct module.

But, if you have a variety of nested directories, it can make the import 
statements long.  Python does have the ability to do "relative" imports.
In a "relative" import, the name of the module to be imported is given 
relative to the location of the file doing the import.  For example, if we 
revisit `module_sub1.py` wanting to import `module_sub2`, the absolute 
import above could be replaced by the following relative import:
```python
# pipe_works/subpackage1/module_sub1.py

from ..subpackage2 import module_sub2
```
The double dots (`..`) before `subpackage2` tells Python that you need to go
up one level from the current `subpackage1` directory and there you will find 
the `subpackage2` directory.  Note, you must use the `from <name> import 
<name>` format when using relative imports.

If you want to import something from the same folder, you would use a 
single dot (`.`) before the name.  See the example above in which the 
`__init__.py` file used the `from .flow_calculations import pressure_drop` 
command.

As one final example, assume that `module_sub1.py` wanted to use code found 
in the `pipe_model.py` module that is in the parent directory of 
`module_sub1.py`.  That relative import command would look like:
```python
# pipe_works/subpackage1/module_sub1.py

from .. import pipe_model
```

## Distributing Packages
If you want to share a package you have developed, there are a variety of 
ways to do that.  To share with a single colleague, you can always just 
give them the package folder with its contents for them to include in their 
code directory.

Alternatively, you can "build" a package in such a way that it could be 
shared on an on-line platform such as <https://pypi.org/>.  More 
information on how to do that can be found in the resources below.


## Resources
* The Python Import System:  <https://docs.python.org/3/reference/import.html#packages>
* Package definition:  <https://docs.python.org/3/glossary.html#term-package>
* Module definition:  <https://docs.python.org/3/glossary.html#term-module>
* Packaging Python Projects and Sharing on PyPi:
  <https://packaging.python.org/en/latest/tutorials/packaging-projects/>