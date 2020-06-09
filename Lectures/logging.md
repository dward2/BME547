# Logging

Device logs can be invaluable to confirm expected performance and to help debug 
when things go wrong.  Python has a `logging` module that provides rich 
functionality.  Logs can be kept at varying "levels"; more verbose logs can 
provide more information, but at the expense of being much larger and more 
difficult to parse.  Logs typically have more verbose debugging modes compared 
to less descriptive runtime modes.

Standard levels in the logging module include:
* DEBUG
* INFO
* WARNING (default level if not specified)
* ERROR
* CRITICAL

## Steps to Logging
1.  `import logging` must be included in each module in which logging will be
done.  
2.  By default logging will be done to the console.  If you want to log to
a file, add `logging.basicConfig(filename="example.log", level=logging.INFO)` 
where you specify the file name for the log and set the threshold level at
which logging messages are saved to the log file.  This command only needs
to be executed once and does not need to be present in each module.
3.  In code, add logging commands as desired:  
  `logging.debug("String containing desired information and message)`  
  `logging.info("Similar string")`  
  `logging.warning("Similar string")`  
  `logging.error("Similar string")`  
  `logging.critical("Similar string")` 
4.  Be default, when your code finishes and you run it a second time, the 
existing log file will remain and the second run of your program will continue 
to add information to the existing log file.  If you wish for the log file to
start from scratch with each run of your program, modify the 
`logging.basicConfig` command as follows:  
`logging.basicConfig(filename="example.log", filemode="w", level=logging.INFO)`  

## Testing of Logging Functions
See the page [testing_logging.md](../Resources/testing_logging.md) in the
Resources folder for information on writing unit tests for functions that do
logging.


## References
https://docs.python.org/3/howto/logging.html#logging-basic-tutorial

Elegant way to use decorators to clean up the logging syntax: 
https://hackaday.com/2018/08/31/an-introduction-to-decorators-in-python/

