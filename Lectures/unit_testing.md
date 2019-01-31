# Unit Testing

## Unit Testing Introduction
Every step or function that has algorithmic content will be paired with a test
to ensure that the code works as desired.

### Test-Driven Development
* Write your tests before you code
* Verify function when generating new code
* Verify that new functions/code doesn't break previous functionality

### Unit Testing
* Break down code into the smallest algorithmic/functional units possible
* Write explicit tests for each of these units
* Write tests for when the units are used properly
* Write tests for when the units are used improperly and might break
* Test that the units gracefully handle exceptions

### What are "good" units?
* Functions / methods must be written with a very specific and narrow 
functional scope in mind.
* If you function does too much and requires a divergent set of tests, then
that function should be broken up into smaller functions.

### Testing Frameworks
* `unittest`
  + Ubiquitous, used by many languages
* `pytest`
  + Easy to use and install with `pip` and `conda`.
  + Has Python specific features
* `nose`
  + Extension of `unittest`
  + Active development has stopped
  
## Installing `Pytest`
Pytest is not a default package in Python, so must be installed in a virtual environment.

* `requirements.txt`
  + `pytest`
  + `pytest-pep8`
  + `pytest-cov`  
  
## Using `Pytest`

Pytest automatically discovers all files in your folder that start with "test".
(This is a default that can be changed, but we are going to leave it as is.)
And, `pytest` will run each test in these files that start with "test".

For example, take the following code to be tested.
```
# temp_conversion.py

def celsius_from_fahrenheit(temp_c):
    """ Converts temperature from degrees F to degrees C

    :param temp_c: float with the temperature in degrees Celsius
    :return: float of temperature in degrees Fahrenheit
    """
    temp_f = temp_c * 1.8 + 32

    return temp_f
```
A test could be written in the file `test_temp_conversion.py` as follows.
```
# test_temp_conversion.py

def test_celsius_from_fahrenheit():
    from temp_conversion import celsius_from_fahrenheit

    result = celsius_from_fahrenheit(20)
    assert result == 68

```
By best practice, the file that contains unit tests has the same name as the 
module with the functions to test, but with `test_` added to the front.

And, the test function name has the same name as the function to be tested, 
again with `test_` appended on the front.

The test module needs to `import` the function to be tested `from` the module
in which it resides.  This gives the test module access to the code to be
tested.

The function to be tested is then called with a particular input and stored in 
a variable called `result`, although the name of this variable can be anything.
The result of the function is then compared with the known actual answer using
the `assert` command.  The `assert` command essentially returns whether the 
given statement is True or False.  `pytest` then reports that result.

The tests are run by the following command:  
`pytest -v` where the `-v` option turns on verbose commenting and is optional.
The results of the above code is as follows:
```
============================= test session starts =============================
platform win32 -- Python 3.7.0, pytest-3.8.2, py-1.6.0, pluggy-0.7.1 -- D:\Miniconda3\envs\mdpEnv\python.exe
cachedir: .pytest_cache
rootdir: D:\ClassRepos\BME547\Lectures\unit_testing_code, inifile:
plugins: pep8-1.0.6, cov-2.6.0
collected 1 item

test_temp_conversion.py::test_celsius_from_fahrenheit PASSED             [100%]

========================== 1 passed in 0.02 seconds ===========================
```

The test passed.  Let's say there was an error in the code.  For example,
assume the temperature conversion was done by the following line of code:
`temp_f = temp_c * 1.8 + 32 + 3` where `+ 3` has been added to the conversion
in `celsius_from_fahrenheit`.  The results of the test would now look as
follows:
```
============================= test session starts =============================
platform win32 -- Python 3.7.0, pytest-3.8.2, py-1.6.0, pluggy-0.7.1 -- D:\Miniconda3\envs\mdpEnv\python.exe
cachedir: .pytest_cache
rootdir: D:\ClassRepos\BME547\Lectures\unit_testing_code, inifile:
plugins: pep8-1.0.6, cov-2.6.0
collected 1 item

test_temp_conversion.py::test_celsius_from_fahrenheit FAILED             [100%]

================================== FAILURES ===================================
________________________ test_celsius_from_fahrenheit _________________________

    def test_celsius_from_fahrenheit():
        from temp_conversion import celsius_from_fahrenheit

        result = celsius_from_fahrenheit(20)
>       assert result == 68
E       assert 71.0 == 68

test_temp_conversion.py:5: AssertionError
========================== 1 failed in 0.07 seconds ===========================
```
We see that the test failed and the output shows the result from the function
(`71`) and the expected result (`68`).

Test functions can also be aids to understand how a function is called.  Take 
the following function also in the file `temp_conversion.py`.
```
# temp_conversion.py

def detect_fever(temp_list_f):
    """ Return the highest temperature and whether it is a fever

    :param temp_list_f: list of temperatures in degrees Fahrenheit
    :return: tuple with highest temperature and boolean for fever
    """
    largest_temp = max(temp_list_f)
    fever_threshold = 100.5
    if largest_temp > fever_threshold:
        fever = True
    else:
        fever = False
        
    return largest_temp, fever
```
It has this corresponding test:
```
# test_temp_conversion.py

def test_detect_fever():
    from temp_conversion import detect_fever

    input_temps = [98, 99, 100, 102, 95]
    (max_temp, is_fever) = detect_fever(input_temps)

    assert max_temp == 102
```
We can see from this test that detect_fever is expected to return two values. 


`pytest -v` now returns the following output:
```
============================= test session starts =============================
platform win32 -- Python 3.7.0, pytest-3.8.2, py-1.6.0, pluggy-0.7.1 -- D:\Miniconda3\envs\mdpEnv\python.exe
cachedir: .pytest_cache
rootdir: D:\ClassRepos\BME547\Lectures\unit_testing_code, inifile:
plugins: pep8-1.0.6, cov-2.6.0
collected 2 items

test_temp_conversion.py::test_celsius_from_fahrenheit PASSED             [ 50%]
test_temp_conversion.py::test_detect_fever PASSED                        [100%]

========================== 2 passed in 0.14 seconds ===========================
```

We can see that both tests now passed.  

### PEP-8 Check
Many software companies have style guides for coding, mandating how code is 
formatted visually, variables are named, functions named, etc.
[PEP-8](https://www.python.org/dev/peps/pep-0008/) is the Style Guide for 
Python Code.  We will be using this style guide in this class.  `pytest` has
the ability to check that code meets the PEP-8 style requirements.  Run `pytest`
as follows:  
`pytest -v --pep8`


