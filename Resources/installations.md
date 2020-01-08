# Installation Information for Windows

## Git
* Install from <https://git-scm.com>.
* During installation, select "Git from the Command Line and also from 3rd 
Party software" under 
"Adjusting You PATH environment".  This will allow you to use git from the 
Windows CMD window or PowerShell as desired.
* Choose "Checkout Windows-style, commit Unix-style line endings" under 
"Configuring the line ending conversion".  This is the Windows default option.


## Python
* On opening install screen, select "Add Python 3.8 to Path".
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
[running_phython_from_git_bash.md](running_python_from_git_bash.md) for an
example of adding to the PATH variable.  
* See [notepad++.md](notepad++.md) for more info on Notepad++.