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
`conda activate <Environment Name>`

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

 ## Links
 <https://docs.python.org/3/tutorial/venv.html> for information on `pip` and
 virtual environments in Linux.
 
 
 <https://conda.io/docs/user-guide/tasks/manage-environments.html#> for 
 information on Conda Virtual Environments
 