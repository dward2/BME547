# Provision Free MongoDB Database on mongoDB.com

MongoDB Atlas is an online service that lets you quickly spin up a MongoDB 
database on a virtual machine that they own. Once you've spun up a database 
instance on their virtual machine, you can connect to and interact with it 
using database connection URL, as discussed in class. Remember that a database 
is a program, just like any other program you write. By knowing the connection 
URL, your Python Flask program knows where the database is running and can 
communicate with the database to save entries or retrieve entries as needed. 

## Setup
1. [Sign up](https://www.mongodb.com/cloud/atlas) for a free account at 
mongoDB.  Click on "Get started now".
2. Complete the form to create an account and click "Continue".
3. Enter your first and last name and agree to the terms and conditions by
   selecting the check box.  Then, click "Create account".
4. You will then receive an email from MongoDB to verify your e-mail.  Click
   "Verify Email" in that email.
5. Click "Continue" on the webpage that opens.
6. Answer the questions on the "Welcome to Atlas!" page.  I answered:
   - Learn MongoDB
   - Internet of Things
   - Python
7. Click "Finish".   
8. On the "Deploy a cloud database" page, select the Free "Shared" option and
   click on the "Create" button for that option.
9. Under "Cloud Provider and Region", select any cloud provider (I used AWS)
and choose a region close to you (I selected N. Virginia).
10. Ignore "Cluster Tier" or "Additional Settings" unless you want to spend
some money to customize your account.  The base settings should be fine.
11. Name your cluster anything you would like (perhaps "bme547")
12. Click "Create Cluster" at the bottom of the page.
13. A visual check may appear to help make sure you are not a robot.  Complete
   it and click "Verify".
14. After some period of time, your cluster will be ready.
15. Create a database user.    
   a. Click on "Database Access" in the left-hand list.  
   b. Make sure the "Database Users" sub-tab is selected.  Then click "Add New 
   Database User" button.  
   c. Select the Password Authentication Method  
   d. Complete the username field, select a password (__remember this__), choose 
   "Read and write to any database", and click "Add User".
16. Add IP addresses allowed to access the database on the "IP Whitelist".  
   a. Click on "Network Access" in the left-hand list.  
   b. Make sure the "IP Access List" tab is selected.  Click on "Add IP Address".  
   c. Select "Allow Access From Anywhere" in the window that pops up.  Click 
    "Confirm".
17. Get connection information to your database.  
   a. Click on "Databases" in the left-hand list.  
   b. Click on the "Connect" button.   
   c. Click on the "Connect Your Application" option.  
   d. Under "1. Select your driver and version", select "Python" for the Driver and 
   "3.6 or later" for the version.  
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
The string in the `connect` command above is the one you copied in step 17e 
above, except `<username>` should have already been replaced by the username 
you created in step 11 above.  You will manually need to replace `<password>` 
with the password you created in step 11c above.  `<dbname>` can be replaced
by any name of your choosing.

Finally, you will need to add one more package to your `requirements.txt` file:
`dnspython` in order to access the database with the string above.

Now, you can access the database use code similar to [here](mongo_db_example.py).

Once you have data added to your database, you can see it through the 
MongoDB website.  Select "Databases" from the left-hand side and click on 
"Browse Collections" if you see that button, or select the "Collections" tab
at the top, depending on your current screen.  You will then see a list of
the `dbnames` that you created in your connect strings, and within each
database, you will see any MongoModel `class` you created in your code.  

