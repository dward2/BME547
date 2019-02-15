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
occurs when your command attempts to run.  For example:
```
f = open('file.bin', 'rb')
```
While this command is syntactically correct, if the file `file.bin` does not
exist, then this command cannot be executed and will raise an exception:
```
FileNotFoundError: [Errno 2] No such file or directory: 'file.bin'
```
Other common exception errors are:
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
As another example, you may want to raise an exception if inputs to a function
are the wrong type:
```python
# This function may raise a TypeError if called with certain args:                                                                                                                                                                     
def add(a, b):                                                                                                                                                                                                                         
    if type(a) is not int or type(b) is not int:                                                                                                                                                                                       
        raise TypeError("Inputs must be python ints")                                                                                                                                                                                  
    return a + b                                              
```
In the example above, if the inputs to this function are not integers, the 
caller of this function is notified (and the program as a whole) that an error 
condition has occurred (and in particular it's a TypeError) by raising this 
exception. If the calling function does not handle this exception then the 
program will crash.

As above, the list of possible exceptions that can be raised can be found at
https://docs.python.org/3/library/exceptions.html

### What happens when an exception is raised
When you raise an exception, code execution in that function stops at that 
point and the exception propogates up to the caller of the function. The 
function does not return anything. The caller of your function can deal with 
the exception with a `try/except` block (for example, re-prompting the user for 
proper input) or it can allow the exception to propagate through the program 
until it crashes with an error message.

### Example
```python
def get_compass_direction_entry():
    compass_direction = input("Enter N/S/E/W or Q for quit: ")
    return compass_direction
    
def move_direction(direction):
    continue_moving = True
    available_directions = ["N", "E", "S", "W", "Q"]
    if direction not in available_directions:
        raise ValueError("Not a valid direction")
    if direction == "N":
        print("Move north")
    elif direction == "E":
        print("Move east")
    elif direction == "S":
        print("Move south")
    elif direction == "W":
        print("Move west")
    elif direction == "Q":
        print("Quit")
        continue_moving = False
    return continue_moving
 
def main_loop():
    continue_loop = True
    while continue_loop:
        entry = get_compass_direction_entry()
        try:
            continue_loop = move_direction(entry)
        except ValueError:
            print("Please enter one of the requested characters.")
    return
    
if __name__ == "__main__":
    main_loop()
```
In the example above, the user is prompted to enter a character in the line
`entry = get_compass_direction_entry()` in the `main_loop()`.  The character
entered is then sent to the `move_direction()` function in a `try` block.

In `move_direction()`, the entered character is checked against a list of 
acceptable characters. If it is not in this list, a `ValueError` exception
is raised ending the `move_direction()` function and telling `main_loop()`, 
which called `move_direction()`, that the sent value is incorrect.  Rather than
the program crashing from this error, the `except ValueError:` block handles
this exception by telling the user to enter something different and then 
allowing the loop to continue.

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

There is a dedicate module to system error symbols: 
https://docs.python.org/3/library/errno.html

### Another Example of Using Warnings and Sys.Exit
```python
# An example of polling the voltage on a GPIO pin that needs to be within
# +/- 0.3 V of 5 V, and will give unreliable operation if it deviates more
# than +/- 0.5 V

def check_voltage_deviation(voltage):
    from warnings import warn
    import sys
    from numpy import abs

    volt_deviation = abs(voltage - 5.0)

    if volt_deviation > 0.5:
        # 0 is normal termination
        # 1 is abnormal termination
        sys.exit("Voltage of {} has deviated too much (deviation of {} V)!"
                 .format(voltage, volt_deviation))
    if volt_deviation > 0.3:
        warn("Voltage of {} is drifting a bit too much (deviation of {} V)."
             .format(voltage, volt_deviation))
    else:
        print("Voltage of {} is within tolerance.".format(voltage))

def main():
    voltage_from_gpio_pin = [5.0, 5.1, 5.3, 4.5, 5.0, 2.0, 5.5, 5.0]

    for v in voltage_from_gpio_pin:
        check_voltage_deviation(v)

if __name__ == "__main__":
    main()
```
Output:
```
Voltage of 5.0 is within tolerance.
Voltage of 5.1 is within tolerance.
Voltage of 5.3 is within tolerance.
D:/ClassRepos/GeneralStudentDebugging/script.py:19: UserWarning: Voltage of 4.5 is drifting a bit too much (deviation of 0.5 V).
Voltage of 5.0 is within tolerance.

Voltage of 2.0 has deviated too much (deviation of 3.0 V)!

Process finished with exit code 1

```

## References
https://docs.python.org/3/tutorial/errors.html
