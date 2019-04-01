# Provision Free MongoDB Database on mlab

mLab is a online service that lets you quickly spin up a MongoDB database on a virtual machine that they own. Once you've spun up a database instance on their virtual machine, you can connect to and interact with it using database connection URL, as discussed in class. Remember that a database is a program, just like any other program you write. By knowing the connection URL, your Python Flask program knows where the database is running and can communicate with the database to save entries or retreive entries as needed. 

## Setup
1. [Sign up](https://mlab.com/signup/) for a free account at mlab. 
2. From your home screen click "create new" next to mongodb deployments
3. Select any cloud provider, and then select the free "sandbox" plan for plan type, then hit continue in the lower right hand corner.
4. Choose a region close to Duke on the next screen
5. Name your database anything you would like (perhaps "bme547")
6. Hit submit order and your free mongodb database should be created.
7. Click on your database name in the table under "MongoDB deployments"
8. Users tab and then click "add database user" button on the right hand side. We are creating a "user" though which we will be accessing the database in our flask program. Name the user whatever you would like, but do not use a personal password for your password (we are not too worried about the security of this database...you can use something like "GODUKE10", but don't use a personal password that you use for another site).

Cool, you're done setting up the database! Now, when you're using this in your flask programs with `pymodm`, your first couple lines will look something like:
```py
from pymodm import connect
connect("mongodb://MYUSERNAME:MYPASSWORD@ds157383.mlab.com:57383/bme590")
```

You should be using the URL format they give you at the top of your databases screen.
