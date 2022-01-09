# Miscellaneous Git Commands
#### Convention for this page

* anything contained in `<>` should be replaced by the
user with the appropriate information without the `<` or `>`.  For example, 
`git add <filename>` should be entered as `git add textfile.txt`
* anything contained in `[]` should be replaced by the user just as above.
However, including this is optional.
* anything in quotes are generally strings that can be replaced by appropriate
comments by the user.

## Config
#### To set your name and e-mail in local Git configuration. 
`git config --global user.name "Your Name"`

`git config --global user.email "Your e-mail"`

#### To change the default editor used by Git
`git config --global core.editor <editor_name>` where `<editor_name>` can be 
one of the following:
  * `nano` for the nano terminal editor
  * `notebook` for the Notebook app in Windows  
  * `"'C:/Program Files (x86)/Notepad++/notepad++.exe' -multiInst -notabbar -nosession -noPlugin"`
    for Notepad++ on Windows (note, you may need to verify this exact path is)
    the same on your computer.
  * any path that leads to a text editor executible file.  

Visit
<https://docs.github.com/en/github/using-git/associating-text-editors-with-git>  
for examples of setting the default editor to other text editors.  

Also, visit <https://git-scm.com/book/en/v2/Customizing-Git-Git-Configuration> 
for more information on using git config.

#### Changing single repository configurations
Add setting: `git config --local --add <config_variable> <setting>`

Edit setting:  `git config --local --edit <config_variable> <setting>`

Remove setting:  `git config --local --unset <config_variable>`

#### Show all configuration settings
`git config --list --show-origin`  (will show settings from the system, global 
and local configurations)

## Local Repositories

#### Create a new local repository
`git init` from within the desired folder/directory

#### Add a file (new or changed) to the index to be committed to repository
`git add <filename>`

#### Commit changes to the repository
`git commit -m "Commit Message"` only commits files specifically added.

`git commit -am "Commit Message"` to commit changes for all modified files that 
have been previously added to the repository.  

#### Status of repository (to see what files have been added, changed, etc.)
`git status`

#### See changes in files made since the last commit
`git diff` shows all unstaged changes since the last commit

`git diff --staged` shows all staged changes since the last commit

To see changes for only a specific file, add the filename after the commands
above.


#### Add a new branch
`git branch <branchname>`

#### Change to a branch for editing/working
`git checkout <branchname>`

#### Add a new branch and checkout for editing/working
`git checkout -b <branchname>`

#### Display a list of branches
`git branch`

#### Delete a Branch
`git branch -d <branchname>`

#### Rename a local branch
`git branch -m <new-name>` if on the branch.
`git branch -m <old-name> <new-name>` if on a different branch.

#### See list of commits and changes
`git log` for list of commits  
`git log -p` to also include the changes made at each commit.  
`git log --oneline` to show one commit per line  
`git log --graph --oneline` to show log with branches plotted


### Tags
* Check out details on semantic versioning here: http://semver.org
#### Create a tag
`git tag -a v#.# -m "Tag Message"`

#### See a list of tags
`git tag`

#### Show tag information
`git show v#.#`

#### Tag a past commit
`git tag -a v#.# <commitchecksum>` where `<checksum>` is the first few digits
of the commit number.


## Remote Repositories
#### Clone a repository (make a new local copy of an existing GitHub repository)
`git clone git@github.com:<GitHubName>/<RepoName>.git [LocalFolderName]`
where `<GitHubName>` is your GitHub username and `<RepoName>` is the name
of the repository on GitHub.  `[LocalFolderName]` is optional and supplies
the name of the local folder to be created.  If omitted, the `<RepoName>` is
used for the local folder name.  Enter this command in the folder in which
you want to create a subfolder that will contain the git repository.  This
is different than `git init` which you edit within the desired git folder.

For a detailed example of using `git clone` can be found at 
[GitBashFolders](GitBashFolders/GitBashFolders.md)

#### Sending local changes to the linked remote repository
`git push`  
If the local branch doesn't exist on the remote origin, use:  
`git push --set-upstream origin <branchname>`

#### Getting changes from linked remote repository and adding to local repository
`git pull`

#### Linking a local repository to a new and empty GitHub repository
`git remote add origin <repositoryURL>`

#### Verifying link between a local and remote repository
`git remote -v`

#### Pushing local repository to new GitHub repository
`git push -u origin main`

#### Pushing a local tag to GitHub
`git push origin v#.#`

#### Linking local repository to a second GitHub repository
`git remote add <localnickname> <repositoryURL>`  
where `<localnickname>` is a nickname that your local repository will use to
reference this specific remote repository.  The nickname `origin` is the
default for the first linked repository.  You can then substitute 
`<localnickname>` for `origin` in any push/pull commands to send to this second
repository.  Use carefully to make sure you keep the various remote and local
repositories coordinated.

#### Viewing branches in remote repository
`git branch -a`  
will list all local and remote branches

#### Checkout and copy a remote branch to local repository
Let's say you have cloned a GitHub repository as follows:
```
$ git clone git://example.com/myproject
$ cd myproject
```
If we look at the branches in this repository, we will see:
```
$ git branch
* main
```
To see what branches also exist in the remote repository, we type:
```
$ git branch -a
* main
  remotes/origin/HEAD
  remotes/origin/main
  remotes/origin/v1.0-stable
  remotes/origin/experimental
```
To examine the remote branch, you can check it out directly:
```
$ git checkout origin/experimental
```
But, if you want to work on that branch, you need to create a local tracking
branch which can be done by:
```
git checkout experimental
```
Now, if we look at the local branches:
```
$ git branch
* experimental
  main
```
The local `experimental` branch will now track with the remote branch of the 
same name.

#### GitHub Credentials
_**NOTE** This section may become obsolete when GitHub removes the ability to
authenticate with username and password. (This is epxected to happen in 
August 2021)._

If you have a local repository linked to GitHub, and you are having problems
pushing to that repository because of authentication issues, try the following
command:
```
git remote set-url origin https://<GitHubID>:<GitHubPassword>@github/<GitHubID>/<RepositoryName>.git
```
This will store the credentials in the `.git/config` file.
See <https://www.shellhacks.com/git-config-username-password-store-credentials/>
for more info.

## Git Log Options
The following information was taken from 
<https://ma.ttias.be/pretty-git-log-in-one-line/>.  

#### One Line Log
`git log --pretty=oneline`

#### To create a permanent one-line log:
Enter the following command on the git bash command line.
```
git config --global alias.logline "log --graph --pretty=format:'%Cred%h%Creset -%C(yellow)%d%Creset %s %Cgreen(%cr) %C(bold blue)<%an>%Creset' --abbrev-commit"
```
It creates a new git command called `logline` that is used as follows:
```
git logline
```
