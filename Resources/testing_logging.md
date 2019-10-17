# Unit Testing of Functions that Create Log Entries
Assume you have a function `log_if_negative` in a module `my_functions.py` 
that creates a log entry if an input is negative:
```
# my_functions.py
import logging

def log_if_negative(a):
    if a < 0:
        logging.info("a is a negative number")
```

In order to test that this function correctly outputs to a log, we can use a 
package called `testfixtures`
(https://testfixtures.readthedocs.io/en/latest/logging.html).  

First, include `testfixtures` in your virtual environment.

Next, write a test function to capture that the logging occurred as expected.

```
# test_my_functions.py
from testfixtures import LogCapture

def test_log_if_negative_is_made():
    from my_functions import log_if_negative
    with LogCapture() as log_c:
        log_if_negative(-1)
    log_c.check(("root", "INFO", "a is a negative number"))
    
```
+ `from testfixtures import LogCapture`  
   imports the function `LogCapture()` that will capture log entries created
   during the test.

+ `with LogCapture() as log_c:`  
   any log entries created in this`with` code block will be captured in the 
   variable `log_c`.  This variable can have any name you choose.  Include the
   call to the function you want to test for log entries inside this `with`
   block.
   
+ `log_c.check( ("root", "{LogLevel}", "{LogMessage}") )`  
   After the `with` block, you can `check` that the expected log message was
   created.  The `check` function expects a three membered tuple.  The first 
   member is "root".  The second member is the expected log level (DEBUG, INFO,
   WARNING, etc.).  The third member is the expected log message.  If you
   expect more than one log entry, you may enter multiple tuples.  If the
   `check()` function does not find the expected log entry, it will raise
   an assertion error, causing pytest to indicate a failure.  You do not need
   an `assert` statement in this test.
   
   
__NOTE__: The test function above can be used to verify that a log entry was
made when it was supposed to be made.  Unfortunately, it cannot be used to 
verify that a log entry is not made when one should not be made.  That check
must be done in a separate function such as follows:

```
def test_log_if_negative_is_not_made():
    from my_functions import log_if_negative
    with LogCapture() as log_c:
        log_if_negative(2)
    log_c.check()
```
+ In this case, the `check()` function is not sent any parameters, so we
are not expecting any log_entries.  If there are no log entries, the test will
pass.  If there are log entries, the test will fail.

See the `testfixtures` documentation at 
<https://testfixtures.readthedocs.io/en/latest/logging.html> for more info.