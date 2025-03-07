# Provision Free MongoDB Database on mongoDB.com

MongoDB Atlas is an online service that lets you quickly spin up a MongoDB 
database server on a virtual machine that they own. Once you've spun up a MongoDB 
instance on their virtual machine, you can connect to and interact with it 
from Python code and use it so save and retrieve data. 

## Setup
Note: The MongoDB Atlas website interface for new accounts changes frequently.
The instructions here are accurate as of March 2022, but may change.  So, if
your experience varies from below, modify as needed.

1. [Sign up](https://www.mongodb.com/cloud/atlas) for a free account at 
mongoDB.  Click on "Try Free" or "Get Started".
2. Enter your e-mail, first and last names, and select a password.  Agree to 
   the terms and conditions by selecting the check box.  Then, click "Create
   your Atlas account". 
3. You will then receive an email from MongoDB to verify your e-mail.  Click
   "Verify Email" in that email.
4. Click "Continue" on the webpage that opens.
5. Answer the questions on the "Welcome to Atlas!" page.  These questions may
   have changed since, but here is what I answered in case they are the same:
   1. Learn MongoDB
   2. New to MongoDB
   3. Python
   4. Not sure (for what kind of data)
   5. Not sure (for application architectural models)   
6. Click "Finish".   
7. On the "Deploy your cluster" page:
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
10. Under "Where would you like to connect from?"
    1. Choose "My Local Environment"
11. Click on "Finish and Close" to finish on the "Security Quickstart" page.
12. Click on "Go to Database" on the pop-up window.  Note: the button might be
    labelled "Go to Overview" instead.
13. After some period of time, your cluster will be ready.
14. Add IP addresses allowed to access the database on the "IP Whitelist".  
   a. Click on "Network Access" in the left-hand list.  
   b. Make sure the "IP Access List" tab is selected.  Click on "Add IP Address".  
   c. Click on "Allow Access From Anywhere" in the window that pops up.  Click 
    "Confirm".
15. Get connection information to your database.  
   a. Click on "Database" in the left-hand list.  
   b. Click on the "Connect" button.   
   c. Click "Drivers" under the "Connect to your application" heading.  
   d. Under "1. Select your driver and version", select "Python" for the Driver 
      and "3.11 or later" for the version.  
   e. Make note of the `pip` `pymongo` installation command under section "2. Install your driver"  
   f. Copy the string that is shown under "3. Add your connection string into 
   your application code" section.  Make sure the slider "view full code
   sample" is slid to the left (off).  Replace the `<db_username>` and 
  `<db_password>` placeholders with the name and password from step 9 above.    
   g. Save this string for use in class and projects.  

Cool, you're done setting up the database server! 

Once you have data added to your database server, you can see it through the 
MongoDB website.  Select "Databases" from the left-hand side and click on 
"Browse Collections" if you see that button, or select the "Collections" tab
at the top, depending on your current screen.  You will then see a list of
your databases, and within each database, you will the collections you created 
in your code.  


### Adding another a database user
   a. Click on "Database Access" in the left-hand list.  
   b. Make sure the "Database Users" sub-tab is selected.  Then click "Add New 
   Database User" button.  
   c. Select the Password Authentication Method  
   d. Complete the username field, select a password (__remember this__), choose 
   "Read and write to any database", and click "Add User".  
   e. Make a new copy of your connect string with this new username and password


### Granting Another User Access to Your MongoDB Web Interface
When working as a team, you will likely be using just a single MongoDB
database.  As the entire team may need to see that database on the MongoDB
website, the owner of the database in use can grant other MongoDB accounts
access to the web interface of the database.

1. Log into your MongoDB Atlas database server account.
2. Make sure you are viewing the database you want to give access to.
3. Click on "Access Manager" at the top of the page and select "Project Access"
   from the dropdown.
4. Click on the "Invite to Project" button.  
5. Enter the e-mail address associated with the MongoDB account you wish to
   provide access.  
6. Select the appropriate permission level to give.
7. Click the "Invite to Project" button.
