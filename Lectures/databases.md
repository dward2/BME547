# Databases
Storing things in a program is a complicated proposition when you have large
amounts of data or complicated data structures.

Based on what we know about Python to-date, how would we save information in our
program and have it accessible for later use if we need to restart the program?

The simplest approach would be to have a list in memory, and then save that
list to a text or CSV file.  Each time we need the data, we would then need
to read data from the file into the list and then iterate through this list
to find the correct piece of data.  Unfortunately, if we have lots of data,
it can take a long time to iterate through all of this data.

We can speed up the search through the data by using a dictionary.  But, the
dictionary is an even larger data structure (requires more memory) and would 
need to be converted to a JSON string for saving in a file.

These approaches are slow and memory intensive (requires reading all of the 
data and search through all the data each time you want only a piece).

Here is where a database comes in.  A database is a program that is 
responsible for managing data storage and retrieval for you.  A good database
uses advanced and optimized algorithms for storing, finding, and retrieving data from an
external source.  This reduced memory requirements for your application and 
improves efficiency.  

## Types of Databases
Databases can be split into two "families":  Relational (SQL) and 
Non-Relational (noSQL).

### Relational (SQL) Databases
Relational databases, often called SQL databases, have a pre-defined structure 
(called a schema)
that allows for "relationships" to be drawn between different sets of data.
The data tables and variable types in these data tables are pre-defined, which
can improve the efficiency and size of the database.  The
data tables consist of rows (records) and columns (fields).  
SQL (Structured Query Language) is used to create, access, and manipulate the
data in the database.  Most databases have type checking to ensure that data
being entered into the database matches the requirements.

### Non-Relational (NoSQL) Databases
Non-relational databases do not have a pre-defined schema or data model.
Entries are considered "objects" or "documents" that may or may not have
similar data formats.  This may be advantageous if different database entries
may need different types of data included with it.  Data within these objects 
are often structured as "key:
value" pairs.  Since there is not a pre-defined format for this type of 
database, there is not automatic data-type checking done before insertion
into the database.

## MongoDB
For this class, we will be using a non-relational database called MongoDB.
It is easy to set-up and use.  A database is just like any other program that
runs on a computer.  This program could be running on your own computer, on a
virtual machine, or a cloud service.  Our Python code accesses the database
by making requests to the database API.  


We will be accessing the MongoDB database from our Python code using a package 
called [PyMODM](https://pymodm.readthedocs.io/en/latest/) which gives us access 
to the MongoDB API, but also enforces type-checking which is very helpful from 
a programming perspective.  

The basics of accessing a MongoDB database from Python is demonstrated in
this [Jupyter Notebook](../Resources/Databases/mongo_example.ipynb).

A code example can be found [here](../Resources/Databases/mongo_db_example.py).

### Creating a Mongo DB
You have many options for setting up your own MongoDB instance.
* Set-up a free cloud service at <https://www.mongodb.com/cloud/atlas>.
Complete instructions for doing so can be found [here](../Resources/Databases/mlab.md).
* You can install and run MongoDB on your own computer (locally or on your 
virtual machine).  See the community edition [here](https://docs.mongodb.com/manual/installation/#tutorials).
* You can install and run MongoDB easily using Docker.  


### PyMODM Syntax

#### Import PyMODM package
`from pymodm import connect, MongoModel, fields`

#### Connect to MongoDB database
```
connect("mongodb+srv://<username>:<password>@<yourclustername>-<server>.mongodb.net/<folder>?retryWrites=true&w=majority")
```  
If using MongoDB Atlas, you should obtain the string to use in the `connect`
function from the MongoDB website.  Refer to the set-up instructions found 
[here](../Resources/Databases/mlab.md) for how to get the connect string.  It 
should be very similar to what is above.
`<server>` will be provided in the string you obtain from the website.  You
will need to replace `<username>`, `<password>`, and `<yourclustername>` with
the appropriate information you entered doing the MongoDB set-up online.
Finally, replace `<folder>` with any string.  This will be the "collection" 
name in MongoDB.

__Note__: There have been instances where the MongoDB website provides a
connect string that does not provide the `<folder>` placeholder.  For example:
`mongodb+srv://<username>:<password>@bme547.ba348.mongodb.net/?retryWrites=true&w=majority`
In this case, you will need to remember to insert a collection/folder name
between `mongodb.net/` and `?retryWrites`.

:eyes: If using macOS and you receive an SSL or certificate error when trying
to use `pymodm`, visit the [installations_mac.md](../Resources/installations_mac.md#ssl-or-certificate-errors)
 page for a potential fix.

:eyes: On Windows or macOS, if you get an error similar to 
`pymongo.errors.ServerSelectionTimeoutError:...[SSL:CERTIFICATE_VERIFY_ERROR]...`,
import the `ssl` module and then add `ssl_cert_reqs=ssl.CERT_NONE`to the 
`connect` command as so:

```python
import ssl

connect("<YourConnectString", ssl_cert_reqs=ssl.CERT_NONE)
```

#### Create Schema / Data structure
```
class User(MongoModel):
    email = fields.EmailField(primary_key=True)
    first_name = fields.CharField()
    last_name = fields.CharField()
    age = fields.IntegerField()
```
The class name (`User` in the above example) can be defined by the user.  It
must include `(MongoModel)` after the name so that it inherits the `MongoModel`
class.  The number of fields and field names are up to the user.  

Commonly used fields are:
* `CharField`
* `IntegerField`
* `BooleanField`
* `DateTimeField`
* `EmailField`
* `FileField`
* `ImageField`
* `FloatField`
* `DictField`
* `ListField`

Information on these fields and other fields can be found in the PyMODM API: 
<https://pymodm.readthedocs.io/en/latest/api/index.html#model-fields>

Be aware of possible class/module conflicts as described 
[here](../Resources/Databases/mongo_db_class_module_conflicts.md).

#### Create a Database Item
`u = User(email="suyash@suyashkumar.com", first_name="Suyash", last_name="Kumar", age="1000")`  
`u` can be any variable name and `User` is whatever the name of the class as
defined above.

#### Save Item to Database
`u.save()`

#### Query Database:  Return all items
`results = User.objects.raw({})`  
`results` is any variable name and `User` is the name of the class defined as 
above.  `results` will contain a QuerySet class, which can be iterated over to
get the results as such:
```
for item in results:
    print(item.email)
``` 

#### Query Database:  Return Items Based on Specific Search
`results = User.objects.raw({"first_name": "Mark"})` if searching on 
non-primary key  
`results = User.objects.raw({"_id": "suyash@suyashkumar.com"})` if searching
on primary key

Comparison operators can be found at 
<https://docs.mongodb.com/manual/reference/operator/query-comparison/>.  Example:  
`results = User.objects.raw({"age": {"$gte": 1000}})`
 
### Checking for whether a primary key is in database
If you do a search for a value in the primary key field that does not exist
in the database, `pymodm` will generate an error.  So, here is some sample
code for how you can check to see if an entry exists in the database.  

```python
from pymodm import errors as pymodm_errors

try:
    db_item = User.objects.raw({"_id": <item_to_search>}).first()
except pymodm_errors.DoesNotExist:
    return False
return True
```
This code snippet will return False if the `<item_to_search>` value is not
found in the primary key field of the database.  It will return `True` if it
is found.

### Deleting a database entry
If you need to delete a specific entry from your database in your Python code,
first, query the object to find it and save it in a variable.  Then, use the
`.delete()` method.  Example:
```python
x = Patient.objects.raw({"_id": "999"}).first()
x.delete()
```