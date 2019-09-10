# Modules
An advantage of defining functions within a Python module file is that
you can import these functions into other modules.

In a previous lecture, we created a module called `calculator.py`:
```python
# calculator.py

def check_HDL(HDL):
    if HDL >= 60:
        return "Normal"
    elif 40 <= HDL < 60:
        return "Borderline Low"
    else:
        return "Low"
        
def check_LDL(LDL):
    if LDL < 130:
        return "Normal"
    elif 130 <= LDL <= 159:
        return "Borderline high"
    elif 159 < LDL <= 189:
        return "High"
    else:
        return "Very High"        

def cholesterol_check():
    print("Cholesterol Check")
    chol = input("Enter your cholesterol result: ")
    chol_data = chol.split("=")
    if chol_data[0] == "HDL":
        result = check_HDL(int(chol_data[1]))
        print("The HDL cholesterol level is {}.".format(result))
    elif chol_data[0] == "LDL":
        results = check_LDL(int(chol_data[1]))
        print("The LDL cholesterol level is {}.".format(results))

def interface():
    print("My Calculator Program")
    keep_running = True
    while keep_running:
        print("Options:")
        print("1 - Cholesterol Check")
        print("9-Quit")
        choice = input("Choose an option:  ")
        if choice == '9':
            keep_running = False
        elif choice == '1':
            cholesterol_check()

if __name__ == '__main__':
    interface()
```

Let's say we are working on a different project, with code in a file called 
`analysis.py` in which we want to use the `check_HDL` function found in 
`calculator.py`.  We can import functions from 
`calculator.py` into `analysis.py` for use.  Example:
```python
# analysis.py

from calculator import check_HDL

HDL_test_result = 45
diagnosis = check_HDL(HDL_test_result)
print("The HDL level is {}.".format(diagnosis))
``` 
Output:
```
The HDL level is Borderline Low.
```

This code imports the function `check_HDL` from the `calculator.py` module 
such that it can be used in the `analysis.py` module.

Another syntax for importing a module is as follows:
```python
# analysis.py

import calculator

HDL_test_result = 45
HDL_diagnosis = calculator.check_HDL(HDL_test_result)
print("The HDL level is {}.".format(HDL_diagnosis))
LDL_test_result = 80
LDL_diagnosis = calculator.check_LDL(LDL_test_result)
print("The LDL level is {}.".format(LDL_diagnosis))
```
Output:
```
The HDL level is Borderline Low.
The LDL level is Normal.
```
In this case, all of the functions from `calculator` are imported.  But, with
this syntax, the module name and the function name need to be used to call
the function.  We can make this easier by using an alias as follows:
```python
# analysis.py

import calculator as calc

HDL_test_result = 45
HDL_diagnosis = calc.check_HDL(HDL_test_result)
print("The HDL level is {}.".format(HDL_diagnosis))
LDL_test_result = 80
LDL_diagnosis = calc.check_LDL(LDL_test_result)
print("The LDL level is {}.".format(LDL_diagnosis))
```
The `calculator` module is imported and is referenced by `calc`.

Finally, you will sometimes see imports done as follows:
```python
# analysis.py

from calculator import *

HDL_test_result = 45
HDL_diagnosis = check_HDL(HDL_test_result)
print("The HDL level is {}.".format(HDL_diagnosis))
LDL_test_result = 80
LDL_diagnosis = check_LDL(LDL_test_result)
print("The LDL level is {}.".format(LDL_diagnosis))
```
In this syntax, all of the functions in `calculator` are imported, and you do
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
`calculator.py` module, so it looks like this:
```python
# calculator.py

def check_HDL(HDL):
    if HDL >= 60:
        return "Normal"
    elif 40 <= HDL < 60:
        return "Borderline Low"
    else:
        return "Low"
        
def check_LDL(LDL):
    if LDL < 130:
        return "Normal"
    elif 130 <= LDL <= 159:
        return "Borderline high"
    elif 159 < LDL <= 189:
        return "High"
    else:
        return "Very High"        

def cholesterol_check():
    print("Cholesterol Check")
    chol = input("Enter your cholesterol result: ")
    chol_data = chol.split("=")
    if chol_data[0] == "HDL":
        result = check_HDL(int(chol_data[1]))
        print("The HDL cholesterol level is {}.".format(result))
    elif chol_data[0] == "LDL":
        results = check_LDL(int(chol_data[1]))
        print("The LDL cholesterol level is {}.".format(results))

def interface():
    print("My Calculator Program")
    keep_running = True
    while keep_running:
        print("Options:")
        print("1 - Cholesterol Check")
        print("9-Quit")
        choice = input("Choose an option:  ")
        if choice == '9':
            keep_running = False
        elif choice == '1':
            cholesterol_check()

interface()
```
If this module is run by entering the command `python calculator.py` it will 
run exactly
the same way as it did with the `if __name__ == "__main__":` statement.  The
Python interpreter will start at the top of the file, see a variety of 
function definitions, and then start executing the statements found at the
module level starting with `inteface()`.

Now, what happens if we go back to the `analysis.py` module, and run it while
importing functions from this modified `calculator.py` file.

If we type `python calculator.py`, here is the output we get now:
```
My Calculator Program
Options:
1 - Cholesterol Check
9-Quit
Choose an option:  9
The HDL level is Borderline Low.
```

Notice that the user was asked for an option.  When the user entered `9` for
Quit, only then did the expected output
from the `analysis.py` program be displayed.

What happened?  `analysis.py` does not have any input statements, and doesn't
call the `interface()` code from `calculator.py`.

As always, the Python interpreter started at the top of the
`analysis.py` file.  The first statement it sees is
`import calculator`.  The Python interpreter then goes to 
`calculator.py` file and starts scanning from the top.  It sees a variety of
function definitions which it stores in memory.  Then, it comes across 
the direct statement `interface()` in the module.  It therefore executes this 
statements, giving the extra outputs not desired.  Only when this execution is
complete does control go back to the `analysis.py` module.

Here is the value of the `if __name__ == "__main__":` statement.  In the case
where `calculator.py` has this statement, when `calculator` is imported
into `analysis`, it will see all of the function definitions, and them come
to the `if __name__ == "__main__":` statement.  Since this imported module
is not the `__main__` module, the commands within this `if` block will not run.

So, it is always a good idea to put any module level code that you do not want
to be executed upon import either into a function or under the
`if __name__ == "__main__":` statement.
