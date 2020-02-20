# Exceptions
There are two primary types of Python "errors":
1. Syntax Errors
2. Exceptions
## Syntax Errors
Syntax errors violate the coding syntax, meaning that the Python interpreter
cannot interpret your code.  For example:
```
print "The sky is blue."
``` 
This yields the following syntax error output upon executing the code:
```
print "The sky is blue."
                       ^
SyntaxError: Missing parentheses in call to 'print'
```
The arrow points to where the syntax is invalid, and the error message 
[attempts to] convey what is wrong.

## Exceptions
In contrast, Exceptions are raised when you have valid syntax, but an error
occurs when your command attempts to run.  

## Class Exercise (5 min)
* Write a function that will generate an exception error.
* Call this function from another function.
* Run code and verify that error is achieved.
* Share with the class:  what error you found?

## Exception Errors
Common exception errors are:
  * ``ZeroDivisionError``
  * ``NameError`` (trying to use a variable name that is not defined)
  * ``TypeError`` (mixing conflicting types of data in an operation, or passing
   a function variable input type that is not supported)
  * ``AssertionError``
  * ``ImportError``
  * ``IOError``
  * ``EOFError``

There is a comprehensive list of built-in exceptions here:
https://docs.python.org/3/library/exceptions.html

## How do we deal with exceptions gracefully?  `try/except`
Syntax errors are caught and corrected with our unit tests and development
testing, but exceptions can happen during device function.  We don't want our
code to abruptly stop when an exception occurs, but instead, we want a planned
procedure to deal with exceptions.

`try/except` allows us to "try" to execute a segment of code, and if an 
exception is raised, then the "except" code is executed instead.  Our "excepts" 
can be tailored to the specific exception error.

## Class Exercise
* Implement `try/except` fix in your code


### Pseudo-Code
```
def main():
    try:
        do_stuff()
    except ErrorType1:
        clean_up_from_Error1()
    except ErrorType2:
        clean_up_from_Error2()
    except:
        clean_up_from_any_other_error()
    else:
        code_to_run_after_do_stuff_with_no_exceptions()
```
### Example
```python
def div_example():
    for x in [3, 5, 7, 0, 9]:
        try:
            y = 1/x
        except ZeroDivisionError:
            print("div by 0, skipping this iteration")
            continue
        print("Inverse of {} is {}".format(x, y))
```

### `finally` clause
If there some code you would like to have regardless of whether there is an
error or not, you can add a `finally` clause.
```python
def open_file_example(filename):
    try:
        in_file = open(filename, "r")
    except FileNotFoundError:
        print("The file did not exist.  Choose another file.")
    except:
        print("There was a different error.")
    finally:
        print("The function `open_file_example` is finished.")
    return
    
```

## Raising Exceptions
### Why and When?
There may be times where we want to have our own code raise exceptions.
Generally, we should raise exceptions in our code to signal that some sort 
of error has occurred in a function (like inputs being the wrong type) that 
will not allow for safe and successful execution of the code. And, the goal of 
raising an exception is to notify the caller of the function
that something has gone wrong and needs to be fixed for continued operation.

### How to raise an exception
To raise an exception in Python to indicate an error, we use the `raise` 
command.  An example:
```python
raise ValueError("This message string gives more information and context about" 
                    "why this error was raised")
```
#### Pseudo-Code:
```
if some_condition_I_don't_like is True:
    raise ErrorType("Why I am unhappy")
```

## Class Exercise
* Write a function called `add_two_numbers(a, b):`
* Have this function return the sum of the two numbers
* If the variables `a` or `b` do not contain an `int` variable, raise a `TypeError` exception.
* If the variables `a` or `b` contain a negative number, raise a `ValueError` exception.
* Call this function multiple times with integers and non-integers and see what happens.

## What happens when an exception is raised
When you raise an exception, code execution in that function stops at that 
point and the exception propogates up to the caller of the function. The 
function does not return anything. The caller of your function can deal with 
the exception with a `try/except` block (for example, re-prompting the user for 
proper input) or it can allow the exception to propagate through the program 
until it crashes with an error message.

## Class Exercise
* Write another function that calls `add_two_numbers()` and have that function 
either:  
  + print out the resulting summed number  
  + prints "Needs Integers" if a `TypeError` is raised, or
  + print "No negative numbers" if a `ValueError` is raised.


## Tests for Raised Exceptions
If your function raises an exception, you will want to test if it raises the
exception successfully in the right circumstances.  An example of such a test
for the `move_direction()` function above is as follows:
```python
def test_something():
    import pytest
    from modulename import move_direction
    with pytest.raises(ValueError):
        move_direction("L")
```
This test will pass if `move_direction()` successfully raises a ValueError

## Class Exercise
* Write tests for `add_two_numbers` that tests whether `ValueError` and 
`TypeError` are successfully raised with bad inputs.

## Other Options
### Warnings
Your code may want to alert the user that some attention needs to be given to
something, but does not demand a full exception or program halt.  The 
`warning` package provides this functionality.
```python
def get_compass_direction_entry():
    from warnings import warn
    compass_direction = input("Enter N/S/E/W or Q for quit: ")
    if compass_direction == "W":
        warn("Going west is dangerous.")
    return compass_direction
```
The resulting output is shown below where a warning is given and the code line
is referenced, but the program execution continues.
```
Enter N/S/E/W or Q for quit: W
Move west
yourcode.py:5: UserWarning: Going west is dangerous.
   warn("Going west is dangerous.")
Enter N/S/E/W or Q for quit: 
```

### Program Termination
Your code may find something that warrants immediate termination of the 
program.  `sys.exit()` is the most common way to terminate program execution,
and it is most useful to provide a returned exit status to indicate why
termination occurred.

Using the same example as above, let's terminate the program if the user
wants to go west.
```python
def get_compass_direction_entry():
    import sys
    compass_direction = input("Enter N/S/E/W or Q for quit: ")
    if compass_direction == "W":
        sys.exit("Going west is too dangerous. Must stop.")
    return compass_direction
``` 
Output:
```
Enter N/S/E/W or Q for quit: W
Going west is too dangerous. Must stop.

Process finished with exit code 1
```

There is a dedicated module to system error symbols: 
https://docs.python.org/3/library/errno.html

[Logging](logging.md)

## References
https://docs.python.org/3/tutorial/errors.html
