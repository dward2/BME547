# Python Virtual Environments

## Intro
Python comes with standard set of libraries and functionality.  This base
functionality can be expanded by the installation of additional packages.
These additional packages can be added to the base installation on your 
computer.  However, there is the possibility that some installed packages
could interfere with each other.  Or, some existing programs might use an 
older version of a package that would conflict with a newer one installed
in the base installation.  

For these reasons, it is recommended to create a virtual environment for each
project in which you work.  This virtual environment will contain the specific
packages needed for that program.  And, other users can then recreate this
virtual environment to run your code and know that they will have the same
Python environment for which the code was originally written.

In the instructions below, anything contained in `<>` should be replaced by
the user with the appropriate information without the `<` or `>`.  For
example, `pip install <PackageName>` should be entered as `pip install numpy`.

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

#### Create a New Virtual Environment
First, navigate to the folder containing your project.  This can be the same 
folder as your git repository.

Type  
`python3 -m venv <VirtualEnvironmentName>`  
where `<VirtualEnvironmentName>` is the desired name of the virtual
environment.  For example `python3 -m venv MyVenv` makes a virtual
environment with the name `MyVenv`.  A subfolder with the name of the virtual
environment will be created in the folder.

#### Activate a Virtual Environment
In the same folder in which you entered the above command, type  
`source <VirtualEnvironmentName>/bin/activate`  
Following the same example as above:  `source MyVenv/bin/activate`

#### Installing a single package in virtual environment
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


#### Deactivate a Virtual Environment
`deactivate`


## Windows / Conda
Conda is a Python Package repository for Windows.
Enter the following commands at the Anaconda Prompt.

#### To create a new virtual environment
`conda create --name <Environment Name>`  
where `<Environment Name>` is the name of the virtual environment to be created.

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
name: myvenv
dependencies:
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
 using the command `python3 -m venv MyVenv` will create a folder called 
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
 