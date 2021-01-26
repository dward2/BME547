# SSH and GitHub

SSH protocol can be used to authenticate with GitHub.  Basic instructions for
setting up SSH authentication between git and GitHub can be found at 
<https://docs.github.com/en/free-pro-team@latest/github/authenticating-to-github/connecting-to-github-with-ssh>

If this is the first time using SSH keys and GitHub, you probably
only need to follow the steps

<a href="https://docs.github.com/en/free-pro-team@latest/github/authenticating-to-github/generating-a-new-ssh-key-and-adding-it-to-the-ssh-agent">
Generating a new SSH key and adding it to the ssh-agent</a><br>

<a href="https://docs.github.com/en/free-pro-team@latest/github/authenticating-to-github/adding-a-new-ssh-key-to-your-github-account">
Adding a new SSH key to your GitHub account</a><br>

<a href="https://docs.github.com/en/free-pro-team@latest/github/authenticating-to-github/testing-your-ssh-connection">
Testing your SSH connection</a><br>

On Windows, to avoid needing to enter your SSH passphrase every time it is 
needed, see the instructions at https://docs.github.com/en/github/authenticating-to-github/working-with-ssh-key-passphrases#auto-launching-ssh-agent-on-git-for-windows

## Support for multiple ssh keys with GitHub
If you have multiple GitHub accounts, and you want to set up your GitBash to
work with more than one, follow these instructions.

1. Create SSH keys for each GitHub account following the instructions above.
   Make sure that you have a different e-mail associated with each GitHub
   account.  Also, when asked to enter a file in which to save the key, make
   sure you use different file names for each GitHub account, and you know 
   which file goes with which account. 
   
2. Enter the `.ssh` folder by typing: `cd ~/.ssh/`

3. Create a file called `config` in this folder.  Add content as follows:
    ```
    Host acct1.github.com
      HostName github.com
      PreferredAuthentications publickey
      IdentityFile ~/.ssh/key_file_for_acct1
      
    Host acct2.github.com
      HostName github.com
      PreferredAuthentications publickey
      IdentityFile ~/.ssh/key_file_for_acct2
    ```
    Replace `acct1` and `acct2` with some short-hand identification that
    differentiates the accounts (example, work vs personal).  Replace 
    `key_file_for_acct1` and `key_file_for_acct2` with the names of the files 
    generated in step 1 above.  Save this `config` file.

4.  Close and restart your GitBash window.
5.  Enter `ssh-add -l` to list your existing ssh keys.  If you do not see 
    one or both of these keys, you can add them with 
    `ssh-add ~/.ssh/key_file_for_acct`.
6.  Check your connections via:
    ```
    ssh -T git@acct1.github.com
    
    ssh -T git@acct2.github.com
    ```

When cloning a repository, use the ssh URL which will look something like
`git@github.com:github_id/repo_name.git`.  In my experience, GitBash will then
try to authenticate with the first ssh key in your config file.  If you need
to authenticate with the other ssh key, change the ssh URL as follows:
`git@acct2.github.com:github_id/repo_name.git`

The above information was taken from 
<https://coderwall.com/p/7smjkq/multiple-ssh-keys-for-different-accounts-on-github-or-gitlab>.
Refer to that sight for more information or troubleshooting help.

