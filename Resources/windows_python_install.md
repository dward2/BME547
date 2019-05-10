Notes from my install of Python in Windows

Some basic info:
<https://docs.python.org/3/using/windows.html#other-platforms>

First, downloaded the Python installer from:
https://www.python.org/downloads/release/python-373/

Ran installer, turned off option to install for all users, and picked option
to add PATH.

After install, clicked button to extent MAX_Path length

venv seems to be preinstalled, so I didn't need to specifically add it.

Created a venv by `python -m venv venv`

Then, activated by `venv\Scripts\activate`

Then, did `pip install numpy`

`deactivate` turned off virtual environment

Now, on my virtual machine, git seems to be working from command prompt.
That may be because I had previous added Git Bash.

Using this Python 3.7, I was able to run my Heart_Monitor2 code, which used 
numpy, scipy, and matplot lib.

My Heart_Rate_Sentinel_Server also ran.  So `flask` works.

`tkinter` also seemed to work fine.

And, the virtual environment that was created by PyCharm was able to be
activate from the command line as above.


