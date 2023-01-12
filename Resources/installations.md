# Installation Information for Windows

## Git
* Install from <https://git-scm.com>.
* During installation, accept the preselected options with the following
exceptions:
  1. On the`Select Components` screen, I deselect `Git Bash Here` and `Git
  GUI Here` under `Windows Explorer integration` to prevent cluttering my
     right-click context menu.  But, you may leave if desired.
  2. On the `Choosing the default editor used by Git` screen, I would select
  a different editor rather than Vim.  I like Notepad++, but standard
     Notepad is a good choice, also.
  3. On the `Adjusting the name of the initial branch in new repositories` 
  screen, select `Override the default branch name for new repositories` and
     enter `main` as the new default name.  This will now mirror the behavior
     of GitHub.
  4.  On the `Configuring the line ending conversions` screen, the default 
  should be `Checkout Windows-style, commit Unix-style line endings`.  Make
      sure that it is.


## Python
* On opening install screen, select "Add Python to Path".
* Run default installation.
* Choose option to "Disable path length limit" at the end of the install.

+ No need to separately install pip and venv.  It is part of base package.

* To enable use of `python` from the GitBash command line, do the following:
  
  - Open GitBash and type `cd ~` to ensure you are in your home directory.
  - Open the `.bashrc` file by typing `nano .bashrc` (or use your editor of
  choice)
  - At the end of the file, add the following line: 
  `alias python='winpty python.exe'`
  - Save and close the file.
  - Close and exit from the GitBash window
  - Reopen the GitBash window and `python` should work from the command line.
 

## Notepad++
* In order to access from CMD prompt or GitBash, find the file location of
`notepad++.exe` and add that to the PATH.  See 
[running_python_from_git_bash.md](running_python_from_git_bash.md) for an
example of adding to the PATH variable.  
* See [notepad++.md](notepad++.md) for more info on Notepad++.