# Installation Information for Windows

## Git
* Install from <https://git-scm.com>.
* During installation, select "Git from the Command Line option" under 
"Adjusting You PATH environment".  This will allow you to use git from the 
Windows CMD window or PowerShell as desired.
* Choose "Checkout Windows-style, commit Unix-style line endings" under 
"Configuring the line ending conversion".  This is the Windows default option.


## Python
* On opening install screen, select "Add Python 3.7 to Path"
* Choose option to relax 260 character PATH limit at end of install.

+ No need to separately install pip and venv.  It was part of base package.
+ Activation of virtual environment uses `source <venvName>/Scripts/activate`

* To use `python` from the GitBash command line, do the following:
  
  - Open GitBash and type `cd ~` to ensure you are in your home directory.
  - Open the `.bashrc` file by typing `nano .bashrc`
  - At the end of the file, add the following line: 
  `alias python='winpty python.exe'`
  - Save and close the file.
  - Close and exit from the GitBash window
  - Reopen the GitBash window and `python` should work from the command line.
 

## Notepad++
* In order to access from CMD prompt, added to PATH.