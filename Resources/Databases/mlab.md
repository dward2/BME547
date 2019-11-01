# Provision Free MongoDB Database on mongoDB.com

MongoDB Atlas (previously mlab.com) is an online service that lets you quickly 
spin up a MongoDB 
database on a virtual machine that they own. Once you've spun up a database 
instance on their virtual machine, you can connect to and interact with it 
using database connection URL, as discussed in class. Remember that a database 
is a program, just like any other program you write. By knowing the connection 
URL, your Python Flask program knows where the database is running and can 
communicate with the database to save entries or retreive entries as needed. 

## Setup
1. [Sign up](https://www.mongodb.com/cloud/atlas) for a free account at 
mongoDB.
2. Click on the Free Starter Cluster option.
3. Select any cloud provider
4. Choose a region close to Duke
5. Ignore "Cluster Tier" or "Additional Settings" unless you want to spend
some money to customize your account.  The base settings should be fine.
6. Name your cluster anything you would like (perhaps "bme547")
7. Click "Create Cluster" at the bottom of the page.
8. After some period of time, your cluster will be ready.
9. Follow the "Get Started" tasks by creating a database user.    
   a. Click on "Database Access" under "Security" on the left-hand list.  
   b. Make sure the "MongoDB Users" sub-tab is selected.  Then click "Add New 
   User" button to the right.  
   c. Complete the username field, select a password (remember this), choose 
   "Read and write to any database", and click "Add User".
10. Follow the next "Get Started" topic by adding to the "IP Whitelist".  
   a. Click on "Network Access" under "Security" on the left-hand list.  
   b. Make sure the "IP Whitelist" tab is selected.  Click on "Add IP Address".  
   c. Select "Allow Access From Anywhere" in the window that pops up.  Click 
    "Confirm".  It may take a few minutes for this step to be confirmed.
11. Skip the "Load Sample Data" step of the "Get Started" tasks, unless you
want to play around with some data.
12. Finish the "Get Started" tasks by connecting to your database.  
   a. If not already there, click on "Clusters" under "Atlas" on the left-hand
   list.  
   b. Click on the "Connect" button.   
   c. Click on the "Connect Your Application" option.  
   d. Under "1. Choose your driver version" select "Python" for the Driver and 
   "3.6 or later" for the version (or an earlier version if you are using 
   that).  
   e. Copy the string that is shown under "2. Add your connection string into 
   your application code" section in the Connection String Only tab.  

Cool, you're done setting up the database! Now, when you're using this in your 
flask programs with `pymodm`, your first couple lines will look something like:
```py
from pymodm import connect
connect("mongodb+srv://<username>:<password>@bme547-nlfrn.mongodb.net/test?retryWrites=true&w=majority")
```
The string in the `connect` command above is the one you copied in step 12e 
above, except `<username>` should have already been replaced by the username 
you created in step 8 above.  You will manually need to replace `<password>` 
with the password you created in step 9c above.

Finally, you will need to add one more package to your `requirements.txt` file:
`dnspython` in order to access the database with the string above.

Now, you can access the database use code similar to [here](mongo_db_example.py).

Once you have data added to your database, you can see it through the 
MongoDB website.  Go to the "Collections" area by either clicking on a button
called "Collections" or  choosing the "Collections" tab, depending on what
screen you are starting from.  You will then see a collection with the same
name as the `class` you created in your code.  In the example case above, it
will be `user`.  You can then see the contents of this database.

## Caution:  Using the same class in different modules
There may be times where you need to access the MongoDB database in
multiple modules.  You only need to connect to the MongoDB using the 
`connect` command once in your code, before you need to access the database.  
You do not need to have that command in each module.
    
However, there are precautions you must take in regards to how you define
the MongoModel class that contains your data structure.

In the example code above, when you look to see the entries of your database 
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
can also cause problems.  For example, if `another_module` is re-written as 
follows:
```
# another_module.py

from database import PhoneNumber

def add_another_number(name_arg, phone_number_arg):
    u = PhoneNumber(name=name_arg, phone_number=phone_number_arg)
    u.save()
    return
```
this leads to what I call "looping imports".  When `database` imports the 
`another_module` module, the first thing `another_module` does is try to 
import `database` during this import of `database`, `database` tries to 
import `another_module` again, which will lead to an error.  

The solution is:  
__Do not cut and paste the code that defines the class from one
module to the other.  Define a separate module that only contains the
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