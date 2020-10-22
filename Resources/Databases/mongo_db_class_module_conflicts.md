# Mongo_DB / PyMODM Caution:  Using the same class in different modules
There may be times where you need to access the MongoDB database in
multiple modules.  You only need to connect to the MongoDB using the 
`connect` command once in your code, before you need to access the database.  
You do not need to have that command in each module.
    
However, there are precautions you must take in regards to how you define
the MongoModel class that contains your data structure.

In the example code found [here](./mongo_db_example.py), when you look to see the entries of your database 
through the MongoDB website, you see the following:
```
_id: "david.a.ward@duke.edu"
first_name: "David"
last_name: "Ward"
age: 45
_cls: "__main__.User"
``` 
Note that, for the class name (`_cls`), `pymodm` and MongoDB have appended the 
name of the module in which the class was defined.  Since the class was defined 
in the module that was called from the command line by 
`python module_dp_example.py`,  the module name appended is `__main__` since 
the class was defined in the `__main__` module.  

There may be times where you need to access the class you define for your
MongoDB database in multiple modules.  For example, assume the following
module is written:

```
# database.py

from pymodm import connect, MongoModel, fields

class PhoneNumber(MongoModel):
    name = fields.CharField(primary_key=True)
    phone_number = fields.CharField()

connect("mongodb+srv://<username>:<password>@bme547-nlfrn.mongodb.net/test?retryWrites=true&w=majority")

u = PhoneNumber(name="Library", phone_number="888-867-5309")
u.save()

import another_module
another_module.add_another_number("Gym", "888-888-8888")

for user in PhoneNumber.objects.raw({}):
    print("{}: {}".format(user.name, user.phone_number))
```
This module defines a class called `PhoneNumber` to store names and phone 
numbers in a MongoDB.  When run, the code first establishes
a connection to the database.  It then adds a name and phone number to the 
database.  Then, after importing `another_module`, it calls a function in
`another_module` to add another phone number.  Finally, the code retrieves
the database entries and prints them out.

The code for `another_module` is :

```
# another_module.py

from pymodm import MongoModel, fields

class PhoneNumber(MongoModel):
    name = fields.CharField(primary_key=True)
    phone_number = fields.CharField()

def add_another_number(name_arg, phone_number_arg):
    u = PhoneNumber(name=name_arg, phone_number=phone_number_arg)
    u.save()
    return
```
The PhoneNumber class is redefined in this module so that it is available to
the function in this module for database access.

When the program is run by typing `python database.py` at the command line,
here is the output:
```
Library: 888-867-5309
```
The program found the first number added in the `database` module, but
not the second number added in the `another_module` module.  

If we look in the MongoDB through the website,
 we see that both phone number additions to the database was successful:
 ```
 _id: "Library"
phone_number: "888-867-5309"
_cls: "__main__.PhoneNumber"

_id: "Gym"
phone_number: "888-888-8888"
_cls: "another_module.PhoneNumber"
 ```  
But, notice how the class names are different. That is because the classes
were defined in two different modules, and so have two different names.  So,
when the `database` module used its own version of the class to access the
database, it only found the first number that
had the class name with `__main__` appended to it since `database` is the 
`__main__module`.

The reverse would have been true also.  If code in the `another_module` module
accessed the data base using the `PhoneNumber` class defined in `another_module`,
it would have only found the "Gym" entry which was created using the 
`another_module.PhoneNumber` class.

Unfortunately, just importing the definition created in the `database` module
will not solve the problem either, and can create other problems.
For example, if `another_module` is re-written as 
follows:
```
# another_module.py

from database import PhoneNumber

def add_another_number(name_arg, phone_number_arg):
    u = PhoneNumber(name=name_arg, phone_number=phone_number_arg)
    u.save()
    return
```
the database entry stored here will have the `_cls` name of 
`database.PhoneNumber` and still won't be found when trying to be found from
the main module that will be looking for `__main__.PhoneNumber`.  In addition,
if you are not careful with importing a module that is already being imported,
you can get what I call "looping imports".  When `database` imports the 
`another_module` module, the first thing `another_module` does is try to 
import `database`.  Depending on what you are importing and whether there are
global variables and function calls, this can lead to errors.  

The solution is:  
__Do not cut and paste the code that defines the class from one
module to the other.  Also, do not define a class in any module that might
be run from the command line.  Instead, define a separate module that only 
contains the
MongoDB class information and import this into any module that needs to
access the database.__  

For the example above, create a module called `mongo_db_class`.

```
#mongo_db_class.py

from pymodm import MongoModel, fields

class PhoneNumber(MongoModel):
    name = fields.CharField(primary_key=True)
    phone_number = fields.CharField()
```

Then, this class can be imported into both of the modules that need accesss
to it.  In each module, `pymodm` and MongoDB will then define the class as
`mongo_db_class.PhoneNumber` and there will be no ambiguity when accessed from
either module.