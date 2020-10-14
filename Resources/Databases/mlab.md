# Provision Free MongoDB Database on mongoDB.com

MongoDB Atlas (previously mlab.com) is an online service that lets you quickly 
spin up a MongoDB 
database on a virtual machine that they own. Once you've spun up a database 
instance on their virtual machine, you can connect to and interact with it 
using database connection URL, as discussed in class. Remember that a database 
is a program, just like any other program you write. By knowing the connection 
URL, your Python Flask program knows where the database is running and can 
communicate with the database to save entries or retrieve entries as needed. 

## Setup
1. [Sign up](https://www.mongodb.com/cloud/atlas) for a free account at 
mongoDB.  Click on "Start free".
2. Complete the form to create an account and click "Continue".
3. Create an organization name and a project name.  You can use the defaults
   or come up with your own.
   Choose Python as your preferred language.  Click "Continue".
4. Click on the "Create a cluster" button in the "Shared Clusters" option. 
   This is the free version.
5. Select any cloud provider.
6. Choose a region close to Duke or your current location.
7. Ignore "Cluster Tier" or "Additional Settings" unless you want to spend
some money to customize your account.  The base settings should be fine.
8. Name your cluster anything you would like (perhaps "bme547")
9. Click "Create Cluster" at the bottom of the page.
10. After some period of time, your cluster will be ready.
11. Create a database user.    
   a. Click on "Database Access" in the left-hand list.  
   b. Make sure the "Database Users" sub-tab is selected.  Then click "Add New 
   Database User" button.  
   c. Select the Password Authentication Method  
   d. Complete the username field, select a password (remember this), choose 
   "Read and write to any database", and click "Add User".
12. Add IP addresses allowed to access the database on the "IP Whitelist".  
   a. Click on "Network Access" in the left-hand list.  
   b. Make sure the "IP Access List" tab is selected.  Click on "Add IP Address".  
   c. Select "Allow Access From Anywhere" in the window that pops up.  Click 
    "Confirm".  It may take a few minutes for this step to be confirmed.
13. Get connection information to your database.  
   a. If not already there, click on "Clusters" in the left-hand list.  
   b. Click on the "Connect" button.   
   c. Click on the "Connect Your Application" option.  
   d. Under "1. Select your driver and version", select "Python" for the Driver and 
   "3.6 or later" for the version (or an earlier version if you are using 
   that).  
   e. Copy the string that is shown under "2. Add your connection string into 
   your application code" section.  Make sure the checkbox labelled "Include
   full driver code example" is unchecked.  
   f. Save this string for use in class and projects.  

Cool, you're done setting up the database! Now, when you're using this in your 
flask programs with `pymodm`, your first couple lines will look something like:
```py
from pymodm import connect
connect("mongodb+srv://<username>:<password>@bme547-nlfrn.mongodb.net/<dbname>?retryWrites=true&w=majority")
```
The string in the `connect` command above is the one you copied in step 13e 
above, except `<username>` should have already been replaced by the username 
you created in step 11 above.  You will manually need to replace `<password>` 
with the password you created in step 11c above.  `<dbname>` can be replaced
by any name of your choosing.

Finally, you will need to add one more package to your `requirements.txt` file:
`dnspython` in order to access the database with the string above.

Now, you can access the database use code similar to [here](mongo_db_example.py).

Once you have data added to your database, you can see it through the 
MongoDB website.  Go to the "Collections" area by either clicking on a button
called "Collections" or  choosing the "Collections" tab, depending on what
screen you are starting from.  You will then see a collection with the same
name as the `class` you created in your code.  In the example case above, it
will be `user`.  You can then see the contents of this database.

