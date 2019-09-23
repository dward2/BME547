# JSON
JSON (JavaScript Object Notation) (https://json.org) is a standard data 
information exchange format used in many applications.

Python has a standard library called `json` that provides basic functions for
encoding and decoding Python variables into and out of JSON format.

The Python documentation for `json` can be found at
https://docs.python.org/3/library/json.html.

Simple Example of saving variable to a file using JSON format:
```python
import json

my_dictionary = {
                "Name": "Firstname Lastname", 
                "School": "Duke University"
                 }

out_file = open("filename.json", "w")
json.dump(my_dictionary, out_file)
out_file.close()
```
The code above will create a file named "filename.json" that contains the 
`my_dictionary` information in JSON format.

Simple Example of importing a JSON format file into a variable:
```python
import json

filename = "filename.json"
in_file = open(filename, "r")
new_variable = json.load(in_file)
in_file.close()
print(new_variable)
```
The code above will give the following output:
```
{'Name': 'Firstname Lastname', 'School': 'Duke University'}
```

More information on doing file I/O in Python can be found at:
* https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files
* https://docs.python.org/3/library/functions.html#open

## In Class Exercise
* To your Cholesterol Calculator, add an option to enter patient data,
including name and age.  Put that information into a dictionary.
* Create a `json` output file that contains this information.
* If time, integrate the ability to enter an HDL or LDL test result, have it
diagnosed, and saved with the patient's data.