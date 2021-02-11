# Mutable and Immutable Data Types

This is one of the trickiest topics in Python.  Different data types
exhibit different behavior, particularly with respect to making changes and
using variables of these data types as parameters.

First, we need to understand the difference between a variable and a data type,
and then the difference between a mutable and immutable variable is in Python.

## Data Type vs. Variable
A data type is the specific form in which a piece of data can exist.  A 
partial list is below.
* The integer data type (`int`) is a whole number (ex: `-3`, `0`, `23`).
* The string data type (`str`) is a list of alphanumeric characters (ex: `"a"`, 
  `"d"`, `"hello"`, `"1da390d"`).  
* The float data type (`float`) is a decimal number (ex: `3.14159`).
* The tuple data type (`tuple`) is a list of data (ex: `(1, 2)`, `("a", True, 
  15.3)`).
* The list data type (`list`) is also a list of data (ex: `[1, 2]`, `["a", 
  True, 15.3]`).
* The dictionary data type (`dictionary`) is a set of key:value pairs (ex: 
  `{"name": "Gary Jones", "age": 17}`).  
  
A variable is a container for a specific instance of one of these variable 
types.  A variable can hold any data type and can change its data
type during the program.  This is why Python is considered a dynamically-typed
language, because the data type of variables does not need to be pre-defined
and can even change during program execution.

So, the Python command `a = 5` points the variable `a` to the value of 5 which
is an integer data type.

## Immutable Data Types
`int`, `str` and `tuple` data types are considered immutable.  What does
this mean?  I think it is easiest to demonstrate by example.

Let's start by assigning the variable `a` to the integer value of 5.
```python
a = 5
```
First, Python creates a portion of memory to contain the integer value of 5.
Then, Python points the `a` variable to look at this memory location.
This area of memory has an id, and we can see what this id is with the `id()` 
function.  We can also see what data type is contained in the variable using
the `type()` function.
```python
print(id(a))    # Output:  2090137584
print(type(a))   # Output: <class 'int'>
```
_Note: the actual value output for the id will likely vary each time the 
program is executed, so you will likely not see the exact same number above if 
you run this yourself._

This integer value of 5 is immutable.  That memory address and that id will
always contain the value of 5.  So, if the value assigned to the variable `a`
needs to change, Python will actually point the variable `a` to a new memory
location that contains the new value.
```python
a = a + 2
print(a)       # Output: 7
print(id(a))   # Output: 2090137616
```
In the code above, the variable `a` which starts with a value of 5 needs to
change to the value of 7.  `a` currently points to the integer 5 which is 
immutable.  So, to update the value of `a` to 7, Python points the variable `a`
to a new memory location that contains the value of 7.  

The same things happens with a `str` variable type.
```python
b = "dog"
print(type(b))    # Output: <class 'str'>
print(id(b))      # Output: 78652352
b = b + "s"
print(b)          # Output: dogs
print(id(b))      # Output: 78654304
```

So, `int` and `str` data types are immutable.  Therefore, when variables that
contain those data types need to change their value, those variables need to 
change the location in memory to which they are pointing.

## Mutable Data Types
`list` and `dictionary` are mutable data types.  How do they work?  Again,
let's look at an example.

```python
c = [15, 23, 9]
print(type(c))    # Output: <class 'list'>
print(id(c))      # Output: 78653416
```
A `list` data type points to a portion of memory that is designed to be 
flexible in how much information it can contain.  So, if the information in
the memory needs to change or be added to, the same memory location is used.

```python
c.append("Hello")
print(c)            # Output: [15, 23, 9, 'Hello']
print(id(c))        # Output: 78653416
c[1] = True
print(c)            # Output: [15, True, 9, 'Hello']
print(id(c))        # Output: 78653416
```
In the example above, we can see that we changed the content of the list, but
the id of the variable containing the list remained the same.

## Immutable and Mutable Data Types as Function Parameters
Because of the difference between immutable and mutable data types, variables
that contain the two different types act differently when sent as parameters
to a function.

### Immutable parameters
Let's look at the following code as an example:
```python
def add_two(x):
    print("In add_two as received")
    print("  ID of x = {}     Value of x = {}\n".format(id(x), x))
    x = x + 2
    print("In add_two after modification")
    print("  ID of x = {}     Value of x = {}\n".format(id(x), x))

def main():
    y = 5
    print("In main before sending as parameter")
    print("  ID of y = {}     Value of y = {}\n".format(id(y), y))
    add_two(y)
    print("In main after sending as parameter")
    print("  ID of y = {}     Value of y = {}\n".format(id(y), y))

if __name__ == '__main__':
    main()
```
The output of this code is:
```
In main before sending as parameter
  ID of y = 920     Value of y = 5

In add_two as received
  ID of x = 920     Value of x = 5

In add_two after modification
  ID of x = 952     Value of x = 7

In main after sending as parameter
  ID of y = 920     Value of y = 5
```
_Note: For ease, I have shortened the id numbers._

When the `main()` function is run, the variable `y` is created and its integer
value of 5 is stored in memory at the id of 920.  This memory location is
immutable and will always contain the value of 5.  This variable is then sent
as a parameter to the `add_two()` function.  The parameter `x` in the 
`add_two()` function is pointed to the same memory location as `y` (920), so it 
has the same value.  When the `x` value is incremented by 2, its value needs
to change.  Since the integer 5 is immutable, the variable `x` needs to point
to a new memory location that contains the value of 7.  So, Python redirects
where the variable `x` is pointing to the memory location of 952 which contains
the value of 7.  

When the function ends, control returns to the `main()` function.  Here, the
`y` variable still points to the id 920, which still contains the value of 5.
So, when a variable containing an immutable data type is sent as a parameter,
the value of the variable that is sent as a parameter is not changed by the 
function.

### Mutable parameters
Let's look at another similar example, but one that uses a mutable data type as
a parameter:
```python
def add_two(x):
    print("In add_two as received")
    print("  ID of x = {}     Value of x = {}\n".format(id(x), x))
    x[0] = x[0] + 2
    print("In add_two after modification")
    print("  ID of x = {}     Value of x = {}\n".format(id(x), x))

def main():
    y = [5, 10, 15]
    print("In main before sending as parameter")
    print("  ID of y = {}     Value of y = {}\n".format(id(y), y))
    add_two(y)
    print("In main after sending as parameter")
    print("  ID of y = {}     Value of y = {}\n".format(id(y), y))

if __name__ == '__main__':
    main()
```
Output:
```
In main before sending as parameter
  ID of y = 872     Value of y = [5, 10, 15]

In add_two as received
  ID of x = 872     Value of x = [5, 10, 15]

In add_two after modification
  ID of x = 872     Value of x = [7, 10, 15]

In main after sending as parameter
  ID of y = 872     Value of y = [7, 10, 15]

```
When the `main()` function is run, the `y` variable is created and points to a
section of memory that contains a mutable `list` data type.
This mutable data type is stored at the id of 872.  When `y` is sent as a
parameter, its value is stored in the variable `x` within the `add_two()`
function and points to the same `id` number of 872 as it should have the same
value.  When the variable `x` is modified in
`add_two()`, since it is pointing to a mutable data type, it can change the 
value of the
data without needing to make a new memory location.  So, the data at the 
memory location 872 is changed and `x` continues to point to that location.

When control is returned to the `main` function, the `y` variable in `main`
continues to point at the same location of 872.  And, the data in this location
has changed.  So, when a variable whose value is a mutable data type is sent as 
a parameter to a function, the value of that variable that is sent is 
changed by the function.