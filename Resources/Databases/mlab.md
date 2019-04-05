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
2. Click on "Build my first cluster" or "Build A Cluster" depending on what
screen you reach.  
3. Select any cloud provider
4. Choose a region close to Duke
5. Ignore "Cluster Tier" or "Additional Settings" unless you want to spend
some money to customize your account.  The base settings should be fine.
5. Name your cluster anything you would like (perhaps "bme547")
6. Click "Create Cluster" at the bottom of the page.
7. After some period of time, your cluster will be ready.  
8.  Next, create a "user" through which you will be able to access
the database through your code.   Click on the "Security" tab underneath the
"Clusters" heading.  Make sure the "MongoDB Users" sub-tab is selected.
Then click "Add New User" button to the right.  Complete the username field,
select a password (remember this), choose "Read and write to any database", 
and click "Add User".
9. Next, select the "IP Whitelist" sub-tab.  Click on "Add IP Address" and
then select "Allow Access From Anywhere" in the window that pops up.  Click 
"Confirm".  It may take a few minutes for this step to be confirmed.
10.  Go back to the "Overview" tab.  You will see a button called "Connect".
Click on that.  Click on the "Connect Your Application" option.  Under 
"1. Choose your driver version" select "Python" for the Driver and "3.6 or later"
for the version (or an earlier version if you are using that).  Copy the string
that is shown in the "Add your connection string into your application code"
and the Connection String Only tab.  

Cool, you're done setting up the database! Now, when you're using this in your 
flask programs with `pymodm`, your first couple lines will look something like:
```py
from pymodm import connect
connect("mongodb+srv://<username>:<password>@bme547-nlfrn.mongodb.net/test?retryWrites=true")
```
The string in the `connect` command above is the one you copied in step 11 above, 
except `<username>` should have already been replaced by the username you 
created in step 8 above.  You will manually need to replace `<password>` with
the password you created in step 11 above.

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
There may be times where you need to access the class you define for your
MongoDB database in multiple modules.  For example, you may have a module
called `data_create.py` that uses a class `MyClass` for putting records into
the MongoDB database.  Then, you might have a separate module called 
`read_data.py` that also uses `MyClass` to access data from the MongoDB
database.  

__Do not cut and paste the code that defines the class from one
module to the other.__  MongoDB will append the module name to the front
of the class (ex. `data_create.MyClass`) when storing it in the database.
If you then try and retrieve it from a different module where the class is 
also defined, it will look for the data with a different class name
(ex. `read_data.MyClass`).  It will look like there is no data available.

Instead, define the class in one module, and import it into others that need
to use it.  In the example above, `MyClass` could be defined in the 
`data_create.py` module.  Then, in the `read_data.py` module, it could be
imported using `from data_create import MyClass`.  Now, the `read_data.py`
module will be looking for `data_create.MyClass` in the database.