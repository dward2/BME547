# Assignment 01: Setup Course Tools & Git Introduction

## Getting Setup
1. Create an account on GitHub (https://github.com).  An understandable and
professional user name is suggested.  
   

2. To communicate your GitHub user name to us, you will open a GitHub issue 
with that information.
   1. Go into the BME547 repository (<https://github.com/dward2/BME547>) and 
  click on "Issues" in the tab bar at the top of the page.
   2. Click on the green "New issue" button.
   3. In the title, enter your name and the GitHub user name you created. For 
  example, "David Ward - dward2".
   4. In the comment area, please include your Duke e-mail address and whether
  your primary computer for this class is running Windows, macOS, or Linux.
   5. Click the green "Submit new issue" button.
 
 
3. Download and install `git` at https://git-scm.com.  We will be using 
`Git Bash`, *not* a GUI client.
   + **MAC** users:   
     `git` is likely already installed.  Open a Terminal window
and type `git --version`.  If you see a version number, it is already
installed.  If not, you will need to download it from the site above.
   + **Windows** users have two options:
     1. install from the above website (recommended) which will install the
   GitBash command window (see <a href="../Resources/installations.md">
   installations</a> for additional details), or
     2. use the Windows Subsystem for Linux 
    ([Ubuntu Linux Subsystem](https://docs.microsoft.com/en-us/windows/wsl/about)) 
    with Ubuntu allowing you to access `git` through Linux.  
    Note - this second option does not install `git` in your Windows environment, 
    so other Windows applications that have `git` hooks will not work.
   + **Everyone**: Add your name and e-mail to your local Git configuration by following the
     instructions under **Config**  on [this page](/Resources/Git/GitCommands.md#config). 


4. Set up an SSH key to allow local authentication with GitHub:
   1. Visit <https://docs.github.com/en/authentication/connecting-to-github-with-ssh>.
   2. When following the instructions on these webpages, make sure that you
      select the tab in the webpage for your computer type (Mac/Windows/Linux).
   2. From the page above, follow the instructions under the links:
      * If you think you may already have an SSH key, see [Checking for 
        existing SSH keys](https://docs.github.com/en/authentication/connecting-to-github-with-ssh/checking-for-existing-ssh-keys)
      * [Generating a new SSH key and adding it to the ssh-agent](https://docs.github.com/en/authentication/connecting-to-github-with-ssh/generating-a-new-ssh-key-and-adding-it-to-the-ssh-agent)
      * [Adding a new SSH key to your GitHub account](https://docs.github.com/en/authentication/connecting-to-github-with-ssh/adding-a-new-ssh-key-to-your-github-account)
      * [Testing your SSH connection](https://docs.github.com/en/authentication/connecting-to-github-with-ssh/testing-your-ssh-connection)
   3. To automatically load your SSH keys when starting git, follow the 
    instructions at [Working with SSH key passphrases](https://docs.github.com/en/authentication/connecting-to-github-with-ssh/working-with-ssh-key-passphrases)


5. Download and install `python`. 
   + **Mac** users:  
     * Python is likely already installed.  Open a Terminal window 
       and enter `python --version`.  You may see an output like 
       `Python 3.9.0`.
     * If the version number is 2.7, or if no version of python is found, 
       enter `python3 --version` into the terminal window.  
     * If you do not have any version 3 or if your version 3 is earlier than
       3.10, you will need to install the latest version of `python3`.
     * __Do not try to delete or "upgrade" the 2.7 version or any 
       other version currently on your 
   computer as it is a part of the macOS installation.__
     * Visit <https://docs.python.org/3/using/mac.html> for instructions on 
       installing Python. 
     * Note that if you have both `python2` and `python3` installed on your 
     computer, it is possible that you will have to enter `python3` in place
     of `python` to run the correct version.  Alternatively, you can set up an
     alias:
       + Open a terminal window and check the window title bar and see if it
         indicates you are using `bash` shell or a `zsh` shell.  Generally,
         if you are running macOS 10.14 or earlier, it will be a `bash` shell.
         With macOS 10.15 or higher, it could be either one.
       + Note that your terminal window may say something like `zsh is the
         most recent shell being used`.  In my experience, you do NOT need to
         upgrade to the `zsh` shell unless you want to.
       + If you are using a `bash` shell, you will need to make modifications
         to the `.bashrc` file.  If you are using a `zsh` shell, you will need
         to make modifications to the `.zshrc` file.
       + Enter `which python3` to determine the pathway to `python3`.  It
         will could be either `/usr/local/bin`, `/usr/bin`, 
         `/Library/Frameworks/Python.framework/Versions/3.12/bin/python3`, 
         or something similar.
       + You can modify the appropriate `rc` file determined above in one of 
         two ways, replacing `<python_path>` with the appropriate path 
         determined from the step above:
         - Enter  `echo "alias python=<python_path>" >> ~/.bashrc` or
           `echo "alias python=<python_path>" >> ~/.zshrc`
         - Manually edit the appropriate file and add the line 
           `alias python=<python_path>`  
       + You will need to do the same thing with the `pip` package installer.
       Type `pip --version` at the command line and an output similar to
       `pip 19.0.3 from /Library/Python/2.7/site-packages/pip-19.0.3-py2.7.egg/pip (python 2.7)`
       will be shown.  If it refers to version 2, type `pip3 --version` to
       make sure that `pip3` was installed as part of the  `python3` install
       (it should have been).  Then, if you like, you can alias the `pip3`
       following the same approach as python, just replace `python` and 
         `python3` with `pip` and `pip3`.
    
   + **Windows** users have three options:  
     1. Download and install from <https://www.python.org/>.
        * Follow additional guidelines found [here](../Resources/installations.md) for installation.
        * **NOTE:** As of January 7, 2025, the latest version is 3.13.1.  
   
     2. Install Python from Anaconda.
        * You can install either the full Anaconda distribution
          (<https://www.anaconda.com/download/success>) (which will download 
          many commonly used packages and set them up in a base environment)
          or you can install Miniconda 
        (<https://docs.anaconda.com/miniconda/miniconda-install/>) which 
          brings in the bare minimum of packages (RECOMMENDED)
        * Using Anaconda will require you to set-up
   virtual environments somewhat differently than what will be described in 
          class.
     3. Installing and using the [Ubuntu Linux Subsystem](https://docs.microsoft.com/en-us/windows/wsl/about), 
   and running `python` from within that environment.  This approach will give 
   you a legitimate Linux environment, but there is overhead to running GUI 
   applications through an X-server, which adds more complexity and can be 
   slower for complex interfaces.


6. You will want a code writing environment / text editor that makes life 
easier for you as your projects get more complex.  Options include:
   + Terminal Editors
      + [VIM](http://www.vim.org)
      + [nano](https://www.nano-editor.org/)
   + Code / Text editors
      + [Visual Studio Code](https://code.visualstudio.com/)
        (See install and use info at [Resources/visual_studio_code.md](../Resources/visual_studio_code.md)).
      + [Sublime Text](https://www.sublimetext.com/)
      + [Notepad++](https://notepad-plus-plus.org/)
        (See [Resources/Notepad++.md](../Resources/notepad++.md) for set-up
        info and markdown plug-ins)
   + Full-featured IDE (integrated development environment)
     + [PyCharm](https://github.com/dward2/BME547/tree/main/Resources/PyCharm) 
    (professional edition free to use in academic setting, also includes
    Python interpreter).
     + [Spyder](https://www.spyder-ide.org/) (free IDE included with Anaconda)
    
    Check to see if your chosen text editor has the ability (or an extension) to
    edit and render Markdown text.  If so, set that up. 

## Checking Set-up
A GitHub repository has been created with some simple steps for you to follow
to verify that can execute git and Python on your computer.  Please visit
<https://github.com/dward2/setup_verification> and follow the instructions
found there.

## Learning Git
If you really can't wait to get started...
1. Never used git before?  Start with these resources:  
  https://try.github.io/  
  https://www.codecademy.com/learn/learn-git  
  https://www.git-tower.com/learn/cheat-sheets/vcs-workflow  
  http://gitimmersion.com/  
  https://www.atlassian.com/git/tutorials/setting-up-a-repository

1. Familiar with git (or just completed the exercises above)?  Give this a try:
  http://learngitbranching.js.org/

1. Having trouble?  We'll be covering usage of many of these tools in upcoming
  lectures.  

## What We Will Eventually Learn How To Do In Git:
  + Create a git repository on your local computer.
  + Create a local file, then add and commit it to your local repository.
  + Edit your local file, adding and committing those edits.
  + Create a remote repository on GitHub that has the same name as your local repository.
  + Add the remote repository (origin) URL to your local repository.
  + Push your local repository to GitHub.
  + Create a local branch, create/add/commit a new file.
  + Push new local branch to GitHub.
  + Merge new branch on GitHub into main branch on GitHub.
  + Pull the updated main branch into local repository.
