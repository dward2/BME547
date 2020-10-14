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
`-S <session_name>` arguement.

Within each session, you can have multiple screens.  

## Using Screen
Start a new screen session:  `screen`

Start a new screen session with a given name:  `screen -S <session_name>`

List of commands:  `ctrl-a ?`

See list of active screens:  `ctrl-a "`

Create a new screen:  `ctrl-a c`

Switch to a different screen:  `ctrl-a <#>` where `<#>` is the number of the
screen.

To rename the current screen:  `ctrl-a A`

To disconnect from the current session:  `ctrl-a d`  

To restart an existing (detached) session:  `screen -r`

To stop and delete a screen session, get into that screen session using
`screen -r`, and then typing `ctrl-a` followed by `:` then `quit`


## How to run a server on one screen and do other things on a second screen
In linux, run `screen`.  Type `ctrl-a c` to create a second screen.  In one
of the screens, start your server.  Then, switch to the other screen by
typing `ctrl-a "` and choosing the other screen.  You can now work in this
second screen while the server is running in the other.

## Keeping a server running while logging off
Follow above steps.  Then, in the non-server screen, type `ctrl-a d` to 
disconnect from screen.  You can now log off safely.  When you log back on,
you can seen that your screen session is "detached" by typing `screen -ls`.
To reattach to your screens, type `screen -r`.




## References
<https://linuxize.com/post/how-to-use-linux-screen/>
<https://www.gnu.org/software/screen/manual/screen.html>