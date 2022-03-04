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
* Ideal unit:
  + Takes inputs
  + Does calculations on those inputs
  + Returns output
* Any function with a user interface only sends and receives data, but does
not do any calculation.  Any calculation should be in a separate unit function
that can be tested.
* If you function does too much and requires a divergent set of tests, then
that function should be broken up into smaller functions.

### Testing Frameworks
* `unittest`
  + Ubiquitous, used by many languages
* `pytest`
  + Easy to use and install with `pip` and `conda`.
  + Has Python specific features
* `nose2`
  + Extension of `unittest`
  
## Installing `Pytest`
Pytest is not a default package in Python, so must be installed in a virtual environment.

* `requirements.txt`
  + `pytest`
  + `pytest-pycodestyle`
  
### conda version
_If you don't have `conda`, please skip this section._

From the command line:
```
conda install pytest
conda install -c conda-forge pytest-pycodestyle
``` 
Or, in an `environment.yml file`:
```
name: myvenv
channels:
  - default
  - conda-forge
dependencies:
  - pytest
  - pytest-pycodestyle
```
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
platform win32 -- Python 3.8.3, pytest-6.0.1, py-1.9.0, pluggy-0.13.1 -- d:\classrepos\testwork\venv\scripts\python.exe
cachedir: .pytest_cache
rootdir: D:\ClassRepos\testwork
plugins: pycodestyle-2.2.0
collecting ... collected 1 item

test_temp_conversion.py::test_celsius_from_fahrenheit PASSED             [100%]

============================== 1 passed in 0.03s ==============================
```

The test passed.  Let's say there was an error in the code.  For example,
assume the temperature conversion was done by the following line of code:
`temp_f = temp_c * 1.8 + 32 + 3` where `+ 3` has been added to the conversion
in `celsius_from_fahrenheit`.  The results of the test would now look as
follows:
```
============================= test session starts =============================
platform win32 -- Python 3.8.3, pytest-6.0.1, py-1.9.0, pluggy-0.13.1 -- d:\classrepos\testwork\venv\scripts\python.exe
cachedir: .pytest_cache
rootdir: D:\ClassRepos\testwork
plugins: pycodestyle-2.2.0
collecting ... collected 1 item

test_temp_conversion.py::test_celsius_from_fahrenheit FAILED             [100%]

================================== FAILURES ===================================
________________________ test_celsius_from_fahrenheit _________________________

    def test_celsius_from_fahrenheit():
        from temp_conversion import celsius_from_fahrenheit

        result = celsius_from_fahrenheit(20)
>       assert result == 68
E       assert 71.0 == 68
E         +71.0
E         -68

test_temp_conversion.py:7: AssertionError
=========================== short test summary info ===========================
FAILED test_temp_conversion.py::test_celsius_from_fahrenheit - assert 71.0 == 68
============================== 1 failed in 0.11s ==============================
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
platform win32 -- Python 3.8.3, pytest-6.0.1, py-1.9.0, pluggy-0.13.1 -- d:\classrepos\testwork\venv\scripts\python.exe
cachedir: .pytest_cache
rootdir: D:\ClassRepos\testwork
plugins: pycodestyle-2.2.0
collecting ... collected 2 items

test_temp_conversion.py::test_celsius_from_fahrenheit PASSED             [ 50%]
test_temp_conversion.py::test_detect_fever PASSED                        [100%]

============================== 2 passed in 0.04s ==============================
```

We can see that both tests now passed.  

### PEP-8 Check
Many software companies have style guides for coding, mandating how code is 
formatted visually, variables are named, functions named, etc.
[PEP-8](https://www.python.org/dev/peps/pep-0008/) is the Style Guide for 
Python Code.  (A more friendly presentation of the PEP-8 Style guide can be
found [here](https://pep8.org/).  We will be using this style guide in this 
class.  `pytest` has the ability to check that code meets the PEP-8 style 
requirements.  Run `pytest` as follows:  
`pytest -v --pycodestyle`

Typical output now looks like this:

```
============================= test session starts =============================
platform win32 -- Python 3.8.3, pytest-6.0.1, py-1.9.0, pluggy-0.13.1 -- d:\classrepos\testwork\venv\scripts\python.exe
cachedir: .pytest_cache
rootdir: D:\ClassRepos\testwork
plugins: pycodestyle-2.2.0
collecting ... collected 4 items

temp_conversion.py::PYCODESTYLE PASSED                                   [ 25%]
test_temp_conversion.py::PYCODESTYLE PASSED                              [ 50%]
test_temp_conversion.py::test_celsius_from_fahrenheit PASSED             [ 75%]
test_temp_conversion.py::test_detect_fever PASSED                        [100%]

============================== 4 passed in 0.14s ==============================

```
The PEP-8 checks are shown in the list first, and indicates whether they
passed or failed.  Above is a passing example.  Below is an example of when 
the code failed.  Note that the output give a description of where the PEP-8
violation is and what the error was.

```
============================= test session starts =============================
platform win32 -- Python 3.8.3, pytest-6.0.1, py-1.9.0, pluggy-0.13.1 -- d:\classrepos\testwork\venv\scripts\python.exe
cachedir: .pytest_cache
rootdir: D:\ClassRepos\testwork
plugins: pycodestyle-2.2.0
collecting ... collected 4 items

temp_conversion.py::PYCODESTYLE FAILED                                   [ 25%]
test_temp_conversion.py::PYCODESTYLE FAILED                              [ 50%]
test_temp_conversion.py::test_celsius_from_fahrenheit PASSED             [ 75%]

test_temp_conversion.py::test_detect_fever PASSED                        [100%]

================================== FAILURES ===================================
______________________________ pycodestyle-check ______________________________
D:\ClassRepos\testwork\temp_conversion.py:26:1: W293 blank line contains whitespace

______________________________ pycodestyle-check ______________________________
D:\ClassRepos\testwork\test_temp_conversion.py:17:27: W292 no newline at end of file

=========================== short test summary info ===========================
FAILED temp_conversion.py::PYCODESTYLE
FAILED test_temp_conversion.py::PYCODESTYLE
========================= 2 failed, 2 passed in 0.07s =========================

```
Let's parse one of the failures:
```
______________________________ pycodestyle-check ______________________________
D:\ClassRepos\testwork\temp_conversion.py:26:1: W293 blank line contains whitespace
```
It starts by telling us which file the error is in (`temp_conversion.py`).  It 
then tells us the location of the error.  `26:1` means line 26 column 1.  It
then gives us the PEP-8 error number (`W293`) and what the error is (`blank 
line contains whitespace`).  When you fix these errors, you can run `pytest`
again and see if they pass.

Note, you may sometimes see the following output:
```
temp_conversion.py::PYCODESTYLE SKIPPED                                  [ 25%]
``` 
Rather than saying `PASSED` or `FAILED`, it says `SKIPPED`.  `pytest` uses a 
cache to save information from run to run.  It uses this cache to determine if
a file has changed since the last `pytest` run.  In order to save run time,
PYCODESTYLE will not check a file if it has previously passed and has not
changed since.  To force the PEP-8 check on files, use the `--cache-clear` flag
as so:
```
pytest -v --pycodestyle --cache-clear
```


## Exercise
__Goal__:  Develop a Python function that:
* receives as parameters two tuples, `(x1, y1), (x2, y2)`, that represent two
(x, y) coordinates on a plane,
* receives a parameter, `x`, that is a new value on the x-coordinate of the 
above plane,
* and returns a value `y` that is on the line created by the first two points.

__Steps__: 
* Write a unit test for this function before you code the function itself.
* Add instructor as a collaborator to your repository and create an issue that
links to this unit test.  Add the instructor as an assignee.
* Develop the function.
* If  you find that your function has multiple steps that can be broken down
into smaller functions, do so, and then write a test for the smaller functions
as well.
* Make sure your function passes your unit tests.
* Open a second issue that links to the completed function and add instructor
as an assignee.

__Additional Work__:
* Develop a function that takes `(x1, y1), (x2, y2)` and a third point 
`(x3, y3)` and returns True if the third point is on the line defined by the
first two points.  Otherwise, it returns False.
* Write unit tests that test this function for both True and False results.
