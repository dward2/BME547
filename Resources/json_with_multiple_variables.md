# Using JSON with multiple variables

### Dumping and loading a single python variable via JSON to/from a file
When we use the `json.dump(obj, out_file)` function, it encodes a single
variable (`obj`) into a JSON string and then writes that JSON string into
a file object found in the `out_file` variable.  Then, this JSON string can
be read in and decoded back to a Python variable using the 
`json.load(out_file)` command.  This is demonstrated in the [JSON lecture
notes](../Lectures/json.md).  

### Dumping/loading multile python variables via JSON in a single file

How do we save multiple Python variables as JSON strings in a single file?

We can use the `json.dump()` command multiple times to write multiple variables
to the same file:

```python
import json

def output_to_json(patient1, patient2):
    with open("patients.json", 'w') as out_file:
        json.dump(patient1, out_file)
        out_file.write("\n")
        json.dump(patient2, out_file)
```
The `out_file.write("\n")` line prints a line return character after the first
json output so that each variable will be on its own line.  

### `json.loads()`

Then, to read
the data back in, you need to use the `json.loads()` function instead of the
`json.load()` function.  `json.loads()` takes a string containing a JSON string 
as an argument rather than a file.  So, we read in each individual line from
the JSON file generated above and individually convert it into a Python 
variable.

```python
import json

def input_from_json():
     with open("patients.json", 'r') as in_file:
        in_line = in_file.readline()
        person1 = json.loads(in_line)
        in_line = in_file.readline()
        person2 = json.loads(in_line)
```
Each line of the file is read in as a string, and then this string is sent
through the `json.loads()` decoder to create a Python variable.

### `json.dumps()` vs. `json.dump()`

Note, the opposite of `json.loads()` is `json.dumps()`.  `json.dumps()` encodes
a variable into a JSON string and returns it as a string variable rather than
to a file.  The `output_to_json()` function above can be rewritten as follows:

```python
import json

def output_to_json_file(patient, patient2):
    with open("patients.json", 'w') as out_file:
        out_string = json.dumps(patient)
        out_file.write("{}\n".format(out_string))
        out_string = json.dumps(patient2)
        out_file.write("{}\n".format(out_string))
```
In this example, each Python variable is first converted into a JSON string
that is then written to the output file using the `.write()` function.

### Creating a single list from multiple variables to output

There is another option.  Rather than write each Python variable to its own
JSON string and save each JSON string in the file, you could combine the 
variables into a list and then write this single list to a single JSON 
string/file.

```python
import json

def output_to_json(patient1, patient2):
    db = [patient1, patient2]
    with open("patients.json", 'w') as out_file:
        json.dump(db, out_file)
```  

Then, you could then use `json.load()` to read in this list, and then parse through
the list to get the individual patients.