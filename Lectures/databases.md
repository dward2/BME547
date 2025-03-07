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
called [PyMongo](https://www.mongodb.com/docs/languages/python/pymongo-driver/current/) 
which gives us access to the MongoDB API.  

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


## PyMongo Syntax

### Install PyMongo in Virtual Environment
```
pip install pymongo
pip install dnspython
```

### Import MongoClient from PyMongo package
`from mongo import MongoClient`

### Connect to MongoDB database server
```
uri = "<connect_string>"
client = MongoClient(uri)
```  
If using MongoDB Atlas, you should obtain the `<connect_string>` to use above 
from the MongoDB website.  Refer to the set-up instructions found 
[here](../Resources/Databases/mlab.md) for how to get the connect string.  
Make sure to replace the `<db_username>` and `<db_password` placeholders with
the appropriate information created during the MongoDB set-up online.

### Connect to a Database
You can have many different databases in your MongoDB account.  Connect to 
a database as follows:
```python
database = client["Class_Database"]
```
If the database named does not exist, MongoDB will create one when a new 
document is added to it.

### Create a Collection
A collection is a set of documents within your database.  You would have 
a different collection for each type of document you want to store.  For 
example, you might have a collection of users, a collection of equipment, a 
collection of locations, etc.
```python
user_collection = database["users"] 
```

### Create a Document
A document in MongoDB is a set of key:value pairs.  In Python, this is a 
standard dictionary type. The keys are the name of each item of the document 
and the value is a Python data type.  This document dictionary is then 
created in the database u sing the `.insert_one()` method of the collection.
```python
user_document = {"email": "suyash@suyashkumar.com", "first_name": "Suyash", 
                 "last_name": "Kumar", "age": 1000}
user_collection.insert_one(user_document)
```
While this example only has the `int` and `str` data type as values, most 
Python data types, including lists, dictionary, datetime, etc., can be used 
as values.

#### Unique IDs
Each document in MongoDB is given a unique ID that differentiates it from 
every other document.  If one is not specified in the `insert_one` call, 
MongoDB will assign it one.  The unique id is stored in the `_id` key of the
document.  MongoDB enforces that no two documents can share the same `_id`.

To specify a unique id, simply include the `_id` key in the document 
dictionary.  The example above is rewritten below to use the email as the 
unique id:
```python
user_document = {"_id": "suyash@suyashkumar.com", "first_name": "Suyash", 
                 "last_name": "Kumar", "age": 1000}
user_collection.insert_one(user_document)
```


### Retrieve a Document
#### All Documents
```python
all_users_cursor = user_collection.find()
```
`user_collection.find()` returns a "cursor" to the found documents in the 
collection.  You use the cursor to move through the documents by iterating 
over it in a `for` loop to get each document individually as such: 
```python
for item in all_users_cursor:
    print("Email:  {}".format(item["_id"]))
``` 
If you would prefer not to have to move through the results using a cursor, 
you can create an actual list of results in a Python variable as follows:
```python
all_users = list(all_users_cursor)
```
But, be careful as if your search has found many records in the database, 
it could possibly exceed memory limits for your application.  

#### Documents Based on Specific Search
A search query can be added to the `.find` method to return only documents 
matching the given criteria.
```python
results = user_collection.find({"first_name": "Mark"})  
```

Comparison operators can be found at 
<https://docs.mongodb.com/manual/reference/operator/query-comparison/>.  Example:  
```python
results = user_collection.find({"age": {"$gte": 1000}})
``` 

#### A Single Document
If you want to return only a single document (i.e., you know there is only 
one document that meets your search request or your only care about the 
first one), you can get the first document itself using the `.find_one()` 
method as follows:
```python
document = user_collection.find_one({"email": "mark@test.com"})
```
This is particularly effective if you do your search on the unique id of which
there is only one, as discussed below.

### Update a Document
The easiest way to update a document in MongoDB is to follow these steps:
1. Retrieve the document to be updated from the collection
2. Update the document dictionary with the desired changes
3. Replace this document dictionary into the collection using the unique id.
Example:
```python
# Retrieve document
mark_user = user_collection.find_one({"first_name": "Mark"})

# Update the contents of the document
mark_user["age"] += 20

# Replace with the updated document using its unique identifier
user_collection.replace_one({"_id": mark_user["_id"]}, mark_user)
```

### Deleting a Document
To delete a single document from a collection based on a query:
```python
user_collection.delete_one({"first_name": "Mark"})
```
To delete all documents in a collection:
```python
user_collection.delete_many({})
```
The empty query dictionary `{}` is required.

## Documentation
PyMongo documentation can be found at <https://www.mongodb.com/docs/languages/python/pymongo-driver/current/>