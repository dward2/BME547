# Accessing Underlying `pymongo` functionality
`pymodm` uses the package `pymongo` to access MongoDB.  The info on this page
provides some informaiton on accessing some of the underlying functionality
of the `pymongo` package.  This information should be used very carefully
in that the developers of `pymodm` made the choice not to make this
functionality available.  So, its use may interfere with normal operation of
`pymodm`.  Use at your own risk.

## Dropping a Collection
A collection in MongoDB is a set of documents created by the same MongoModel 
class.  Assume you have already made a connection to MongoDB using the 
`pymodm.connect` command.  To delete a connection, use the following code:
```python
from pymodm import connection
db = connection._get_db()
db.drop_collection(<collection_name_string>)
```
where `<connection_name_string>` is a string containing the name of the
collection as shown in MongoDB.  It will generally be similar to the name of
the MongoModel class in python, but capitalization and spacing/underscores
are likely different.  So, verify the names in MongoDB.  Or, the following
code will get a list of the names of the various collections in your
database (again assuming a connection to MongoDB has already been made):
```python
from pymodm import connection
db = connection._get_db()
names = db.list_collection_names()
print(names)
```
