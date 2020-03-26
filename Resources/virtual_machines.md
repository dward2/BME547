# Virtual Machines
Virtual machines (VMs) provide a cloud-based virtualization of a complete 
operating system that allows you access to a virtual computer from any other 
computer.  In this class, we will use virtual machines to host servers that we 
write.

## Setting up your Virtual Machine
Duke OIT has allocated each student access to one virtual machine.  If you
are already using your virtual machine for another class or project, and would
prefer not to use that machine for this class, please let an instructor know
and a request for a second virtual machine can be made.

* Visit https://vcm.duke.edu/ and log in to the Virtual Computing Manager (VCM)
using your NetID.
* Click on "Reserve a VM".
* Select the type of VM you would like.  We will be demonstrating the use of 
a Linux (Ubuntu) VM in class.  It is possible to use Windows 10 to host your
server, if you prefer, but does require some additional set-up.
* Depending on virtual machine availability, your VM may be available
immediately, or may take some time to set up.  You will receive an e-mail when
it is available.
* Once the VM is available, you will see it listed on the home page of 
<https://vcm.duke.edu>.  
* Clicking on the name of your virtual server will allow you access to the VM
Management Tools.  Your virtual server will have a default name such as 
`vcm-####.vm.duke.edu`.  This will be used as the URL to access your server.
The user ID assigned to you to access this virtual machine should be the same
as your NetID.  For now, you can ignore the Admin user name and password.

## Accessing your Linux Virtual Machine
* First, make sure your VM is powered on by clicking "Power On" in the Virtual 
Computing Manager.
* You will need an SSH client on your computer, which is an application that
allows you to access and interact with the Linux VM.  There are a variety of
options for SSH clients.  
  + For macOS, there is a built-in SSH client you can run from the Terminal 
  window.  Type `ssh user@hostname` where `user` is is the user account to
  be accessed and `hostname` is the name of the server.  For example:
  `aa123@vcm-1111.vm.duke.edu`.  Then, login to your VM using your NetID and
  password.
  + For Windows, a variety of free, third-party software exists, including:  
    ++ PuTTY, <https://www.chiark.greenend.org.uk/~sgtatham/putty/latest.html>  
    ++ MobaXterm, <https://mobaxterm.mobatek.net/>
    
#### Using PuTTY
*  Upon running PuTTY, the initial window will be the PuTTY Configuration 
window.  On the left hand pane of the window, "Session" should be chosen.
*  In the "Host Name" box on the right-hand side, enter the name of your 
VM (example, `vcm-####.vm.duke.edu`).
* A "PuTTY Security Alert" window may open.  Click "Yes" to continue.
* Login to your VM using your NetID and password.
* To avoid having to enter your VM host name each time, enter your host name as
above, and then enter a name in the "Saved Sessions" text box and click "Save".
In the future, you will just be able to "Load" that profile.

#### Using MobaXterm
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
in your VM through a menu system on the left hand pane of the MobaXterm
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
will completely turn off and you will need to turn it back on in the VCM.
  
**NOTE:** If you are accessing your Windows VM from outside of the Duke
network, you will need first need to access the Duke network through a VPN.
See <https://oit.duke.edu/what-we-do/services/vpn> for more information.

## Using Your Virtual Machine
Once your machine is set up, you will need to configure it for git and Python
just as we described at the beginning of the semester.  

This means making sure you have the 
software needed for using git, python, installing packages, and using virtual 
environments.  Review the information from the 
[setup assignment](/Assignments/01_tool_setup_git_intro.md) and
[virtual_environments.md](/Resources/virtual_environments.md).  For the Linux 
virtual machine, you can follow the information given for macOS users.
