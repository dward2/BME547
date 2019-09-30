# Debugging
## pdb
* Python has a built in debuging package called `pdb`.
* Reference: https://docs.python.org/3/library/pdb.html
* Provides debugging functions primarily on the command line.
* Can install breakpoints to halt code and inspect variables.
## pudb
* Add-on package to provide improved interface for debugging.
* Reference: https://documen.tician.de/pudb/index.html
* Can still be used in a terminal environment, so good for remote debugging
with servers.
* Only available on Mac/Linux.
* Install `pudb` in virtual environment.
* `import pudb`
* Add code `pudb.set_trace()` to set a breakpoint.
* Will halt execution and allow for inspection of variable space.
* Can step through code line by line
* `!` brings up a command line interface or IPython interface (based on the
settings in the Ctrl-P preference window)
* `?` brings up help menu
* `n` steps through the code, but does not enter functions (equivalent to 
       "step over").
* `s` steps through the code and enters functions (equivalent to "step in")
* `o` shows output in the console window.  Hit `enter` to return to debugger.
#### Example Code
```python
import pudb

def main():
    a = 5
    b = 6
    c = a * b
    pudb.set_trace()
    print_me(c)
    return c

def print_me(c):
    print(c)

if __name__ == "__main__":
    main()
```
* The `pudb.set_trace()` command could be put into an `if` statement if you 
only want the code to stop at certain times or conditions.  For example, in
loop below, the code will stop only when the loop is on the iteration with
`i` equal to 5 so you can only check that particular iteration.
```
for i in range(10):
    print(i)
    if i == 5:
        pudb.set_trace()
    do_math_on_i(i)
```
* Or, if you want the ability to set breakpoints and use them some of the 
time and not all of the time, you could set them up in `if` statements as
follows:
```python
import pudb
debug = True

def do_math(i):
    if debug:
        pudb.set_trace()
    # code here to do some math
    return answer
```
* In the code above, when you want to run your code with breakpoints, you set
the `debug` variable to `True`.  When you do not want the breakpoints to be
active, you set the `debug` variable to `False`.  In this way, you do not need
to be entering and deleting breakpoints.
* For the ability to hit `ctrl-C` to stop a program at any time and debug the
code from there, add the following lines at the top of the code:
```
import pudb
pudb.set_trace(paused=False)
```


For in-class demo code, click [here](./debugging_code/debug_demo.py).

  