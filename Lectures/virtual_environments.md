# Python Virtual Environments

## Intro
Python comes with a standard set of libraries and functionality.  This base
functionality can be expanded by the installation of additional packages.
These additional packages can be added to the base installation on your 
computer.  However, there is the possibility that some installed packages
could interfere with each other.  Or, some existing programs might use an 
older version of a package that would conflict with a newer one installed
in the base installation.  

See the Case Study below for an example of how using virtual environments can
save you from versioning troubles.

For these reasons, it is recommended to create a virtual environment for each
project in which you work.  This virtual environment will contain the specific
packages needed for that program.  And, other users can then recreate this
virtual environment to run your code and know that they will have the same
Python environment for which the code was originally written.

In the instructions below, anything contained in `<>` should be replaced by
the user with the appropriate information without the `<` or `>`.  For
example, `pip install <PackageName>` should be entered as `pip install numpy`.

## Using Virtual Environments
### Create a virtual environment
First, navigate to the folder containing your project.  This can be the same 
folder as your git repository.

Type  
`python -m venv <VirtualEnvironmentName>`  
where `<VirtualEnvironmentName>` is the desired name of the virtual
environment.  For example `python -m venv MyVenv` makes a virtual
environment with the name `MyVenv`.  A subfolder with the name of the virtual
environment will be created in the folder.

### Activate a Virtual Environment
#### Linux (MacOS)
In the same folder in which you entered the above command, type  
`source <VirtualEnvironmentName>/bin/activate`  
Following the same example as above:  `source MyVenv/bin/activate`

#### Windows Bash
In the Bash window, from the project folder, type:
`source <VirtualEnvironmentName>/Scripts/activate`
Following the example above: `source MyVenv/Scripts/activate`
#### Windows Command Line
At the command prompt, in the project directory, type:
` ./<VirtualEnvironmentName>/Scripts/activate.bat`

For the example above, it would be: `./MyVenv/Scripts/activate.bat`
### Installing a single package in virtual environment
`pip install <PackageName>` installs the latest version of PackageName

`pip install <PackageName>==#.#.#` installs the specified version of 
PackageName

`pip install --upgrade <PackageName>` updates PackageName to the latest version

#### Install multiple files (recommended workflow)
For easy duplication of virtual environments, it is recommended to maintain a
list of packages to be installed in a virtual environment in a file called
`requirements.txt`.  This file is a simple list of the packages to be installed,
with or without versions.  These can then all be installed at once with the
following command.

`pip install -r requirements.txt`

From an existing virtual environment, you can create a `requirements.txt` file
to generate duplicate virtual environments with the following command.

`pip freeze > requirements.txt`

#### Information about current Virtual Environment
List of packages in the current environments:  
`pip list`

Information about a specific package:  
`pip show <PackageName>`


### Deactivate a Virtual Environment
`deactivate` 


## Windows / Conda
Conda is a Python Package repository for Windows.
Enter the following commands at the Anaconda Prompt.

#### To create a new virtual environment
`conda create --name <Environment Name> python=3.11`  
where `<Environment Name>` is the name of the virtual environment to be created.
`3.11` can be replaced with the preferred version number.

If you don't specify a specific version of Python, none will be installed
in the environment.  Then, when other packages are installed into this
environment, they will load whatever version of Python they require.  But, this
can lead to version problems if different packages require different versions
of Python.  Therefore, it is recommended to specify a Python version when
creating the virtual environment.

#### To activate a virtual environment
`conda activate <Environment Name>` or `activate <Environment Name>`  
(For running from the Windows command prompt, the second option above is the correct one.)

#### To deactivate a virtual environment
`deactivate`

#### To list available virtual environments
`conda env list`

#### To list packages installed in current environment
`conda list`

#### To install a single package in virtual environment
To install in the current environment:  
`conda install <PackageName>`

To install in a different virtual environment:  
`conda install --name <Environment Name> <PackageName>`

To install a specific version of the package, include `=#.#.#` after the 
package name.

#### To create a virtual environment with multiple packages (recommended workflow)
For easy duplication of virtual environments, it is recommended to maintain a
list of packages to be installed in a virtual environment in a file called
`environment.yml`.  This file is formatted similar to the following example:
```
name: my_venv
dependencies:
  - python=3.11
  - numpy
  - scipy
```
If specific versions of a package is required, add `=#.#.#` after the package
name.

A virtual environment with the name given in the `environment.yml` file can
then be created with the following command.
`conda env create -f environment.yml`

#### Create an `environment.yml` file from existing environment
Note that this procedure will delete any existing environment.yml.

Activate the desired environment, then type the following.  
`conda env export >environment.yml`

 ## Virtual Environments and Git  (`.gitignore`)
 The creation of virtual environments can place a lot of files into a subfolder
 of your project.  If you are not careful, it is easy to accidentally commit
 those files into your git repo, thereby increasing the size of your repo and
 the time it takes to add/commit/push.  To avoid adding files to your repo
 that should be excluded, add a file called `.gitignore` to your repository.
 In this file, list either the specific files or paths that you do not want
 included in your repository.  For example, creating a virtual environment
 using the command `python -m venv MyVenv` will create a folder called 
 `MyVenv`.  To exclude this directory from the repo, I would add the following
 line to `.gitignore`:
 ```
 MyVenv
 ```
 If there are specific files, or types of files you want to exclude, you can
 specify them directly.  For example:  
 `*.txt` will exclude all files with the `txt` extension.  
 `file1.txt` excludes the specfically named file.  
 `MySub/file1.txt` excludes the specifically named file in the MySub sub-folder.
 
 Later, when using IDEs or other tools that also generate additional files that
 you do not want stored in your repo, those files can also be added to 
 `.gitignore`.
 
 ## Case Study:  `sendgrid` module update
 `sendgrid` is a package that provides Python functionality to access the
 SendGrid API for sending e-mails from your Python code.  A project was
 started when the released version of `sendgrid` was version 5.6.  People who
 started the project and created a virtual environment from a `requirements.txt`
 file with the `sendgrid` entry had version 5.6 installed and they started
 code development using the version 5.6 syntax.
 
 During the middle of the project, the `sendgrid` package was updated to
 version 6.0.  This update was considered a BREAKING update, meaning that the
 functionality and syntax of package changed.  Before this update was 
 discovered, there were two types of impacts:  
 * Some people did not start the project before the update.  So, they
   created a virtual environment and installed `sendgrid` from their
   `requirements.txt` file.  This installed the latest version of `sendgrid`
   which was now version 6.0.  However, they followed the version 5.6 syntax,
   being unaware of the update.  Their code didn't work.
 * Those who had created their virtual environment before the update had 
   version 5.6 installed, and they wrote their code using version 5.6 syntax.
   Everything worked smoothly for them.  However, when someone else
   downloaded their code, this new user would create a virtual environment
   using the downloaded `requirements.txt` file.  This file would install
   `sendgrid`, but would install the latest version 6.0.  Then, then they tried
   to run the code written with version 5.6 syntax, the code would not work.
   
 This second case in particular highlights the value of virtual environments,
 when done correctly.  Best practice is to specify the specific version of
 each package used in the development virtual environment in the 
 `requirements.txt` file.  In this way, you
 "lock in" in the version that was used during development so that future
 virtual environments that are created will also have the same version of
 each package.  This avoids version conflicts.
 
 Specific version of packages can be specified using the syntax shown in 
 the following example:
 ```
 sendgrid == 5.6.0
 ```
 Therefore, it is recommended that specific versions be defined in the
 `requirements.txt` file.  The `requirements.txt` file can be generated from
 an existing virtual environment, and will include version numbers, by 
 using the `pip freeze > requirements.txt` command described above.
 
 
 ## Links
 <https://docs.python.org/3/tutorial/venv.html> for information on `pip` and
 virtual environments in Linux.
 
 
 <https://conda.io/docs/user-guide/tasks/manage-environments.html#> for 
 information on Conda Virtual Environments
 
 <https://pip.pypa.io/en/stable/reference/pip_install/> for reference 
 documentation on pip.
 
# In Class Exercise
For the next homework assignment, you will need to use a Jupyter Notebook.
So, in class, we are going to make a virtual environment, install `jupyter`,
and run a Jupyter Notebook.
* Make a new folder, and within that folder, create a new virtual environment.
* Activate this environment, and install `jupyter` in this environment.
* Follow instructions below for starting and using a Jupyter Notebook
## Starting  Jupyter Notebook
To start a new Jupyter Notebook, type
```
jupyter notebook
```
This will ideally open a browser window.  If not, a URL should be given in your
terminal window that you can open with a browser.
![images/JN_empty.JPG](../Resources/Jupyter/images/JN_empty.JPG)
To start a new Jupyter Notebook, click on the "New" button and choose
"Python 3" from the dropdown menu.  A new browser window should open.
![images/JN_new_notebook.JPG](../Resources/Jupyter/images/JN_new_notebook.JPG)
You can now explore the notebook.  You can add new cells by clicking on the
"+" button.  You can change the type of cell (whether it contains code or 
markdown) by clicking on the drop down that says "Code" in the picture above.
You can change the order of the different cells using the arrow buttons.

Enter code into a cell.  To execute the cell, type `Shift+Enter`.

**NOTE**: On Windows with Python 3.8, the Python Kernel did not start in
the Jupyter Notebook.  One possible fix can be found 
[here](../Resources/Jupyter/notebook_python38_fix.md).

When you are ready to save the notebook, choose the "Save As..." option under 
the File menu.

When you are finished, you can click "Logout".  Go back to the command prompt.
If there is not a prompt available for you to type, the jupyter server may
still be running.  Click Ctrl-C to exit the server.  Then, you can see that
a new jupyter notebook has been created in your directory with the file
extension `.ipynb`.

## Opening an existing Jupyter Notebook
```
jupyter notebook <notebookname>.ipynb
``` 










 # Misc Stuff
 ## Linux (and MacOS)
#### Install pip

`pip` is the tool to install packages from the most popular repository of
Python packages, `PyPI`.  `pip` is used in the MAC and Linux terminal windows.

To see if you have pip installed, type `pip` or `pip3` on the command
line.  If you see usage information come up, it is installed.  If not,
you will need to install pip by typing

```
sudo apt install python3-pip
```

Note:  depending on how it is installed and the install history on your 
computer, you may need to type `pip3` instead of `pip` in the following
instructions.

#### Install Virtual Environment Package
You then need to install the virtual environment package by typing 
```
sudo apt-get install python3-venv
```

## Details related to Python Path
### `venv`
When you first start a Git Bash or terminal window, you start in the 
default environment for Python.  Entering `python` will run whatever version
of Python can be found in your default paths.  For example, in my installation
(Windows 10), entering the command `where python` yields the following:
```bash
daw74@vcm-23932 MINGW64 ~/repos/project
$ where python
C:\Users\daw74\AppData\Local\Programs\Python\Python311\python.exe
```

Now, when I create a virtual environment, all of the files necessary to run
Python are copied into the folder created with the virtual environment.  Then,
when the virtual environment is activated, the path is modified so that it
looks for Python in the new virtual environment location.

```bash
daw74@vcm-23932 MINGW64 ~/repos/project
$ python -m venv my_venv

daw74@vcm-23932 MINGW64 ~/repos/project
$ source my_venv/Scripts/activate
(my_venv)
daw74@vcm-23932 MINGW64 ~/repos/project
$ where python
C:\Users\daw74\repos\project\my_venv\Scripts\python.exe
C:\Users\daw74\AppData\Local\Programs\Python\Python311\python.exe

```
Now, a new path has been given priority that points to the Python version 
copied into the virtual environment.  When the environment is deactivated, this
new path is removed and points back to the default Python location (see below).  

```bash
(my_venv)
daw74@vcm-23932 MINGW64 ~/repos/project
$ deactivate

daw74@vcm-23932 MINGW64 ~/repos/project
$ where python
C:\Users\daw74\AppData\Local\Programs\Python\Python311\python.exe
```

### `conda`
When you first start an Anaconda Prompt or Anaconda Powershell Prompt (which
is shown in the examples below), you start in the base environment.  The base
environment will be pointing to a python version isntalled as part of Anaconda.
```bash
(base) PS C:\Users\daw74\repos\project> where.exe python
C:\Users\daw74\AppData\Local\anaconda3\python.exe
C:\Users\daw74\AppData\Local\Programs\Python\Python311\python.exe
```
The use of the `conda list` command gives you all of the packages installed.
If you installed the full Anaconda, this will be a long list and includes
Python.
```bash
(base) PS C:\Users\daw74\repos\project> conda list
# packages in environment at C:\Users\daw74\AppData\Local\anaconda3:
#
# Name                    Version                   Build  Channel
alabaster                 0.7.12             pyhd3eb1b0_0
anaconda-client           1.11.2          py310haa95532_0
anaconda-navigator        2.4.0           py310haa95532_0
anaconda-project          0.11.1          py310haa95532_0
anyio                     3.5.0           py310haa95532_0
appdirs                   1.4.4              pyhd3eb1b0_0
...
python                    3.10.9               h966fe2a_1
...
zeromq                    4.3.4                hd77b12b_0
zfp                       0.5.5                hd77b12b_6
zict                      2.1.0           py310haa95532_0
zipp                      3.11.0          py310haa95532_0
zlib                      1.2.13               h8cc25b3_0
zope                      1.0             py310haa95532_1
zope.interface            5.4.0           py310h2bbff1b_0
zstandard                 0.19.0          py310h2bbff1b_0
zstd                      1.5.2                h19a0ad4_0
```

When we make a new environment using conda, an empty environment is created.
(Note: your actual response may vary from the below as I have edited it 
somewhat for brevity.)

```bash
(base) PS C:\Users\daw74\repos\project> conda create --name my_venv
Collecting package metadata (current_repodata.json): done
Solving environment: done

## Package Plan ##

  environment location: C:\Users\daw74\AppData\Local\anaconda3\envs\my_venv

Proceed ([y]/n)? y

Preparing transaction: done
Verifying transaction: done
Executing transaction: done
#
# To activate this environment, use
#
#     $ conda activate my_venv
#
# To deactivate an active environment, use
#
#     $ conda deactivate

(base) PS C:\Users\daw74\repos\project> conda activate my_venv
(my_venv) PS C:\Users\daw74\repos\project> conda list
# packages in environment at C:\Users\daw74\AppData\Local\anaconda3\envs\my_venv:
#
# Name                    Version                   Build  Channel
```

Notice that after activating the new environment, `conda list` returns nothing 
installed in the environment, including Python.  The "Anaconda" version of
Python is no longer available in this environment as seen by:
```bash
(my_venv) PS C:\Users\daw74\repos\project> where.exe python
C:\Users\daw74\AppData\Local\Programs\Python\Python311\python.exe
```
Notice that the anaconda version is no longer in the path.  But, the generic
Python that is also available on this computer is still there.  So, Python
will still run.  But, when another package is loaded into the environment,
conda will install a version of Python because it believes that no Python
exists.  For example, let's install the `wikipedia` package.

```bash
(my_venv) PS C:\Users\daw74\repos\project> conda install -c conda-forge wikipedia
Collecting package metadata (current_repodata.json): done
Solving environment: done

## Package Plan ##

  environment location: C:\Users\daw74\AppData\Local\anaconda3\envs\my_venv

  added / updated specs:
    - wikipedia

The following NEW packages will be INSTALLED:

  beautifulsoup4     conda-forge/noarch::beautifulsoup4-4.12.2-pyha770c72_0
  certifi            pkgs/main/noarch::certifi-2020.6.20-pyhd3eb1b0_3
  pip                conda-forge/win-64::pip-20.0.2-py36_1
  python             conda-forge/win-64::python-3.6.15-h39d44d4_0_cpython
  python_abi         conda-forge/win-64::python_abi-3.6-2_cp36m
  requests           conda-forge/win-64::requests-2.12.5-py36_0
  setuptools         conda-forge/win-64::setuptools-49.6.0-py36ha15d459_3
  soupsieve          conda-forge/noarch::soupsieve-2.5-pyhd8ed1ab_0
  ucrt               conda-forge/win-64::ucrt-10.0.22621.0-h57928b3_0
  vc                 conda-forge/win-64::vc-14.3-h64f974e_17
  vc14_runtime       conda-forge/win-64::vc14_runtime-14.36.32532-hfdfe4a8_17
  vs2015_runtime     conda-forge/win-64::vs2015_runtime-14.36.32532-h05e6639_17
  wheel              conda-forge/noarch::wheel-0.36.2-pyhd3deb0d_0
  wikipedia          conda-forge/noarch::wikipedia-1.4.0-py_2
  wincertstore       conda-forge/noarch::wincertstore-0.2-pyhd8ed1ab_1009

Proceed ([y]/n)? y

Downloading and Extracting Packages

Preparing transaction: done
Verifying transaction: done
Executing transaction: done
```
Notice that Python version 3.6 is being installed.  That is because the 
`wikipedia` package specifies that at least Python 3.6 must be installed.
Since conda doesn't see an installed version of Python, it uses that version.
Unfortunately, some of the other supporting packages have been updated such 
that they no longer work with Python 3.6.  So, the above installation will fail
when trying to use `wikipedia`.  

Therefore, I would suggest it is best practice to create a conda virtual
environment with Python already installed.  You can do this during the creation
of the virtual environment as follows:

```bass
(base) PS C:\Users\daw74\repos\project> conda create --name my_venv python=3.11
Collecting package metadata (current_repodata.json): done
Solving environment: done

## Package Plan ##

  environment location: C:\Users\daw74\AppData\Local\anaconda3\envs\my_venv

  added / updated specs:
    - python=3.11


The following NEW packages will be INSTALLED:

  bzip2              conda-forge/win-64::bzip2-1.0.8-h8ffe710_4
  ca-certificates    conda-forge/win-64::ca-certificates-2023.7.22-h56e8100_0
  libexpat           conda-forge/win-64::libexpat-2.5.0-h63175ca_1
  libffi             conda-forge/win-64::libffi-3.4.2-h8ffe710_5
  libsqlite          conda-forge/win-64::libsqlite-3.43.0-hcfcfb64_0
  libzlib            conda-forge/win-64::libzlib-1.2.13-hcfcfb64_5
  openssl            conda-forge/win-64::openssl-3.1.2-hcfcfb64_0
  pip                conda-forge/noarch::pip-23.2.1-pyhd8ed1ab_0
  python             conda-forge/win-64::python-3.11.5-h2628c8c_0_cpython
  setuptools         conda-forge/noarch::setuptools-68.1.2-pyhd8ed1ab_0
  tk                 conda-forge/win-64::tk-8.6.12-h8ffe710_0
  tzdata             conda-forge/noarch::tzdata-2023c-h71feb2d_0
  ucrt               conda-forge/win-64::ucrt-10.0.22621.0-h57928b3_0
  vc                 conda-forge/win-64::vc-14.3-h64f974e_17
  vc14_runtime       conda-forge/win-64::vc14_runtime-14.36.32532-hfdfe4a8_17
  vs2015_runtime     conda-forge/win-64::vs2015_runtime-14.36.32532-h05e6639_17
  wheel              conda-forge/noarch::wheel-0.41.2-pyhd8ed1ab_0
  xz                 conda-forge/win-64::xz-5.2.6-h8d14728_0

Proceed ([y]/n)? y

Downloading and Extracting Packages

Preparing transaction: done
Verifying transaction: done
Executing transaction: done
#
# To activate this environment, use
#
#     $ conda activate my_venv
#
# To deactivate an active environment, use
#
#     $ conda deactivate
```
Note that Python is now installed with the virtual environment.  Then, if the
`wikipedia` package is installed, it will not load Python 3.6 because a higher
version of Python is already installed.