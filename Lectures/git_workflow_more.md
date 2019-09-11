# Git Workflow: Part 2
## Tags
Check out details on semantic versioning here: http://semver.org
#### Create a tag
`git tag -a v#.# -m "Tag Message"`

#### See a list of tags
`git tag`

#### Show tag information
`git show v#.#`

#### Tag a past commit
`git tag -a v#.# <commitchecksum>` where `<checksum>` is the first few digits
of the commit number.

#### Pushing a local tag to GitHub
`git push origin v#.#`

#### Push all local tags to GitHub
`git push origin --tags`

## Issues
GitHub repositories has a feature for tracking Issues.  Issues can be used for:
* Creating a To Do list of things to do for code development
* Keeping a bug list
* Asking for input or help

### Using Issues To Ask For Help
* Make sure the person you want to communicate with is a collaborator on your
repository.
* Whenever possible, you should reference specific code in your questions.
* __Starting a New Issue__
  - Navigate to the Code in GitHub you have a question about.
  - Click on the line number of the first line of code you want to reference.
  - If you want to reference more than one line of code, hold down the shift
    key and then click on the last line you want to reference.
  - Click on the `...` to the left of the first line of code selected.
  - Choose `Reference In New Issue` from the context menu.
  - A new issue form will open.  Enter a title.
  - Add your additional comments and question below the permalink that was 
    placed in the "Write" section.
  - Select the person you want to communicate with in the "Assignees" area.
  - Click on "Submit New Issue"
* __Adding Code Permalink To Existing Issue__
  - Follow the same steps as above under "Starting a New Issue", up to the
    "Click on the `...`" step.
  - At the `...`, select the `Copy Permalink` option.
  - Navigate to your existing Issue.
  - Paste the permalink into a new comment of your issue.
  - Select the person you want to communicate with in the "Assignees" area, if
    not already selected.
  - Click on the green "Comment" button.
 * In both cases above, an e-mail notification will be sent to the Assignees
 of the Issue.   
 
### Linking Commits and Pull Requests to Issues
In order to track what work is being done on issues, they can be referred to in
commit and merge messages.  For example, if you want to link a particular
commit to issue #2, you would include a reference to #2 in your commit message.
For example, `git commit -m "Temporary fix of image bug (#2)'`.

If you want to close an issue that has been completed with a commit or a 
pull request merge, include `(Close #2)` in the commit or merge message.
