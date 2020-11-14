# Robust and Comprehensive Unit Testing

Expanding on the basic idea of testing units of code from last class, we 
should take some time to consider common ways to write robust unit tests. 
Generally, tests should cover a wide variety of inputs your "unit" will 
receive including "bad" inputs (for example, if you were expecting an integer, 
what happens when someone passes your code a float?). Code written with tests 
that only test expected use cases will usually fail in unexpected ways in 
production.

## Examples of Bad Input
Here is a basic example.  Let's say you have a function that checks if two
fruits are the same:
```
def is_same_fruit(a, b):
    return a == b
```
What happens when someone types in `" apple"` and you try and compare that to
`"apple"` in your code?  The above procedure would return `False`.  But, in
actual use, we would want this function to return `True`.  So, we should write
a test to ensure `is_same_fruit` returns `True` when given these two
inputs.  Then, we need to make sure our code passes that unit test.

Another typical example of bad input is receiving the wrong type of input.
For example, you may have a function that expects a list of numbers.  But,
what if the function receives `[1, 2, "3", 4, "Hello", 5]`.  What would
happen?  Write a test with this  type of input and then ensure your function
handles it gracefully.

## Testing Multiple Cases Using Parametrized Testing
It is often helpful to run a test over many different input and expected 
output combinations. `pytest` provides a tool to streamline that process
--a decorator called `parametrize`. We will talk more about 
[decorators](https://www.python-course.eu/python3_decorators.php) later in 
this class, but they allow your python functions to be augmented (or 
"decorated") with some additional functionality. The `parametrize` decorator 
lets us run a test function many times with different inputs and outputs.

A simple example is as follows.  Suppose we want to test this basic function:
```py
def add(a, b):
    return a + b
```

Here's a test that tests against many input and expected output combinations:
```py
@pytest.mark.parametrize("a, b, expected", [
    (1, 2, 3),
    (2, 3, 5),
    (5, 5, 10),
])
def test_add_parametrize(a, b, expected):
    answer = add(a, b)
    assert answer == expected
```

We can break this down further:
```py
@pytest.mark.parametrize("a, b, expected", [
    (1, 2, 3),
    (2, 3, 5),
    (5, 5, 10),
])
```
This part of the code is the "decorator." When the python interpreter runs 
this, it knows to augment the function below it in a certain way--in this case, 
it knows to essentially copy the test function below the decorator 3 times and 
call it 3 times with each set of inputs defined in the list.

Notice the decorator function takes two arguments. A string `"a, b, expected"` 
and a list of tuples `[(1, 2, 3), (2, 3, 5), ...]`. 

The string must match the named input parameters of your function, which you 
can see in the function definition (`def test_add_parametrize(a, b, expected):`).

The list of tuples is the list of input & expected output arguments to call 
the test function with. Each set of arguments is treated as a separate test 
case by `pytest` when you run `pytest`.


__Note__:  By adding the decorator described above, we now have a specific 
reference to `pytest` in our code file.  For the decorator to be recognized, 
we must import pytest in the module (```import pytest```) for the decorator to 
work. 

## Approximations
Floating point values can have numerical round-off error.
```python
a = 0.1 + 0.2
print(a == 0.3)
False
print(0.3 - a)
-5.551115123125783e-17
```
This round-off error a common way
for direct-equality assertions to fail.  `pytest` has a way to deal
with this called `approx`.
```python
import pytest
print(a == pytest.approx(0.3))
True
```

#### Approx references:
* https://docs.pytest.org/en/latest/reference.html#pytest-approx
* https://docs.scipy.org/doc/numpy/reference/generated/numpy.testing.assert_approx_equal.html


# In Class Exercise
* Write a function to subtract two numbers.
* Write a function to find the minimum and maximum of a list.
* Write unit tests for these functions.  Write at least one test that
checks for failure (i.e., gives bad input and expects False)
* Push to a GitHub repository
* Activate GitHub Actions and implement automated testing.