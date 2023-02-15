# Text Input from a File

It is a common occurrence that data from a text file needs to be read into a
program in order to process the data in the file.  In Python, this can be
accomplished by using the `open` and `input` functions.

## `open()`
Let's assume we have a text file called `input_data.txt` that contains a series 
of numbers, each on their own line.

Example:
```
15
2.342342
19.2
5
25
```

The `open()` function is used to open the text file and return a file
object that is stored in a variable and used to access the contents of the 
file.

```python
in_file = open("input_data.txt", "r")
```
`open()` requires at least one parameter which is a string that gives the path
and filename to the file to be opened.  When used with only the single 
parameter, the default file mode of "Read-Only" is used.  Often, a second
parameter is given to set the file mode.  This second parameter is a single
character.  In the example above, `"r"` is given to explicitly set the file
mode to read-only.  Other common file modes:
* `"w"`: write mode, will create a file if one does not exist or overwrite the
         file if it does exist
* `"a"`: append mode, will create a file if one does not exist or append to an
         file if it does exist
* `"b"`: binary mode, only used when reading in a binary file such as an image


The default path for the file is the 
current directory from which the module was executed.  Relative paths from this
directory can be given.  For example, if
your repository has a subfolder called "data" in which your files are located,
you would reference those files as such:
```python
in_file = open("data/input_data.txt", "r")
```
It is also possible to reference a file using an absolute path:
```python
in_file = open("D:/BME547/Classwork/data/input_data.txt", "r")
```
However, this approach is discouraged because this code will only work on the
specific machine that contains this path or requires other users to create
a similar folder.  Relative paths are greatly preferred.  

## `readline()`
Once the file is opened, we can access the data.  Often, when reading text
files, we are interested in reading the file line by line. The file object has
a `readline()` method that will return a single line from the file.  The returned
string will contain a `"\n"` character at the end, which is the new line
character, unless the inputted line is the last line of the file and there is
no new line after it.  Each call to `readline()` will return the next line in 
the file.

The following example reads in the first three lines of an input file.
```python
in_file = open("input_data.txt", "r")
for i in range(3):
    line = in_file.readline()
    print(line)

```
Output:
```
15

2.342342

19.2

```
Notice in the output that there is a blank line between each line printed.  That is
because there is the new line character read in from the input file by the
`readline()` method and then the new line character created by the `print()`
function.  You could remove these extra lines in one of two ways:
* Use the `.strip("\n")` function to remove the new line character from the
  inputted line, such as  
  ```python
  line = in_file.readline().strip("\n")
  ```
* Modify the `print()` function with the `end=""` parameter to tell the print
  statement to end with nothing instead of the new line character such as
  ```python
  print(line, end="")
  ```


If you would like to iterate over all of the lines in a file, you can do so by
simply iterating over the file object, and each iteration returns a line from
the file.
```python
in_file = open("input_data.txt", "r")
for line in in_file:
    print(line, end="")
```

## `readlines()`
Sometimes, you may prefer to read all of the text lines in at once into a
single list that you can then access multiple times, manipulate the data, 
and/or send this data to another function.  This can be done with the 
`readlines()` method.
```python
in_file = open("input_file.txt", "r")
all_lines = in_file.readlines()
for line in all_lines:
    print(line, end="")
print("Increment data")
for line in all_lines:
    number = float(line)
    number += 1
    print(number)
```
Output:
```
15
2.342342
19.2
5
25
Increment data
16.0
3.342342
20.2
6.0
26.0
```

## `close()`
Finally, it important to close any input file you are using when finished with
it in order to free up system resources.  This is done with the `close()`
method of the file object.
```python
in_file.close()
```
Another common method for dealing with closing files is to do all of the file
access within a `with` statement.  
```python
with open("input_file.txt", "r") as in_file:
    for line in in_file:
        print(line, end="")
```
Once the `with` code block is finished, the file is automatically closed.


More information on doing file I/O in Python can be found at:
* <https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files>
* <https://docs.python.org/3/library/functions.html#open>

## Passing File Object as Parameter
The file object created by the `open()` function can be passed as a parameter
to allow for multiple functions to use it for reading in data.  For example,
assume you have an input file such as follows:
```
Patient ID = 145
Test Results = 20, 13, 9
```

You could write modular functions to read-in and analyze each line.

```python
def process_patient_id_line(file_object):
    line = file_object.readline()
    data = line.split("=")
    patient_id = int(data[1])
    return patient_id

def process_patient_tests_line(file_object):
    line = file_object.readline()
    data = line.split("=")
    tests = data[1].split(",")
    test_results = [int(i) for i in tests]
    return test_results


in_file = open("input_file.txt", "r")
patient_id = process_patient_id_line(in_file)
test_list = process_patient_tests_line(in_file)
```

### Unit testing this case
These modular functions can still be tested using pytest.  Create a test 
input file that has the data that the function to be tested is expecting to 
receive.  Then, in the test function, open that file and send the file object
to the function to be tested.

Example:
```python
def test_process_patient_id_line():
    from mysandbox import process_patient_id_line
    in_file = open("input_test_file.txt", "r")
    answer = process_patient_id_line(in_file)
    expected = 145
    assert answer == expected
```