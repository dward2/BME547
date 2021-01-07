# Testing Workflow and Continuous Integration
How should unit testing be integrated into the development work flow?  It could
be run manually by the developer whenever they think to do it.  Ideally, it 
would be done each time a change is made.  And, the tests would be run not just
on the new code, but on all of the existing code to make sure that the new
changes didn't break anything.

A better option would be to automate the testing whenever changes are made.  
The tests should be designed so they ensure that the code runs and performs as 
expected.  Then, when developers add new code to the repository, the existing 
tests can be used to ensure that the code that is added meets the desired 
specifications and works correctly.  This increases confidence that frequent 
code changes can be made while maintaining code quality.  Finally, by having 
the tests automated, you ensure that everyone tests their code, and doesn't 
"forget".  These considerations are especially important when you are 
collaborating on a code base.    

This approach of frequent code updates and testing is called Continuous 
Integration and Testing can be integrated with the use of GitHub.  GitHub
Actions provides the ability to automate certain tasks.  We can automate the
running of our tests everytime new code is pushed into a branch in 
GitHub and/or when a pull request is made.  By ensuring that these automated
tests pass before doing amy merges, we can make sure code added to the main
branch has been tested and met quality control.

## Using GitHub Actions
### Create a testing action
1. Create a folder in your repository called `.github\workflows`.
2. In that folder, create a file with the extension.yml.  You can name this
file anything, but I might suggest `pytest_runner.yml`.
3. Add the following to this file:
```yaml
name: Pytest with Pycodestyle

on: [push, pull_request]

jobs:
  build:
    runs-on: ubuntu-latest
    steps:
    - uses: actions/checkout@v2
    - name: Set up Python 3.8
      uses: actions/setup-python@v2
      with:
        python-version: '3.8'
    - name: Install dependencies
      run:  pip install -r requirements.txt
    - name: Test with pytest
      run:
        pytest -v --pycodestyle

```
A brief description of the file above:
* `name` is the name of the GitHub action you are creating and will be 
shown on the GitHub website.  Can be anything.  The use of `name` under the
`steps` title simply provides a string to include in the run output describing
what each step does.  Can be anything.
* `on` indicates what repository actions will trigger this action.  In the 
above example, `push` means that any push of commits to GitHub will trigger
this action while `pull_request` means that the creation of a pull request
will trigger the action.  If you only want to run it on pull requests, simply
remove `push` from the list
* `runs-on` indicates the type of virtual machine that will be used for this
testing.  Please keep this as `ubuntu-latest`.
* `uses` defines the actions to take to set up a virtual environment
  + `actions/checkout@v2` calls a standard action that checks out or clones
    your repo to the virtual machine
  + `actions/set-up python@v2` calls a standard action to set-up a Python
    operating environment on the virtual machine
    - `with:`
      `python-version` indicates the specific Python version to be used.
      Change the 3.8 to a different version if needed.
* `run` gives the specific commands to run in the virtual environment
  + `pip install -r requirements.txt`
  + `pytest -v --pycodestyle`
  
The above configuration file can be used as is.
  

### conda users
While you use `conda` for creating virtual environments on your local computer,
the GitHub action described above uses `pip` for package installation in its 
virtual environments.  So, even though you will not use a `requirements.txt` 
file locally, you will need to create one for use in your repository so 
the GitHub action can create the 
proper virtual environment.  