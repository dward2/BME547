# Branching

Here is the standard workflow for using feature branches in `git` and GitHub.

#### Initial Commit
First, a new repository is created on GitHub with a README.md file and then  
cloned to the local computer.  The repository has a single commit on the main 
branch:

![network-1.jpg](branching_files/network-1.JPG)

_GitHub Commit History_: ![commit-1.jpg](branching_files/commit-1.JPG)

_git local commit history_:
![gitlog-1.jpg](branching_files/gitlog-1.JPG)


#### First Feature Branch
The first feature branch, in this case called `interface`, is created in `git`  
and checked out with the following commands:
```
git branch interface
git checkout interface
```
On the interface branch, the desired code is added committed.

The local `git` commit history now looks like this:

![gitlog-2.jpg](branching_files/gitlog-2.JPG)

Note:  For information on how to implement this single-line commit log,
go <a href="https://github.com/dward2/BME547/blob/main/Resources/Git/GitCommands.md#git-log-options">here</a>.

Next, this feature branch is pushed to GitHub.  As this branch does not
currently exist on GitHub, the following command is used:
```
git push --set-upstream origin interface
```
The repository on GitHub now shows the `interface` branch and its commit 
history:

![network-2.jpg](branching_files/network-2.JPG)
![commit-2.jpg](branching_files/commit-2.JPG)

On GitHub, a pull request is opened to merge `interface` into `main` and the
merge is completed.  The repository branch network now looks like this:

![network-3.jpg](branching_files/network-3.JPG)

and the main branch now has the commit history:

![commit-3.jpg](branching_files/commit-3.JPG)

Note that the commits from the `interface` branch have been added to the 
`main` branch.

As this merge was done on GitHub, the local repository has no knowledge of this
merge.  So, back in the local repository, the local repository is updated to 
the same status as GitHub by using the following `git` commands.First, the
main branch is checked out.
```
git checkout main
```
Then, `fetch` is used to get the latest status from GitHub and `pull` is used
to pull the latest `main` branch updates into the local repository:
```
git fetch
git pull
```
`git` knows to pull the `main` branch because that is the currently active
branch.  The local git commit history for the local main branch is now:

![gitlog-3.jpg](branching_files/gitlog-3.JPG)

#### Second Feature Branch
A second feature branch, called `calculations` is now made from the `main` 
branch.  Make sure that the `main` branch is currently checked out.  
Then, a new branch is made:
```
git checkout main
git branch calculations
git checkout calculations
```
The git commit history for this new branch is as follows:

![gitlog-3new.jpg](branching_files/gitlog-3new.JPG)

Note that it is exactly the same as `main`.  When a new branch is made, it
retains the commit history of the branch from which it was made.

Now, code and commits are made on this new branch, leading to the following
local git commit history:

![gitlog-4.jpg](branching_files/gitlog-4.JPG)

This new branch is pushed up to GitHub:
```
git push --set-upstream origin calculations
```

So, the GitHub repository now looks like:

![network-4.jpg](branching_files/network-4.JPG)

and the `calculations` GitHub commit history is:

![commit-4.jpg](branching_files/commit-4.JPG)

Again, a pull request and merge is done on GitHub.

![network-5.jpg](branching_files/network-5.JPG)
![commit-5.jpg](branching_files/commit-5.JPG)

And, as before, these changes on GitHub need to be pull back into the local
repository using:
```
git checkout main
git fetch
git pull
```
So that the local git commit history for `main` now looks like:

![gitlog-5.jpg](branching_files/gitlog-5.JPG)

#### Adding to existing branch
Lets say that you added some code to a feature branch and pushed it to GitHub
so that other users can see what you are doing.  You can still make further
additions to that feature branch locally and then push it up to GitHub again,
simply using the `git push` command when the feature branch is active.  Since
GitHub already has the branch defined, you do not need to use the 
`--set-upstream` flag.

#### Best Practice:  Make new feature branches from `main` branch
Whenever you are making a new feature branch, generally create this branch from
the `main` branch.  In this way, if others collaborators have made changes
to the `main` branch, you will be working from the most recent copy.  

Or, shown graphically:

__Good:__

![branching-good](branching_files/branching_good.jpg)

__Bad:__

![branching-bad](branching_files/branching_bad.jpg)  
(In the case above, the user forgot to checkout the main branch after merging
the `test` branch into `main` on GitHub.  So, when they made the `test2`
branch, it was a copy of `test` rather than `main`.)

There may be times when you want to try a different approach to a feature, and 
in that case, it may be okay to branch off of a feature branch.  For example,
let's say you start a branch called `test2`.  You have implemented your feature,
but you think there might be a different way to implement that feature.
Rather than overwrite your first attempt, you want to keep what you have done
and modify it for your second idea.  So, you could make a new branch from 
`test2` called `test2_new_idea`.  And, if

![branch_from_branch_ok](branching_files/branch_from_branch_ok.JPG)

Or, if you prefer the original approach, you could checkout `test2` and merge 
it.

#### Forgetting to pull `main` from GitHub after a merge
As another example, let's say the user successfully creates a branch, pushes
it to GitHub, and merges it on GitHub.  GitHub will see the branches looking
like this:

![first_branch_good](branching_files/first_branch_good.JPG)

Then, in their local repository, the user remembers to check out the main
branch, but forgets to "pull" the merged changes on GitHub.  They then create
a second branch, work on it, push to GitHub, and then merge on GitHub.  The
branches will look like this:

![forget to pull main after first merge](branching_files/forget_to_pull_main_after_first_merge.JPG)

Since they did not pull the merged changes from GitHub after merging the first
branch, the second branch was created from the initial empty repository.  This
is not ideal because you should always be working from the most recent copy
of the files whenever possible.
