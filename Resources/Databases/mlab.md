# Provision Free MongoDB Database on mongoDB.com

MongoDB Atlas is an online service that lets you quickly spin up a MongoDB 
database on a virtual machine that they own. Once you've spun up a database 
instance on their virtual machine, you can connect to and interact with it 
using database connection URL, as discussed in class. Remember that a database 
is a program, just like any other program you write. By knowing the connection 
URL, your Python Flask program knows where the database is running and can 
communicate with the database to save entries or retrieve entries as needed. 

## Setup
Note: The MongoDB Atlas website interface for new accounts changes frequently.
The instructions here are accurate as of March 2022, but may change.  So, if
your experience varies from below, modify as needed.

1. [Sign up](https://www.mongodb.com/cloud/atlas) for a free account at 
mongoDB.  Click on "Try Free".
2. Enter your e-mail, first and last names, and select a password.  Agree to 
   the terms and conditions by selecting the check box.  Then, click "Join
   now with no obligation".
3. You will then receive an email from MongoDB to verify your e-mail.  Click
   "Verify Email" in that email.
4. Click "Continue" on the webpage that opens.
5. Answer the questions on the "Welcome to Atlas!" page.  I answered:
   1. Learn MongoDB
   2. New to MongoDB
   3. Python
   4. Not sure (for what kind of data)
   5. Not sure (for application architectural models)   
6. Click "Finish".   
7. On the "Deploy your database" page:
   1. Select the "M0 FREE" button.
   2. Choose any provider under Provider (I use aws).
   3. Change the cluster name, or accept the default.
   4. Click the green "Create" button.
   5. You may need to complete a puzzle to prove you are not a robot.
8. You should be taken to a "Security Quickstart" page.
9. Under "How would you like to authenticate your connection":
    1. Select "Username and Password"
    2. Enter a username (this user name will be used by your Python program
       to access the database and is different than the user name/email you
       use to access the MongoDB website)
    3. Select a password.  Copy this password down somewhere safe as you will
         not see it again
    4. Click "Create User"
15. Under "Where would you like to connect from?"
    1. Choose "My Local Environment"
16. Click on "Finish and Close" to finish on the "Security Quickstart" page.
17. Click on "Go to Database" on the pop-up window.
18. After some period of time, your cluster will be ready.
19. Add IP addresses allowed to access the database on the "IP Whitelist".  
   a. Click on "Network Access" in the left-hand list.  
   b. Make sure the "IP Access List" tab is selected.  Click on "Add IP Address".  
   c. Click on "Allow Access From Anywhere" in the window that pops up.  Click 
    "Confirm".
20. Get connection information to your database.  
   a. Click on "Database" in the left-hand list.  
   b. Click on the "Connect" button.   
   c. Click "Drivers" under the "Connect to your application" heading  
   d. Under "1. Select your driver and version", select "Python" for the Driver 
      and "3.6 or later" for the version (this will ensure it will work on
      your virtual machine which will have Python 3.10 installed)
   e. Ignore section 2
   f. Copy the string that is shown under "3. Add your connection string into 
   your application code" section.  Make sure the slider "view full code
   sample" is slid to the left (off).  
   f. Save this string for use in class and projects.  

Cool, you're done setting up the database! Now, when you're using this in your 
flask programs with `pymodm`, your first couple lines will look something like:
```py
from pymodm import connect
connect("mongodb+srv://<username>:<password>@bme547-nlfrn.mongodb.net/<dbname>?retryWrites=true&w=majority")
```
The string in the `connect` command above is the one you copied in step 20e 
above, except `<username>` should have already been replaced by the username 
you created in step 9 above.  You will manually need to replace `<password>` 
with the password you created in step 11c above.  `<dbname>` can be replaced
by any name of your choosing.  (Note, the connect string you copy from the
MongoDB website will not have `<dbname>` in it.  It will show the `/` and `?`
adjacent.  You need to add something in that space.)

Finally, you will need to add one more package to your `requirements.txt` file:
`dnspython` in order to access the database with the string above.

Now, you can access the database use code similar to [here](mongo_db_example.py).

Once you have data added to your database, you can see it through the 
MongoDB website.  Select "Databases" from the left-hand side and click on 
"Browse Collections" if you see that button, or select the "Collections" tab
at the top, depending on your current screen.  You will then see a list of
the `dbnames` that you created in your connect strings, and within each
database, you will see any MongoModel `class` you created in your code.  


### Adding another a database user.    
   a. Click on "Database Access" in the left-hand list.  
   b. Make sure the "Database Users" sub-tab is selected.  Then click "Add New 
   Database User" button.  
   c. Select the Password Authentication Method  
   d. Complete the username field, select a password (__remember this__), choose 
   "Read and write to any database", and click "Add User".
