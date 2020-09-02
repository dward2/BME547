# Testing Workflow and Continuous Integration
How should unit testing be integrated into the development work flow?  It could
be run manually by the developer whenever they think to do it.  Ideally, it 
would be done each time a change is made.  And, the tests would be run not just
on the new code, but on all of the existing code to make sure that the new
changes didn't break anything.

A better option would be to automate the testing whenever changes are made.
This also helps when you are collaborating on a code base.  The tests should
be designed so they ensure that the code runs and performs as expected.  
Then, when 
developers add new code to the repository, the existing tests can be used to
ensure that the code that is added meets the desired specifications and works
correctly.  Finally, by having the tests automated, you ensure that everyone
tests their code, and doesn't "forget".  

This type of testing is called Continuous Integration and can be integrated
with the use of GitHub.  We will use a service called Travis CI.  Anytime new
code is pushed into a branch in GitHub, Travis CI will automatically run our
unit tests and give us the results.  In this way, only code that passes the
test can then be merged into the master branch.

## Using Travis-CI
### Enable Travis-CI
* Travis-CI must be enabled for both your GitHub account and for specific repositories.
* Follow the instructions at <https://docs.travis-ci.com/user/tutorial/> to
enable Travis-CI.
  + Note that the instructions will say to go to `travis-ci.com` to sign-up.
 The `.com` version is the pay version.  Go to `travis-ci.org` instead to 
 access the free version.

### Set-up Travis-CI for your repository
In your repository, create a file called `.travis.yml`.  This is the Travis 
configuration file.  It should have the following format:
```
language: python
python:
      - "3.6"
cache:
      - pip
install:
      - pip install -r requirements.txt
script:
      - pytest -v --pycodestyle
``` 
Travis-CI is very finicky with respect to the format of this file.  So, ensure
that your spacing and syntax are exact.
