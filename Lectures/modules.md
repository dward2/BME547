# Modules
An advantage of defining functions within a Python module file is that
you can import these functions into other modules.

In a previous lecture, we created a module:
```python
# first_module.py

def addition(x, y):
    print("Add")
    print("x = {}".format(x))
    c = x + y 
    print("{} + {} = {}".format(x, y, c))
    return
    
def subtraction():
    print("subtract")
    a = 1
    b = 2
    c = a - b 
    print("{} - {} = {}".format(a, b, c))
    return
    
def addsubtract(x, y, symbol):
    if symbol == "+":
        c = x + y 
    elif symbol == "-":
        c = x - y 
    else:
        c = "Unrecognized"
    return c 
    
if __name__ == "__main__":
    x = input("Input a command: ")
    print("You entered {}.".format(x))
    a = int(input("a = "))
    b = int(input("b = "))
    if x == 'add' or x == 'a':
        symbol = "+"
        answer = addsubtract(a, b, "+")
    elif x == "s":
        answer = addsubtract(a, b, "-")
    else:
        print("{} is not an active command.".format(x))
        print("Enter a new command.")
    print("c = {}".format(answer))  
    print("Done")
```

Let's say we have a different file called `calculator.py` in which we want to 
use the functions defined in `first_module.py`.  We can import functions from 
`first_module.py` into `calculator.py` for use.  Example:
```python
# calculator.py
from first_module import addsubtract

answer = addsubtract(4, 3, "-")
print(answer)
``` 
Output:
```
1
```

This code imports the function `addsubtract` from the `first_module` module 
such that it can be used in the `calculator` module.

Another syntax for importing a module is as follows:
```python
# calculator.py
import first_module

answer = first_module.addsubtract(4, 3, "-")
print(answer)
first_module.addition(10, 11)
```
Output:
```
1
Add
x = 10
10 + 11 = 21
```
In this case, all of the functions from `first_module` are imported.  But, with
this syntax, the module name and the function name need to be used to call
the function.  We can make this easier by using an alias as follows:
```python
import first_module as fm

answer = fm.addsubtract(4, 3, "-")
print(answer)
fm.addition(10, 11)
```
The first_module is imported and is referenced by `fm`.

Finally, you will sometimes see imports done as follows:
```python
# calculator.py
from first_module import *

answer = addsubtract(4, 3, "-")
print(answer)
addition(10, 11)
```
In this syntax, all of the functions in `first_module` are imported, and you do
not need to reference the module name when calling the imported functions.
This approach is not considered best practice by some in that you may be 
bringing in many functions that you don't need, and it is not obvious in the
code which functions are native to which module.  So, use this approach with
caution.

## The value of `if __name__ == "__main__":`
From the lecture on [variable scope](../Lectures/variable_scope.md), we saw
that variables and statements can be used directly in a module outside of a
function.  Here is where the `if __name__ == "__main__":` statement becomes
necessary.

For example, lets remove the `if __name__ == "__main__":` line from the
`first_module.py` module, so it looks like this:
```python
# first_module.py

def addition(x, y):
    print("Add")
    print("x = {}".format(x))
    c = x + y 
    print("{} + {} = {}".format(x, y, c))
    return
    
def subtraction():
    print("subtract")
    a = 1
    b = 2
    c = a - b 
    print("{} - {} = {}".format(a, b, c))
    return
    
def addsubtract(x, y, symbol):
    if symbol == "+":
        c = x + y 
    elif symbol == "-":
        c = x - y 
    else:
        c = "Unrecognized"
    return c 

x = input("Input a command: ")
print("You entered {}.".format(x))
a = int(input("a = "))
b = int(input("b = "))
if x == 'add' or x == 'a':
    symbol = "+"
    answer = addsubtract(a, b, "+")
elif x == "s":
    answer = addsubtract(a, b, "-")
else:
    print("{} is not an active command.".format(x))
    print("Enter a new command.")
print("c = {}".format(answer))  
print("Done")
```
If this module is run by entering `python first_module.py` it will run exactly
the same way as it did with the `if __name__ == "__main__":` statement.  The
Python interpreter will start at the top of the file, see a variety of 
function definitions, and then start executing the statements found at the
module level starting with `x = input("Input a command:" )`.

Now, what happens if we go back to the `calculator.py` module, and run it while
importing functions from this modified `first_module.py` file.

If we type `python calculator.py`, here is the output we get now:
```
Input a command: a
You entered a.
a = 5
b = 10
c = 15
Done
1
Add
x = 10
10 + 11 = 21
```

Notice that the user was asked for an input command, then values for a and b.
After the value of c and "Done" were printed, only then did the expected output
from the `calculator.py` program be displayed.

What happened?  `calculator.py` does not have any input statements.

As always, the Python interpreter started at the top of the
`calculator.py` file.  The first statement it sees is
`from first_module import addsubtract`.  The Python interpreter then goes to 
`first_module.py` file and starts scanning from the top.  It sees a variety of
function definitions which it stores in memory.  Then, it comes across 
direct statements in the module.  It then executes these statements, giving the
extra outputs not desired.

Here is the value of the `if __name__ == "__main__":` statement.  In the case
where `first_module.py` has this statement, when `first_module.py` is imported
into `calculator`, it will see all of the function definitions, and them come
to the `if __name__ == "__main__":` statement.  Since this imported module
is not the `__main__` module, these commands will not be run.

So, it is always a good idea to put any module level code that you do not want
to be executed upon import either into a function or under the
`if __name__ == "__main__":` statement.
