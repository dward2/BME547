# Running Python in Git Bash Folder in Windows 10

### Avoid the Problem:  Install Git and Python with the following instructions

The easiest way to make sure that you can run Python from the Git Bash window
is to carefully follow the installation instructions found on the 
[installation.md](../Resources/installations.md) page.
Install Git and Python as instructed, and you should be able to run Python 
from the Git Bash window.

### Solve the Problem
If for some reason you cannot run Python from Git Bash, go through the 
following steps:  

#### Check the Windows PATH variable

First, open a Windows Command Prompt (click on the Start icon and then type
`cmd`, or type Windows-R to open the Run window and type `cmd` and hit Ok).

Next, at the command prompt, type `path` and hit return.  The PATH
environmental variable should print out.  Scan through this and look for a
particular path that includes `Python`.  For example, look for a path similar
to `C:\Users\<username>\AppData\Local\Programs\Python\Python37-32\`.

If you see this path, skip to "Git Bash Python Alias" below. 
Otherwise, continue...

#### Find the Python Path
(Note: the following instructions are similar to those found at this web page, 
<https://projects.raspberrypi.org/en/projects/using-pip-on-windows/5> which
has some visuals that may help).

In the Windows search bar, type `python.exe` but do not hit return.  It should
find a python.exe file.  Right click on this file and choose "Open File 
Location" from the menu that appears.  A Windows Explorer window will open
that shows the path containing the `python.exe` executable file.  Click on 
the path bar at the top of the window and copy the path.  **NOTE**: if the 
path contains the words `Start menu`, you are probably looking at the shortcut
to Python.  In that case, right click on the file in the Window that has 
a name like `Python 3.7` and choose "Open File Location".  That should open
up another window that has the `python.exe` file.  Use that path.

#### Add Python Pad to Windows PATH environmental variable
Click on the start menu and type `environment` but do not hit return.  Windows
should return an option called "Edit environment variables for your account".
Select this option.  

A window called "System Properties" will open.  If not already selected, click
on the "Advanced" tab.  At the bottom of the window will be a button called
"Environment Variables...".  Click on this button.

A window called "Environment Variables" will open.  In the top portion of the
windows, there will be a section called "User variables for <username>" where
<username> will be your specific user name.  There should be a variable in 
this section called `Path`.  If not, click the "New..." button under this
section of the window and follow the "New" instructions below.  If there is 
a `Path` variable already, select it, press "Edit...", and follow the "Edit"
instruction below.

##### New
After clicking "New...", a window should open called "New User Variable".  In
the "Variable Name" box, type `Path`.  In the "Variable Value" box, enter
the python path you captured above, followed by a semicolor, and then the 
python path you captured above again followed by "\Scripts\".

For example, the input for Variable Value should look something like:
`C:\Users\<username>\AppData\Local\Programs\Python\Python37-32\;C:\Users\<username>\AppData\Local\Programs\Python\Python37-32\Scripts`

Skip to "Finish Editing Environemtnal Variables".
##### Edit
After clicking "Edit...", a window should open called "Edit environment 
variable".  Click on the "New" button on the right, and enter the python path
you captured above.  Then, click "New" again and enter the python path you 
captured above and add `\Scripts\`.  

##### Finish Editing Environmental Variables
Click on Ok to close out all windows.  if the command prompt window is still
open, close it and re-open it for the new path to take effect.

#### Git Bash Python Alias

Open a Git Bash window.  Type `python` at the prompt.  If it works, you are
finished.  If it doesn't work, go to the 
[installations.md](../Resources/installations.md) page and follow the 
instructions under "To use `python` from the GitBash command line, do the
following:".




 