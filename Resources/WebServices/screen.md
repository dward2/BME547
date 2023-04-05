# Screen

`screen` is a linux program that allows you to have multiple virtual screens or 
windows open within the same session.

## Install Screen
Check to see if it is already installed by typing
```
screen --version
```

If you don't get a response with the version number, or you get an error,
install it by typing
```
sudo apt install screen
```

## Overview
`screen` has sessions and screens.  When you start screen for the first time
by just typing `screen`, you are making a new session.  If you want to
start a new session with a specific name, you start it with the 
`-S <session_name>` argument.

Within each session, you can have multiple screens.  The instructions below
will assume that you make a new session for each server or program you want
to run.

## Using Screen
Start a new session:  `screen`

Start a new session with a given name:  `screen -S <session_name>`

List of commands:  `ctrl-a ?`

To disconnect (detach) from the current session:  `ctrl-a d`  

To restart (reattach) an existing detached session:  `screen -r <session_name>`

To stop and delete a session, reattach that session using
`screen -r <session_name>`, and then typing `ctrl-a` followed by `:` then 
`quit`


## Keeping a server running while logging off from virtual machine
1. Start a new session:  `screen -S my_server`
2. Navigate to the folder containing your server repository
3. Activate the virtual environment for your server/repository.  Example:
   `source myvenv/bin/activate`
4. Start your server code.  Example:  `python my_server.py`
5. You will not have a command line prompt as your server code is running in
   this session.  Detach this session by typing `ctrl-a d`
6. You can verify that your server session is still running by entering
   `screen -ls` and you will see your detached session.
7. You may now safely log off your virtual machine

When you log back on, you can seen that your screen session is still 
"detached" by typing `screen -ls`.  To reattach to your screens, 
type `screen -r my_server`.

## Multiple windows inside a single session
Another way of using `screen` is to create a single session, and then use
multiple "screens" within that session.  (Note: the option above using
a dedicated session for your server is the recommended procedure.)

See list of active screens:  `ctrl-a "`

Create a new screen:  `ctrl-a c`

Switch to a different screen:  `ctrl-a <#>` where `<#>` is the number of the
screen.

To rename the current screen:  `ctrl-a A`

### In a single session, how to run a server on one screen and do other things on a second screen
Start a new session by entering `screen -S <session_name>`.  Type `ctrl-a c` 
to create a second screen.  In one
of the screens, start your server.  Then, switch to the other screen by
typing `ctrl-a "` and choosing the other screen.  You can now work in this
second screen while the server is running in the other.



## References
<https://linuxize.com/post/how-to-use-linux-screen/>

<https://www.gnu.org/software/screen/manual/screen.html>