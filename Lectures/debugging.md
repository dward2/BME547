# Debugging
## For in-class demo code,  
<!--- click [here](./debugging_code/debug_demo.py).--->  
Clone repository at <https://github.com/dward2/debug_class>

<!---
**Summer 2020**
Class code at <https://github.com/dward2/debug_demo>
--->

## Debugging Strategies

### Understand the bug
* What did you expect your code to do?
* What happened instead?

__The Principle of Confirmation__ [1]
> Fixing a buggy program is a process of confirming, one by one, that the many 
> things you believe to be true about the code actually are true. When you 
> find that one of your assumptions is not true, you have found a clue to 
> the location of the bug.

[1] Matloff, N., Salzman, P.J., The Art of Debugging with GDB, DDD, and 
Eclipse, 2008

### Reproduce your bug
* Make sure the bug occurs consistently and whether it is dependent on certain
inputs or conditions.
* Write a unit test that demonstrates the bug.  Can be used to prove that you
have fixed it.

### Examine your assumptions
* Verify the content of variables.  Don't assume what they contain.
* Check carefully for typos.  Don't assume you know what a line of code
actually contains.
* Did you make a change to your code recently that you _assume_ is unrelated 
to the problem you are seeing?
  
### Determine the location of error/fault
* Step through your code in debug mode and see where the problem first occurs.
* Use a top-down approach.  Step over your high level function calls and make
sure each one returns the expected results.  When you find where things start
  to diverge from expected, then you can step into that function to look for
  the exact spot of divergence.

## Debuggers
Debuggers are programs that help you find errors (bugs) in your code.  They
are usually part of an "integrated development environment" (IDE) that also
contains a code editor and other development tools.  The debugger allows you
to watch your code execute line-by-line while observing the value of the 
variables in the code.  This allows you to see the flow of your program and
the results of its calculations.

IDE's with debugging features include 
[PyCharm](../Resources/PyCharm/readme.MD), 
[Visual Studio](https://visualstudio.microsoft.com/), 
[Visual Studio Code](../Resources/visual_studio_code.md), and 
[Spyder](https://www.spyder-ide.org/).  

Python installations come with a simple IDE with debugger called IDLE
(<https://docs.python.org/3/library/idle.html>) that provides a basic GUI for
code editing and debugging.  

In the Python standard library, there is a module called `pdb` that can be used 
for debugging, primarily from the command line (see below).  There is also a 
terminal-based debugger called `pudb` which can be installed in your 
environment and provide an easier-to-use graphical interface directly in the
terminal window.  `pudb` works on macOS/Linux only.  Both of these debuggers
work by the developer adding breakpoints directly in the code.

## pdb
* Python has a built in debugging package called `pdb`.
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


