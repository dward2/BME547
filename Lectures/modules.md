# Modules and Import

## Python Standard Library Modules

The [Python Standard Library](https://docs.python.org/3/library/) has a great 
deal of code functionality that is accessed by importing modules that are
included with the standard distribution of Python.  (Click 
[here](https://docs.python.org/3/py-modindex.html) for a complete list of these
modules.)

These modules are accessed in code by importing them using the following
syntax:
  
`import <module_name>`

Example: `import math`.   

In a previous lecture, we created a module called `calculator.py`:
```python
# calculator.py

def add(x, y):
    z = x + y
    return z

def subtract(x, y):
    z = x - y
    return z

def multiply(x, y):
    z = x * y
    return z

def divide(x, y):
    z = x / y
    return z
    

operator = input("Enter a letter: ")
print("You entered {}".format(operator))
a = input("Enter the first number: ")
b = input("Enter the second number: ")
if operator == "a":
   answer = add(int(a), int(b))
   symbol = '+'
elif operator == "s":
   answer = subtract(int(a), int(b))
   symbol = '-'
elif operator == "m":
   answer = multiply(int(a), int(b))
   symbol = 'x'
elif operator == "d":
   answer = divide(int(a), int(b))
   symbol = '/'
else:
   print("The {} command is not recognized.".format(operator))
   exit()

print("{} {} {} = {}".format(a, symbol, b, answer))
```

Lets add a square root option to the calculator.  The square root function in 
Python is found in the `math` library.  

```python
def square_root(x):
    import math
    z = math.sqrt(x)
    return z
```

The `math` module is imported into the code with the `import math` statement.
Functions in the module are accessed by the syntax 
`<module_name>.<function_name>`.  In the above example, this is 
`math.sqrt()`.  The `import` statement can be either in the function in which
the imported function is used or at the top of the module (most-common 
approach).  

## Packages

One strength of Python is the wide variety of external packages that can be
imported into a project.  First, a virtual environment should be created into
which the external package can be installed.  See 
[virtual_environments.md](virtual_environments.md) for details on creating
and using virtual environments.  Once the desired packages are installed, the 
package functionality is imported using the `import` statement as described 
above.  

## Creating Modules
Python files with functions that we write are also modules that can be 
imported for use in a similar manner as described above.   

Let's say we are working on a different project, with code in a file called 
`analysis.py` in which we want to use functions found in 
`calculator.py`.  We can import functions from 
`calculator.py` into `analysis.py` for use.  Example:
```python
# analysis.py

import calculator

# calculate number of seconds in a day
sec_in_hour = calculator.multiply(60, 60)
sec_in_day = calculator.multiply(24, sec_in_hour)
print("The number of seconds in a day is {}.".format(sec_in_day))
```

This code imports all of the functions from the `calculator.py` module 
such that they can be used in the `analysis.py` module.

### Perils of module-level code

However, you will notice that when `analysis.py` is run, it does not print out 
the expected results of seconds in a day.  Rather, it asks the user for a 
letter input.  This is not found in the `analysis.py` code.  Only after the 
user enters a letter and then two numbers does the expected output display.

What happened?  When `python analysis.py` is entered at the command line, the 
Python interpreter starts looking at the top of the `analysis.py` file.  The 
first statement it sees is `import calculator`.  The Python interpreter then 
goes to `calculator.py` file and starts scanning from the top.  It sees a 
variety of function definitions which it stores in memory.  Then, it comes 
across the direct statement `operator = input("Enter a letter: ")`. 
It therefore executes this statement and those that follow, 
giving the extra output not desired.  Only when this execution is
complete does control go back to the `analysis.py` module.

How can we prevent the execution of these "module-level" statements when
importing functions into another module?

### `if __name__ == "__main__":`

All of the module-level code that is not part of a defined function should be
put in an `if` statement as follows:

```python
if __name__ == "__main__":
```  

When a module is being executed by Python, it has a special variable in the
Python operating space called `__name__`.  If the module is called directly
from the command line, the value of `__name__` for that module will be
`__main__` because it is the main module of the program.

Lets modify the code in `calculator.py` so that the module-level code now looks
as follows:

```
# calculator.py

*** Functions not shown for brevity ***

if __name__ == '__main__':
    operator = input("Enter a letter:")
    print("You entered {}".format(operator))
    
    *** Code omitted for brevity ***
    
    print("{} {} {} = {}".format(a, symbol, b, answer))

```
If the command `python calculator.py` is run from the command line, 
the Python interpreter will
start at the top of the `calculator.py` file.  It will register the defined 
functions.  Then,
it will come across the statement `if __name__ == '__main__':`.  Since this
module was started from the command line, its value for `__name__` will be
`__main__` and the `if` statement will be true.  The code in this block will
then run, which is what is desired when running the `calculator` module.

If the command `python analysis.py` is run, the Python interpreter will start 
at the top of the `analysis.py` file.  It will see the `import calculator`
statement and will then switch to the top of the `calculator.py` file.  It will
register the defined functions.  Then, it will come across the statement
`if __name__ == '__main__':`.  Since the `calculator` module was not started
from the command line, its `__name__` is NOT `__main__` and so the `if` 
statement will be false.  None of the lines within the `if` statement block 
will execute.  This is the desired outcome when running the `analysis` module.

So, it is always a good idea to put any module level code that you do not want
to be executed upon import either into a function or under the
`if __name__ == "__main__":` statement.

By use of the `if __name__ == '__main__':` block, we can write a module that
can be successfully executed directly as well as allow its individual functions
to be imported into other modules.  

## Import Syntax

The examples of `import` above import all of the functions of a module, and
the imported functions are accessed by the syntax 
`<module_name>.<function_name>`.

There is also syntax for importing only a single function from a module:
```python
# analysis.py

from calculator import multiply

# calculate number of seconds in a day
sec_in_hour = multiply(60, 60)
sec_in_day = multiply(24, sec_in_hour)
print("The number of seconds in a day is {}.".format(sec_in_day))
```
In this case, only the `multiply` function from `calculator` is imported and
the module name prefix is not required for the function call.     
This method should be used carefully in that it makes it less clear where the
`multiply` function originates.  

A compromise between the brevity of the second method and the explicitness of
the first method is found in this syntax:
```python
# analysis.py

import calculator as calc

# calculate number of seconds in a day
sec_in_hour = calc.multiply(60, 60)
sec_in_day = calc.multiply(24, sec_in_hour)
print("The number of seconds in a day is {}.".format(sec_in_day))
```
The `calculator` module is imported and is referenced by the alias `calc`.

Finally, you will sometimes see imports done as follows:
```python
# analysis.py

from calculator import *

# calculate number of seconds in a day
sec_in_hour = multiply(60, 60)
sec_in_day = multiply(24, sec_in_hour)
print("The number of seconds in a day is {}.".format(sec_in_day))
```
In this syntax, all of the functions in `calculator` are imported, and you do
not need to reference the module name when calling the imported functions.
This approach is not considered best practice in that you may be 
bringing in many functions that you don't need, and it is not obvious in the
code which functions are native to which module.  So, use this approach with
caution.

