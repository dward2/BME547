# Databases
Storing things in a program is a complicated proposition when you have large
amounts of data or complicated data structures.

Based on what we know about Python, how would we save information in our
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
uses advanced algorithms for storing, finding, and retrieving data from an
external source.  This reduced memory requirements for your application and 
improves efficiency.  

## Types of Databases
Databases can be split into two "families":  Relational (SQL) and 
Non-Relational

### Relational (SQL) Databases
Relational databases, often called SQL databases, have a pre-defined structure 
(called a schema)
that allows for "relationships" to be drawn between different sets of data.
The data tables and variable types in these data tables are pre-defined, which
can improve the efficiency and storage of the database.  The
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


We will be accessing the MongoDB database from 
our Python code using a package called `pymodm` which gives us access to the
MongoDB API, but also enforces type-checking which is very helpful from a 
programming perspective.  

The basics of accessing a MongoDB database from Python is demonstrated in
this [Jupyter Notebook](../Resources/Databases/mongo_example.ipynb).

### Creating a Mongo DB
You have many options for setting up your own MongoDB instance.
* Set-up a free could service at <https://www.mongodb.com/cloud/atlas>.
Complete instructions for doing so can be found [here](../Resources/Databases/mlab.md).
* You can install and run MongoDB on your own computer (locally or on your 
virtual machine).  See the community edition [here](https://docs.mongodb.com/manual/installation/#tutorials)
* You can install and run MongoDB easily using Docker.  More information to come.

### Add More
Basic commands in pymodm
The types of fields you set up.
Look at how code would actually be set up 
 


