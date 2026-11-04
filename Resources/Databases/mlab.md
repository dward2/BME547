# Provision Free MongoDB Database on mongoDB.com

MongoDB Atlas is an online service that lets you quickly spin up a MongoDB 
database server on a virtual machine that they own. Once you've spun up a MongoDB 
instance on their virtual machine, you can connect to and interact with it 
from Python code and use it so save and retrieve data. 

## Setup
Note: The MongoDB website interface for new accounts changes frequently.
The instructions here are accurate as of March 2026, but may change.  So, if
your experience varies from below, modify as needed.

1. Visit [mongodb.com](https://www.mongodb.com/). Click on "Get Started".      
   ![Get Started](./images/get_started.jpg)
2. On the Sign up page (shown below), enter your e-mail, first and last names, 
   and select a 
   password.  Agree to the terms and conditions by selecting the checkbox.   
    ![Sign up info](./images/sign_up_info.jpg)  
    Then, click "Create your Atlas account".  
   (NOTE:  your e-mail and password
   you enter here are for accessing the MongoDB website.  It is not what you
   will use for your Python code to access the database, that information is
   created below.)
3. You will then receive an email from MongoDB to verify your e-mail.  Click
   "Verify Email" in that email.  It will open up a new webpage indicating that
   your email has been verified.  Click on the "Continue" button.
4. On the "Enable Multi-factor Authentication for your account" page (see 
   below), set up
   your preferred MFA method.  
    ![MFA](./images/MFA.jpg)  
5. A page will display saying "Let's build something great" and you
   will have the choice to create a free starter database.  If you like,
   you can change the name of the from Cluster0 to something else.  You can
   also uncheck the "Load a sample dataset" button if you like.  Then, click on
   "Set it up for me".
    ![database_choice](./images/free_database_choice.jpg)
6. A "Connect to <cluster_name>" window will open.  <cluster_name> will either
   be "Cluster0" or the name you entered for the cluster.  An initial database
   user is automatically created and the username and password are displayed.
   Copy this information into a safe location.  
   ![connect](./images/connect_1.jpg)
7. Click on "Choose a connection method".  The following will appear:    
        ![connect](./images/connect_2.jpg)
8. Under "Connect to your application", click on "Drivers and Client Librarier".
   This will appear:    
     ![connect](./images/connect_3.jpg)
   1. Under "Language", select "Python".
   2. Under "Client Library", select "PyMongo (Synchronous)".  
   3. Make sure that the "Configure connection string" button is selected.
   4. Copy the string found under "Use This Connection String In Your 
      Application".  This string is the uri that will be used in your code to
      connect to MongoDB.  You will need to replace `<db_username>` and 
      `<db_password>` with the username and password recorded from step 6 above.
   5. Click the green "Done" button.
9. Next, we need to add IP addresses allowed to access the database.
   1. On the left hand menu, under the "Security" section, click on 
      "Database & Network Access".
   1. Under "Network Access" in the left-hand menu, click on "IP Access List".  
        ![ip access list](./images/ip_access_list_menu.jpg)
   2. On the IP Access List page, Click on the green "+ Add IP Address" 
      button.  
        ![add ip address](./images/add_ip_address.jpg)
   3. In the "Add IP Access List Entry" box, in the "Access List Entry" text
      box, enter `0.0.0.0`.  
        ![enter ip](./images/add_ip_entry.jpg)
   4. Click "Confirm".

Cool, you're done setting up the database server!

Once you have data added to your database server, you can see it through the 
MongoDB website.  Under "Database" on the left-hand side, select "Data 
Explorer".  
    ![data explorer menu](./images/data_explorer_menu.jpg)

You can then navigate through your cluster to see your different databases 
and collections.

### Adding Database User       
If, for some reason, you would like an additional set of credentials to use in 
your code for accessing your MongoDB, you can
    click on the "Database & Network Access" option on the left-hand menu.  
        ![database access](./images/database_network_menu.jpg)  
On the "Database Users" page, you can click on the green "+ Add New Database 
    User" button  
         ![add_user](./images/add_database_user.jpg)  
    Then follow these steps

1. Under "Authentication Method", select "Password".
2. Enter a username (this user name will be used by your Python program
   to access the database and is different from the user name/email you
   use to access the MongoDB website)
3. Select a password.  Copy this password down somewhere safe as you will
         not see it again.
4. Under "Built-in Role", select "Atlas admin".
5. Click the green "Add User" button.
 
### Getting Connection String
 
If you did not get the connection string in the instructions above, follow 
these steps:
1. Under "Database" in the left-hand list, click on "Clusters".
2. Click on the "Connect" button.
3. Click "Drivers and Client Libraries" under the "Connect to your application" 
   heading.
4. Under "Language", select "Python" and under "Client Library" select "PyMongo 
   (Synchronous)" for the version.
5. Copy the string that is shown under "Use This Connection String In Your
   Application".  Replace the `<db_username>` and 
  `<db_password>` placeholders with the name and password you created above.
6. Save this string for use in class and projects.  

### Granting Another User Access to Your MongoDB Web Interface
When working as a team, you will likely be using just a single MongoDB
database.  As the entire team may need to see that database on the MongoDB
website, the owner of the database in use can grant other MongoDB accounts
access to the web interface of the database.

1. Log into your MongoDB Atlas database server account.
2. Click on "Project Identity & Access" under "Security" on the left-hand 
   side.
3. Click on the "Invite to Project" button.  
4. Enter the e-mail address associated with the MongoDB account you wish to
   provide access.  
5. Select the appropriate permission level to give.
6. Click the "Invite to Project" button.
