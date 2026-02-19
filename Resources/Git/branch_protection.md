# GitHub Branch Protection

As we have discussed in class, commits should never be made to the `main` branch
of the repository.  GitHub provides some tools to help prevent this from
happening.  Using "Rulesets" we can define what you can and cannot do to some
or all of your branches in GitHub.

In this example, we are going to set our `main` branch so that it will not
accept direct commits, but can only be modified through pull requests.

* Visit the repository of interest in GitHub.
* Click on "Settings".
* In the left-side list, click on "Rules" in the "Code and automation" section.
* Click on "Rulesets" in the sub menu that opens.
* Click on the green "New ruleset" button and then choose "New branch ruleset"
  from the dropdown menu.
* Enter a name in the "Ruleset Name" box.  It could be something like 
  "NoCommitToMain".
* Set the "Enforcement status" to Active.
* Under the "Target branches" heading, in the box called "Branch targeting 
  criteria", click on the "Add target" button, and then select the 
  "Include default branch" item from the dropdown menu.  Your default branch is
  typically your `main` branch unless you changed some settings.
* Under "Branch rules", select the checkbox next to "Require a pull request
  before merging".  
* Scroll to the bottom of the page and click "Create".

Now, if on your local computer you make a commit to the `main` branch, and 
try to push this change up to GitHub, you will get an error similar to the following:

```
remote: error: GH013: Repository rule violations found for refs/heads/main.
remote: Review all repository rules at https://github.com/BME547-Spring2026/my_repo_name/rules?ref=refs%2Fheads%2Fmain
remote:
remote: - Changes must be made through a pull request.
remote:
To github.com:BME547-Spring2026/my_repo_name.git
 ! [remote rejected] main -> main (push declined due to repository rule violations)
error: failed to push some refs to 'github.com:BME547-Spring2026/my_repo_name.git'

```

What you would need to do at this point, is move the new commits off of the
local `main` branch and onto a new feature branch.  You could then push the
new feature branch up to GitHub and open a pull request to merge the feature
branch into the `main` branch.

Instructions for moving local commits from the `main` branch to a new feature
branch can be found at
https://github.com/dward2/BME547/blob/main/Resources/Git/moving_commits_from_main_to_branch.md#mistaken-commits-not-pushed-to-github.

