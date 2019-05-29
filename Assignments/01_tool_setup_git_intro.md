# Assignment 01: Setup Course Tools & Git Introduction

## Getting Setup
1. Create an account on GitHub (https://github.com).  An understandable and
professional user name is suggested.      

2. To communicate your GitHub user name to us, you will open a GitHub issue 
with that information.  
  a)  Go into the BME547 repository (<https://github.com/dward2/BME547>) and 
  click on "Issues" in the tab bar at the top of the page.  
  b) Click on the green "New issue" button.  
  c) In the title, enter your name and the GitHub user name you created. For 
  example, "David Ward - dward2".  
  d) In the comment area, please include your Duke e-mail address.  
  e) Click the green "Submit new issue" button.  

3.  a) Create a new repository with a name such as "Intro".  Make sure to select
the "Initialize this repository with a README" check box.  
  b) With the repository open, click on the README.md file and then click on 
  the pencil in order to edit the file.  
  c) With two classmates, exchange URLs for your repositories.  The URL should
  look something like https://github.com/git_hub_user_name/repo_name.  
  d) In the README file, add these two URLs.  
  e) At the bottom of the page, click on the green "Commit changes" button.  
  You should now active links to two other repositories.
    
4. Download and install `git` at https://git-scm.com.  We will be using 
`Git Bash`, *not* a GUI client.  
  
   For MAC users, `git` is likely already installed.  Open a Terminal window
and type `git --version`.  If you see a version number, it is already
installed.  If not, you will need to download it from the site above.

   Windows users have two options:   
   a) install from the above website (recommended) which will install the
   GitBash command window, or  
   b) use the Windows Subsystem for Linux 
([Ubuntu Linux Subsystem (Windows 10)](https://docs.microsoft.com/en-us/windows/wsl/about)) 
with Ubuntu allowing you to access `git` through Linux.  
Note - this second option does not installed `git` in your Windows environment, 
so other Windows applications that have `git` hooks will not work.

3. [**Optional**]  Setup an SSH key to seamlessly push/pull to/from your GitHub repositories:
   https://help.github.com/articles/connecting-to-github-with-ssh/

4. Download and install `python3` at https://www.python.org/. Be sure to
   install Python 3.6 or 3.7, *not* Python 2.7.  
   
   For Mac users, Python is likely already installed.  Open a Terminal window 
   and enter `python` or `python3`.  If installed, you should see something
   like the following:
   ```
   Python 3.6.5 (default, Apr  1 2018, 05:46:30)
   [GCC 7.3.0] on linux
   Type "help", "copyright", "credits" or "license" for more information.
   >>>
   ```
   If the version number is 3.6 or higher, you are fine.  Type `quit()` to 
   exit.  If python does not start, you will need to download it.
     
   Windows users have two options:  
   a) [**Preferred**] Install Anaconda Python from 
   https://www.anaconda.com/download.  Using "vanilla" Python on Windows can 
   have challenges with importing some packages, such as `numpy`, which do not 
   exist in compiled wheels for Windows.  You can download the complete 
   Anaconda package or Miniconda which brings in the bare minimum of packages 
   and then install what is necessary in virtual environments, but each project 
   will require more download overhead.  
   b) Installing and using the [Ubuntu Linux Subsystem (Windows 10)](https://docs.microsoft.com/en-us/windows/wsl/about), 
   and running `python3` from within that environment.  This approach will give 
   you a legitimate Linux environment, but there is overhead to running GUI 
   applications through an X-server, which adds more complexity and can be 
   slower for complex interfaces.

5. You will want a code writing environment / text editor that makes life 
easier for you as your projects get more complex.  Options include:
  + Terminal Editors
    + [VIM](http://www.vim.org)
    + [nano](https://www.nano-editor.org/)
  + Code / Text editors
    + [GitHub Atom](https://atom.io/)
    + [Visual Studio Code](https://code.visualstudio.com/)
    + [Sublime Text](https://www.sublimetext.com/)
    + [Notepad++](https://notepad-plus-plus.org/)
  + Browser-based Interactive
    + [Jupyter Lab](https://jupyterlab.readthedocs.io/en/latest/#)
  + Full-featured IDE (integrated development environment)
    + [PyCharm](https://github.com/dward2/BME547/tree/master/Resources/PyCharm) 
    (professional edition free to use in academic setting)

## Learning Git
1. Never used git before?  Start with these resources:  
  https://try.github.io/  
  https://www.codecademy.com/learn/learn-git  
  https://www.git-tower.com/learn/cheat-sheets/vcs-workflow  
  http://gitimmersion.com/  
  https://www.atlassian.com/git/tutorials/comparing-workflows#feature-branch-workflow

1. Familiar with git (or just completed the exercises above)?  Give this a try:
  http://learngitbranching.js.org/

1. Having trouble?  We'll be reviewing some of these tools in lecture on
  Wednesday.  

## Learning Objectives:
  + Create a git repository on your local computer.
  + Create a local file, then add and commit it to your local repository.
  + Edit your local file, adding and committing those edits.
  + Create a remote repository on GitHub that has the same name as your local repository.
  + Add the remote repository (origin) URL to your local repository.
  + Push your local repository to GitHub.
  + Create a local branch, create/add/commit a new file.
  + Merge new local branch commit(s) into local master.
  + Push updated master branch to GitHub.
