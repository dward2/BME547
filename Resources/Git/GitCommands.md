# Miscellaneous Git Commands
#### Convention for this page

* anything contained in `<>` should be replaced by the
user with the appropriate information without the `<` or `>`.  For example, 
`git add <filename>` should be entered as `git add textfile.txt`
* anything contained in `[]` should be replaced by the usre just as above.
However, including this is optional.
* anything in quotes are generally strings that can be replaced by appropriate
comments by the user.
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
`git diff` for all files, or `git diff <filename>` for a specific file.

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

### Tags
#### Create a tag
`git tag -a v#.# -m "Tag Message"`

#### See a list of tags
`git tag`

#### Show tag information
`git show v#.#`

#### Tag a past commit
`git tag -a v#.# <commitchecksum>` where `<checksum>` is the first few digits
of the commit number.

### Config
#### To set your name and e-mail for use in local Git
`git config --global user.name "Your Name"`
`git config --global user.email "Your e-mail"`






## Remote Repositories
#### Clone a repository (make a new local copy of an existing GitHub repository)
`git clone https://github.com/<GitHubName>/<RepoName>.git [LocalFolderName]`
where `<GitHubName>` is your GitHub username and `<RepoName>` is the name
of the repository on GitHub.  `[LocalFolderName]` is optional and supplies
the name of the local folder to be created.  If omited, the `<RepoName>` is
used for the local folder name.  Enter this command in the folder in which
you want to create a subfolder that will contain the git repository.  This
is different than `git init` which you edit within the desired git folder.

For a detailed example of using `git clone` can be found at 
[GitBashFolders](GitBashFolders/GitBashFolders.md)

#### Sending local changes to the linked remote repository
`git push`

#### Getting changes from linked remote repository and adding to local repository
`git pull`

#### Linking a local repository to a new and empty GitHub repository
`git remote add origin <repositoryURL>`

#### Verifying link between a local and remote repository
`git remote -v`

#### Pushing local repository to new GitHub repository
`git push -u origin master`

#### Pushing a local tag to GitHub
`git push origin v#.#`


