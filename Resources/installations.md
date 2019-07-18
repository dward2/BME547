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
 

## Notepad++
* In order to access from CMD prompt, added to PATH.