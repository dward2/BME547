# Debugging
## pdb
* Python has a built in debuging package called `pdb`.
* Reference: https://docs.python.org/3/library/pdb.html
* Provides debugging functions primarily on the command line
* Can install breakpoints to halt code and inspect variables
## pudb
* Add-on package to provide improved interface for debugging.
* Reference: https://documen.tician.de/pudb/index.html
* Can still be used in a terminal environment, so good for remote debugging
with servers
* Only available on Mac/Linux.
* Install `pudb`
* `import pudb`
* Add code `pudb.set_trace()` to set a breakpoint.
* Will halt execution and allow for inspection of variable space.
* Can step through code line by line
* `!` brings up a command line interface or IPython interface (based on the
settings in the Ctrl-P preference window)
* `?` brings up help menu
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

  