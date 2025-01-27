# Unit Testing of User Input/Output with `pytest`

In general, good modular programming would separate input and output 
commands from code that does algorithmic work and calculations by putting 
I/O into their own functions and algorithmic work and calculations into 
their different functions.  By doing so, the algorithmic and calculation 
functions will generally have defined input and output variables to allow 
for definitive testing.  And, functions that only do input/output can be 
skipped in unit testing.

However, there may be times where separating input/output from other code 
is problematic. Or, you may want to test your input/output code for some 
reason.  `pytest` does not allow for direct, interactive user input.  But, 
it does have capabilities for "mocking" pre-defined user input and 
capturing console output in order to write input/output tests.

## Testing Output To Console

`pytest` can capture output that is sent to either the standard output channel 
 (`stdout`) or the standard error channel (`stderr`).  It does this using 
the `capsys` fixture that can be given as a parameter to the unit test 
function.

Let's say you want to test that an appropriate output is sent to the 
console by a function.  An 
example unit test function in would look as follows:

```python
def test_my_output_function(capsys):
    # Arrange
    from my_module import my_output_function
    input_parameter = "abc"
    expected = "The output is abc\n"
    # Act
    my_output_function(input_parameter)
    captured = capsys.readouterr()
    answer = captured.out
    # Assert
    assert answer == expected
```

In the example above, we first "arrange" the data necessary to run the test.  
The function to be tested is imported.  The parameter to be sent to the 
function to be tested is defined in the `input_parameter` variable.  And, 
the expected output from the function is defined in the `expected` variable.
Note that you will need to include the new line character (`\n`) in the 
expected output unless you suppressed its output.

The test function "acts" by calling the output function.  Then, the 
`capsys` parameter is used to access the capture fixture and its `readouterr` 
method is called that returns a named tuple that is stored in the 
`captured` variable.  `captured.out` contains any output captured from the 
standard output channel.  This captured output can be compared against the 
expected output using `assert`.  

If you wanted to check any error output, you would use `captured.err`
instead. 

If you wanted to use the `parametrize` decorator to run multiple tests, you 
can specify the needed parameters ahead of the `capsys` parameter as follows:

```python
@pytest.mark.parametrize("input_parameter, expected", [
    ("abc", "The output is abc\n"),
    ("def", "The output is def\n")
])
def test_my_print(input_parameter, expected, capsys):
```


## Testing Input From Console
If you want to test a function that accepts user input from the console, 
you need to "mock" the input function to provide the needed input rather 
than expecting it from the user.  This is a more complicated approach than 
capturing the output as above.

Mocking is when we replace a function, data class, or other python object 
with a "mock" item that will return the information needed for the function 
that is being tested.  Let's look at the very simply function below:

```python
def add_input(first_value):
    second_value = input("Enter an integer: ")
    return first_value + int(second_value)
```

This function asks for the user to input an integer, and that integer is 
added to an integer sent the function as a parameter.  Using `pytest`, we 
know how to write a unit test that can send a value for the `first_value` 
parameter and check the return value.  But, how do we tell `pytest` what 
the result of the "input" function will be?  That is where we will "mock" 
the `input` function so it returns a known value, instead of waiting for 
user input.  

`pytest` provides the `monkeypatch` fixture to enable this type of "mocking".
`monkeypath` allows us to change the built-in Python function `input` to a 
different function of our own choosing.

```python
def test_add_input(monkeypatch):
    # Arrange
    from my_module import add_input
    first_value_input = 1
    user_input = "3"
    expected = 4
    monkeypatch.setattr('builtins.input', lambda _: user_input)
    # Act
    answer = add_input(first_value_input)
    # Assert
    assert answer == expected
```

In the "Arrange" section, the value to be sent to the function being tested as
a parameter is defined in the `first_value_input` variable. The string that we
want the "mock" input function to return is defined in the `user_input` 
variable. The `expected` variable is given the value expected from the 
function to be tested. Then, the "mocking" command is
```python
monkeypatch.setattr('builtins.input', lambda _: user_input)
```
  
This line "replaces" the built-in Python `input` function with our own function
that will return the desired user_input. The `monkeypatch. setattr` method
takes two parameters:

1. The first is a string that references the object that is to be replaced with
   our mock function. In this case, we want to replace the `builtins.input`
   function.
2. The second parameter is a reference to our mock function. We are replacing
   it with a `lambda` function, which is a one-time defined function. In this
   case, the function simply returns the value in the `user_input` variable.

The "Act" and "Assert" sections then run the function to be tested and 
assert the answer.

## References
* <https://docs.pytest.org/en/stable/how-to/capture-stdout-stderr.
html#accessing-captured-output-from-a-test-function>
* https://docs.pytest.org/en/6.2.x/monkeypatch.html
* https://docs.pytest.org/en/stable/reference/reference.html#monkeypatch