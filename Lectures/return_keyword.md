# `return`
Every function in python returns something to the calling procedure.  If the
calling procedure does not use the return value, it is simply ignored.

The `return` keyword is used to end the current function and return whatever
value is specified after `return` to the calling procedure.  If nothing
follows the `return` keyword, the function returns the `None` object.  If
`return` is not included in a function, the function will also return `None`
when it runs out of code in its block.

#### Example 1 - No `return` used
```python
def myfunction(x):
    a = x + 5


if __name__ == '__main__':
    y = myfunction(-20)
    print(y)

Output:
None
```
When the function runs out of code without finding a `return` statement, it
returns `None`.  This is an objects of its own in Python and is not a string.

#### Example 2 - `return` used alone
```python
def myfunction(x):
    a = x + 5
    return

if __name__ == '__main__':
    y = myfunction(-20)
    print(y)

Output:
None
```
Sometimes for clarity, a `return` may be added at the end of a function even
if no value is being returned.

#### Example 3 - `return` with a value
```python
def myfunction(x):
    a = x + 5
    return a

if __name__ == '__main__':
    y = myfunction(-20)
    print(y)
    
Output:
-15
```
When a value or variable is given after `return`, that value is returned to
the calling function.

#### Example 4 - multiple `return` types
```python
def myfunction(x):
    a = x + 5
    if a < 0:
        return "a cannot be negative"
    else:
        return a

if __name__ == '__main__':
    y = myfunction(2)
    print(y)

Output:
a cannot be negative
```
Note that a function can return different types of values at different
locations.  In this example, it sometimes returns an integer.  Sometimes it
returns a string.  This is not considered best practice because the calling
procedure now needs to be able to handle either an integer return or a string
return.

#### Example 5 - `return` multiple variables
```python
def division_results(dividend, divisor):
    full = dividend / divisor
    quotient = dividend // divisor
    remainder = dividend % divisor
    return full, quotient, remainder


if __name__ == '__main__':
    i = 11
    j = 3
    a, b, c = division_results(i, j)
    print("The result of {} divided by {} is {}".format(i, j, a))
    print("The quotient is {}".format(b))
    print("The remainder is {}".format(c))
 
Output:
The result of 11 divided by 3 is 3.6666666666666665
The quotient is 3
The remainder is 2

```
More than one variable can be returned, as shown in the example above.  In the
case above, the different return values are captured in different variables.
Another approach is to capture all the return values into a single variable
which will be a tuple.  The last four lines of code from above would be
modified as follows:
```python
    answers = division_results(i, j)
    print("The result of {} divided by {} is {}".format(i, j, answers[0]))
    print("The quotient is {}".format(answers[1]))
    print("The remainder is {}".format(answers[2]))
```

#### Example 6 - `return` ends a function right away
```python
def print_information(age):
    print("In this section, information is shared for all patients.")
    print("   Information for All")
    if age < 18:
        return
    print("In this section, information is shared with adults only.")
    print("   Information for Adults Only")


if __name__ == '__main__':
    print_information(15)

Output:
In this section, information is shared for all patients.
   Information for All
```
A function ends when a return is reached.