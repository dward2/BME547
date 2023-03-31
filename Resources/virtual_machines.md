# Virtual Machines
Virtual machines (VMs) provide a cloud-based virtualization of a complete 
operating system that allows you access to a virtual computer from any other 
computer.  In this class, we will use virtual machines to host servers that we 
write.

## Choice of Virtual Machine
You have the choice to set-up either a Linux virtual machine or a Windows
virtual machine.
* Linux 
    - A Linux operating system, will behave similar to macOS command line, and
      to a lesser extent, the GitBash command line from Windows.
    - This is what I will be demonstrating in class.
    - Will come with git and Python pre-installed.
* Windows 10
    - Will give the familiar Windows GUI.
    - Will require the installation of git and Python just like at the start
      of the semester.
    - Allows for the use of an IDEs or GUI code editors.
    - Requires using a VPN to access when not on the Duke network

I would recommend setting up the Linux machine.  It is simpler to setup and
use.  We will primarily be developing the server on our local computers and
only using the VM to deploy the server.  So, access to the command line and
a terminal editor for simple code changes are all that is really needed.
However, if you want the ability to use an IDE, Windows is an option.

Duke OIT allocates each student access to one virtual machine.  In a new system
started this year, I am also able to setup a certain number of
VM reservations specific to this course which do not count against your 
regular student allocation of one virtual machine.  But, I do not know if this
course-specific machine will be able to be kept after the end of the semester.

So, if you want to set-up a virtual machine and guarantee that it will remain
active after the end of the semester (and until you graduate), you will want
to NOT select the course-specific machine.  If you are already using your one
virtual machine, or don't care to keep this VM after the semester, select the
course-specific option.

## Setting up your Virtual Machine

* Visit https://vcm.duke.edu/ and log in to the Virtual Computing Manager (VCM)
using your NetID.
* Click on "Reserve a VM".
* Select the type of VM you would like.
  + Look under the "Everything" heading and select the "All" tab.
  + To select the course-specific Linux option, click on 
    "BME 547 - 01: Medical Software Design (Lecture)".
  + To select the Linux option from your personal allocation, click on 
    "Ubuntu Server 20.04".
  + To select the Windows option from your personal allocation, click on 
    "Windows 10".
* A window may open up with the heading "No SSH Key Found" and gives some 
  information about connecting using SSH.  Select the "Proceed with the less
  secure option" button to skip setting up an SSH key (unless you prefer to
  set up an SSH key, which you are welcome to do).
* A window may open up asking you to agree to the terms of use.  Select Agree.
* Depending on virtual machine availability, your VM may be available
immediately, or may take some time to set up.  You will receive an e-mail when
it is available.
* Once the VM is available, you will see it listed on the home page of 
<https://vcm.duke.edu>.  
* Clicking on the name of your virtual server will allow you access to the VM
Management Tools.  Your virtual server will have a default name such as 
`vcm-####.vm.duke.edu`.  This will be used as the URL to access your server.
The user ID assigned to you to access this virtual machine should be the same
as your NetID.  For now, you can ignore the Admin username and password.

## Accessing your Linux Virtual Machine
* First, make sure your VM is powered on by clicking "Power On" in the Virtual 
Computing Manager.
* You will need an SSH client on your computer, which is an application that
allows you to access and interact with the Linux VM.  There are a variety of
options for SSH clients.  
  + For macOS and Windows, there is a built-in SSH client you can run from the 
    Terminal/CMD/GitBash window.  
    + Type `ssh user@hostname` where `user` is the user account to be accessed
      (usually your Duke NetID) and `hostname` is the name of the server.  For 
      example: `aa123@vcm-1111.vm.duke.edu`.  
    + At the first access,  you may be asked to verify the authenticity of the
      host.  Type `yes` if you are sure you entered the correct VM address.
      The connection will be closed and you will need to connect again.
    + Upon connecting, you will be prompted for your password.  This is your
      Duke NetID password.  You will not see any characters in the terminal
      when typing your password.  Enter your password followed by "Enter".
    + You will now see your virtual machine linux prompt.
      Typing `exit` at the prompt will close the connection to the VM and 
      return you to your local command line prompt.
  + For Windows, a variety of free, third-party software exists, including:  
    ++ PuTTY, <https://www.chiark.greenend.org.uk/~sgtatham/putty/latest.html>  
    ++ MobaXterm, <https://mobaxterm.mobatek.net/>
    
#### Using PuTTY (as of March 2019)
*  Upon running PuTTY, the initial window will be the PuTTY Configuration 
window.  On the left-hand pane of the window, "Session" should be chosen.
*  In the "Host Name" box on the right-hand side, enter the name of your 
VM (example, `vcm-####.vm.duke.edu`).
* A "PuTTY Security Alert" window may open.  Click "Yes" to continue.
* Login to your VM using your NetID and password.
* To avoid having to enter your VM host name each time, enter your host name as
above, and then enter a name in the "Saved Sessions" text box and click "Save".
In the future, you will just be able to "Load" that profile.

#### Using MobaXterm (Personal Edition v11.0)
*  Upon running, MobaXterm, click on the "Session" button on the upper left.
*  In the "Session settings" window that opens, select "SSH" from the toolbar.  
*  In the "Remote host" box, enter your VM name (`vcm-####.vm.duke.edu`).
*  To make future logins easier, you can enter your NetID in the "Specify 
Username" field.  
*  Click "Ok" and a terminal window should open.  Login to your account
using your NetID and password.  
*  In the future, MobaXterm will have saved this session information for easy
log-in.
* Note that MobaXterm has a nice feature of being able to access the files
in your VM through a menu system on the left-hand pane of the MobaXterm
window.  You can then open and edit these files in a local GUI text editor
on your local computer for easier editing.  You can also upload and download
files through this interface.

## Accessing your Windows Virtual Machine
The following instructions have been developed using a local Windows 10 machine.
They may or may not work if you are using macOS to access a Windows VM.
* First, make sure your VM is powered on by clicking "Power On" in the Virtual 
Computing Manager.
* Under VM Management Tools for your VM in the Virtual Computing Manager, you
will see a blue button labeled "Remote Desktop".  Click on that it will 
prompt you to download a file with the same name as your VM and an extension of
"*.rdp".  Save this file on your computer and run it.  
* This file will establish a remote desktop connection.  Click on "Connect"
when the Remote Desktop Connection window opens.  
* Enter your NetID \password in the Windows Security "Enter your 
credentials" window and click "Ok".
* A remote access desktop window should open (likely to full screen).  You can
now use the remote Windows computer just as you would a local Windows computer.
* To disconnect, simply choose "Disconnect" from the Power window.  This will
keep your remote machine or server active.  If you choose "Shutdown", the VM
will completely turn off, and you will need to turn it back on in the VCM.
  
**NOTE:** If you are accessing your Windows VM from outside of the Duke
network, you will need first need to access the Duke network through a VPN.
See <https://oit.duke.edu/what-we-do/services/vpn> for more information.

## Using Your Virtual Machine
Once your machine is set up, you will need to configure it for git and Python
just as we described at the beginning of the semester.  

This means making sure you have the 
software needed for using git, python, installing packages, and using virtual 
environments.  You will also need to set up an SSH key to use with GitHub.
Review the information from the
[setup assignment](/Assignments/01_tool_setup_git_intro.md) and
[virtual_environments.md](/Resources/virtual_environments.md).  For the Linux 
virtual machine, you can follow the information given for macOS users.

### For the course-specific Linux VMs, as of March 2023
* The default installation has `python3` (version 3.10.6) installed.  So, you 
  will need to enter `python3` and `pip3` to access version 3.  Or, you can 
  add the following aliases to your `.bashrc` (or `.bash_aliases` if
  it exists) file:

  ```bash
  alias pip='pip3'
  alias python='python3'
  ```
* The `pip` program is not installed as part of this Python installation.  If
  you are unable to run pip, you can install it as follows:
  ```bash
    sudo apt install python3-pip
  ```
  You may be prompted to enter your password (which is your Duke NetID).
* The `venv` package is not installed as part of this Python installation.
  If you attempt to install a virtual environment and get an error, install
  `venv` with the following command:
  ```bash
  sudo apt install python3.10-venv
  ```
  You may be prompted to enter your password (which is your Duke NetID).  Once 
  `venv` is installed, you
  should then be able to create your virtual environment using `python3 -m 
  venv venv`.

### Deploying Your Server Code on the Virtual Machine
* Clone your repository onto the virtual machine
* If using a Linux virtual machine, follow the instructions for 
  using `screen` [here](/Resources/WebServices/screen.md) and open up a
  screen session in which to run the server.
* Create and activate a virtual environment.  Use the 
`requirements.txt` file to install the needed packages.
* In the server code, modify add the named argument 
`host="0.0.0.0"` to the `app.run()` command as follows:
  ```python
  app.run(host="0.0.0.0")
  ```
* Run the server code.
* If using a Linux virtual machine, disconnect from the screen session so 
  you can log off the virtual machine without shutting down the server.


### Disable Automatic Power Downs
As a default, your virtual machine is configured to automatically power down
at the end of every day.  This a desirable power saving tool.  However, if
you need to keep your VM and server running 24/7, you can disable this 
setting as follows.
* Visit <https://vcm.duke.edu/> and log in to the Virtual Computing Manager 
(VCM) using your NetID.
* Select the appropriate virtual machine under the "My Reservations" section.
* Under VM Management Tools, you should see a checkbox labeled "Automatic
power downs?".  Uncheck this box.  You will be prompted for a reason.  Enter
that you need to have your VM running 24/7 for a class.

