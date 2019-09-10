# `return`
Every function in python returns something to the calling procedure.  If the
calling procedure does not use the return value, it is simply ignored.

The `return` keyword is used to end the current function and return whatever
value is specified after `return` to the calling procedure.  If nothing
follows the `return` keyword, the function returns the `None` object.  If
`return` is not included in a function, the function will also return `None`
when it runs out of code in its block.

#### Example 1
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

#### Example 2
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

#### Example 3
```python
def myfunction(-20):
    a = x + 5
    return a

if __name__ == '__main__':
    y = myfunction(2)
    print(y)
    
Output:
-15
```
When a value or variable is given after `return`, that value is returned to
the calling function.

#### Example 4
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

