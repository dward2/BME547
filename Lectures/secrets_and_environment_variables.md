# Secrets and Environment Variables

Often in our code, we are making connections to outside services such as an
e-mail server, MongoDB database, or other cloud services. We often need to
authenticate ourselves with those services, requiring a password or key to
exist in our code. As an example, our MongoDB connect string contains a
database username and password. If using a public repository, having a key or
password directly in our code exposes that key or password to the world and
others would have undesirable direct access to our accounts and/or databases.

It could be possible to just remove those keys or passwords from the code
before pushing the code to GitHub. But, you have to remember to make those
changes each time. We could move the passwords and keys to a different password
module and then import that module into our code for access to the passwords.
Then, if we do not commit the password module to the repository, it would not
exist on GitHub. The problem with this approach is that if we then have unit
tests that needs to access that service to run, our GitHub Actions tests will
fail.

Luckily, there is a way that we can share "secrets" with GitHub so that GitHub
Actions can access passwords and keys for the testing of code in our public
repository without our passwords and keys being shared with the public. This is
done through the use of GitHub Secrets and environment variables.

## Environment Variables

Environment variables are variables that are stored outside of any particular
program or application and are typically stored and made available by the
computer operating system. The developer can set the content of these variables
through the operating system and then these variables can be made available to
a code or application. In this way, the content of that variable can be made
available to many applications and programs, and can be changed in a single
location with the change then available to all of the users of the variable.

### Setting an Environment Variable in Windows

1. Click on the start menu and type "Environment Variables". An option called "
   Edit the environment system variables" will display. Select that option. A "
   System Properties" window will open.
2. In the "System Properties" window, click on the "Environment Variables..."
   button in the lower right. An "Environment Variables" window will open.
3. In the "Environment Variables" window, click the "New..." button in the pane
   called "User variables for <user_id>" where <user_id> will be your user name
   on the computer. A "New User Variable" window will open.
4. In the "New User Variable" window, enter a variable name and variable value.
   For example, a variable name could be `MONGODB` and the variable value could
   be `my_password`.
5. Click `Ok` to close the "New User Variable" window.
6. Click 'Ok' to close the "Environment Variables" window.
7. Click 'Ok' to close the "System Properties" window.
8. Close and re-open any existing terminal windows for the new environment
   variable to take effect.

### Setting an Enviornment Variable in macOS

1. Open a terminal window.
2. Enter `cd ~` to ensure that you are in your home directory.
3. Depending on your terminal type, you will need to complete the following
   steps for one of the files: `.bash_profile` or `.zshrc`.
4. Open the file in an editor.  (You may need to open the editor in 
   administrator mode.  If opening from the command line, use `sudo` such 
   as `sudo nano .zshrc`. )
5. Scroll to the end.
6. Add this line:  `export <VAR_NAME>=<VAR_VALUE>` where you replace 
   `<VAR_NAME>` and `<VAR_VALUE>` with the name and value of the variable.  
   Example:  `export MONGODB=fall24`.
7. Save the file and close it.
8. Close and re-open any existing terminal windows for the new environment 
   to take effect.  

### Access Environment Variables in Python
Example:
```python
import os

mongodb_pswd = os.environ.get("MONGODB")

connect("mongodb+srv://dward2:{}.ba348.mongodb.net/".format(mongodb_pswd) + 
        "myFirstDatabase?retryWrites=true&w=majority")
```

## Secrets on GitHub

### Create a Secret on GitHub Actions
Follow the instructions at https://docs.github.com/en/actions/security-for-github-actions/security-guides/using-secrets-in-github-actions#creating-secrets-for-a-repository

### Accessing the Secrets in GitHub Actions
Modify the workflow file found in the `.github/workflows` directory.  The 
example file we have previously used has been called `pytest_runner.yml`.
Modify the section that runs `pyetst` as follows:
```
    - name: Test with pytest
      env:
        <ENV_VAR_NAME>: ${{ secrets.<VAR_NAME_SECRETS> }}
      run:
        pytest -v --pycodestyle    
```
Replace `<ENV_VAR_NAME>` with the environment variable name that your 
Python code is looking for (`MONGODB` in the examples above).  Replace 
`<VAR_NAME_SECRETS>` with the GitHub Secrets name you created (also 
`MONGODB` in the examples above).
