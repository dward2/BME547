# Testing Fixtures

When doing unit testing, it may be necessary to set up some data structures
that must be sent to the unit function for testing.  And, it may be necessary
for this data structure to be used by many different tests.  Rather than
writing the code to set up this data for each and every test, it would be
easier to capture that set-up code once and re-use it.

Pytest contains functionality to do that and it is called a fixture.  A fixture
is created by placing a decorator before a specific function that will then
save that function for future use.

As an example, let's say we have two functions that we want to test called
`first_item` and `last_item`.  These two functions both take in a list of
words that must be in all capital letters.  And, let's say that the list of 
words we want to use for the test are found in an external text file and are
mixed case.  Our test function will need to load in the words from the text
file and convert them into all capital letters before being able to test
the function.

The test code for `first_item` might look like this:
```
def test_first_item():
    from array_work import first_item

    in_file = open("array_data.txt", "r")
    lines = in_file.readlines()
    in_file.close()
    in_list = []
    for line in lines:
        in_list.append(line.upper())

    answer = first_item(in_list)
    expected = "APPLES\n"
    assert answer == expected
```
After the from/import statement, we have 6 lines of code to set up the correct
list for the test, then we call the function to be tested and use an `assert`
to see if we got the right answer.

Then, we will need to write a test for the `1ast_item` function.  It would
look like this:
```
def test_last_item():
    from array_work import last_item

    in_file = open("array_data.txt", "r")
    lines = in_file.readlines()
    in_file.close()
    in_list = []
    for line in lines:
        in_list.append(line.upper())

    answer = last_item(in_list)
    expected = "FROGS\n"
    assert answer == expected
```
Notice that we have had to include the same six lines for inputting and
preparing the data for both test functions.  If we have only two tests, maybe
this isn't so bad.  But, if you have hundreds of tests, it becomes cumbersome
to continually duplicate these lines.  And, if you ever needed to make a change
in one of those six lines, you would have to go back to every test function
and make the change.  

Here is where a fixture comes in.  We can capture these reused lines in a
fixture that can be referenced by each test function that needs it.

```
import pytest

@pytest.fixture
def load_array():
    in_file = open("array_data.txt", "r")
    lines = in_file.readlines()
    in_file.close()
    in_list = []
    for line in lines:
        in_list.append(line.upper())
    return in_list


def test_first_item_two(load_array):
    from array_work import first_item

    answer = first_item(load_array)
    expected = "APPLES\n"
    assert answer == expected


def test_last_item_two(load_array):
    from array_work import last_item

    answer = last_item(load_array)
    expected = "FROGS\n"
    assert answer == expected

```
First, we must `import pytest` so that the python interpreter will recognize
the `@pytest.fixture` code.  Then, we "decorate" the function that contains
the code we want to use multiple times with `@pytest.fixture`.  This tells
pytest to save this code for future use.

Then, when there is a test function that needs the data that is set up by
the fixture, we pass that function name as a parameter to the test_function,
as seen by the line `def test_first_item_two(load_array):`.

### Order of Fixtures and Test Functions
It is important that any text fixture is defined ahead of the test that will
be using it.  If all of your tests are in a single file, just make sure that
the fixtures are defined above the tests.  However, if you have multiple
test files, it may not be certain that a test fixture defined in one file will
be defined for tests in another file need to use that fixture.

In this case, all fixtures should be defined in a special file called 
`conftest.py`.  When `pytest` is run, it will look for the `conftest.py` file
first and run any code in it.  So, if all test fixtures are stored in this
file, they will be guaranteed to be available for any other test file.  
`conftest.py` is named as such because it is the "conf"iguration file for 
py"test".  


## Predefined Test Fixtures
Pytest has some predefined test fixtures that can be used.  
### Temporary directories for testing input/output
If your code is doing input/output, you may want to avoid cluttering your 
repository with lots of input/output files for testing.  Pytest provides
fixtures for creating temporary file locations unique to the test instance.

The `tmpdir` fixture provides a path to a temporary directory to use during
testing.  An example:
```
def test_create_file(tmpdir):
    from json_out import export_json
    import json

    outfile = tmpdir.join("testfile.txt")
    mydic = {"First": "Test",
             "Second": 15,
             "Third": True,
             "Fourth": "One more"}
    export_json(mydic, outfile)
    infile = open(outfile, "r")
    newdic = json.load(infile)
    assert newdic == mydic
```
 
For more info:
https://docs.pytest.org/en/latest/tmpdir.html#


## Additional References for Testing Fixtures
* https://docs.pytest.org/en/latest/fixture.html
* http://pythontesting.net/framework/pytest/pytest-fixtures/

Example: https://github.com/mlp6/fem/blob/master/tests/conftest.py

## Other Type of Software Testing
1. Integration Testing (how do all of the units work together)
2. System Testing (does the whole package work)
3. User Testing (alpha / beta; what breaks)
Nice article: https://www.business2community.com/tech-gadgets/4-types-software-testing-use-01704964#DEr51MdDRpj4zXyg.97

## Additional Resources on Unit Testing
* http://pythontesting.net/start-here/
* https://docs.pytest.org/en/latest/
