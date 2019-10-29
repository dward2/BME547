# Using SendGrid

SendGrid is a web service that provides an API for sending e-mails from your
own code.

## Set-up a SendGrid account and Generate an Access Key

* Visit <https://sendgrid.com/> and sign-up for the free plan.
* After signing-up, you will see an option for "Integrate using our Web API
or SMTP relay."  Click on the "Start" button next to that option.  If you
do not see this option, look for the "Setup Guide" in the lower right corner
of the dashboard or by clicking on your name in the upper left corner.
* On the next page, click the Choose button under the "Web API" option.
* On the next page, click the Choose button next to "Python".
* On the next page, in Step 2, type in a name in the "My First API Key Name"
field, and click the "Create Key" button.
* Save the key generated.

## Save the Access Key in your Environment Variables

### For Linux/MaxOS
There are two options.  The first option sets up a file that you would run each time
you start your linux session, sort of like a virtual environment, allowing you
to keep your customized environment variables specific to different projects. 
The second option modifies one of your log-in files to automatically set up the 
environment variable upon log-in.

#### Option 1  
Continue with step 3 of the instructions from the SendGrid setup
guide, duplicated here.  In the terminal, navigate to your project folder and 
then enter the following on the command line:
  * `echo "export SENDGRID_API_KEY='<your_API_key>'" > sendgrid.env` This will 
  create a file called "sendgrid.env". 
  * `echo "sendgrid.env" >> .gitignore` will create (or add to an existing)
  `.gitignore` file so that you do not accidentally upload your sendgrid API
  key to GitHub.
  * `source ./sendgrid.env` will add your SENDGRID_API_KEY to your environment
  variables, allowing your Python code to be able to access your SendGrid
  account.
  * Enter `env` on the command line and look for the `SENDGRID_API_KEY` value
  to confirm that everything worked.

NOTE:  You will need to enter the `source ./sendgrid.env` command each time
  you log in to your linux account as it is not currently saved in your 
  permanent variables.  
  
#### Option 2  
* Edit the `.bashrc` file found in your `~` directory.
* At the very bottom,  add the line 
`export SENDGRID_API_KEY='<your_API_key>'`where `<your_API_key>` is the 
generated key from above.
* Save the file.
* Log off and log back on.
* Enter `env` on the command line and look for the `SENDGRID_API_KEY` value
to confirm that everything worked.

### For Windows 10
* Click on the start menu icon, and type "environ" into the search bar.  One
of the search results should be "Edit the system environment variables."
Choose this.
* A "System Properties" window should open.  It should be open to the 
"Advanced" tab.  If not, select that tab.  Click on the "Environment
Variables..." button.
* An "Environment Variables" window should open.  The upper half of this 
window is called "User Variables for username" where username will be your Windows
ID.  Click on the "New..." button in this section.
* A "New User Variable" window should open.  Enter `SENDGRID_API_KEY` for the
variable name.  Enter the generated key from above as the variable value.
Click "Ok" to close this window.
* Click "Ok" twice to close the "Environment Variables" window and the "System
Properties" window
* Reboot your computer for the change to take effect.

## Sending E-mail in Python
First, you will need to install the `sendgrid` package in the usual way for
your system.

Below is some sample Python code for using `sendgrid` version 6.
```
import os
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail

message = Mail(
    from_email='from_email@example.com',
    to_emails='to@example.com',
    subject='Sending with Twilio SendGrid is Fun',
    html_content='<strong>and easy to do anywhere, even with Python</strong>')
try:
    sg = SendGridAPIClient(os.environ.get('SENDGRID_API_KEY'))
    response = sg.send(message)
    print(response.status_code)
    print(response.body)
    print(response.headers)
except Exception as e:
    print(str(e))
```

For more information on using `sendgrid` in your Python code, visit 
<https://github.com/sendgrid/sendgrid-python>.


## Note
On April 3, 2019, the `sendgrid` python package for using SendGrid in Python
was updated from version 5.6 to 6.0.  This was a BREAKING CHANGE, meaning
that the functionality and syntax of various functions changed.  The
instructions above are written for version 6.0.  If you need to use a previous
version of `sendgrid`, ensure that you are installing the correct sendgrid 
package by specifying the version number in your `requirements.txt` file as so:
` sendgrid==5.6.0`.  Also, the syntax for use will be different than that 
above.
