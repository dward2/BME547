#Scope
The scope of a variable is the area in the code in which this variable
is accessible.  

A variable which is defined within a function is a **local** variable whose scope is limited to that function.  It will not be accessible
outside of the function.

A variable which is defined outside of a function is a **global** variable and
will be accessible anywhere in the module.

### Example of Local Variable
__Module Code:__
```
1   def variable_definition():
2       a = 5
3       b = "Hello"
4       print("a defined as {} in variable_definition".format(a))
5       print("b defined as {} in variable_definition".format(b))
6       return
7
8   def variable_output():
9       print("a has the value of {} in variable_output".format(a))
10      print("b has the value of {} in variable_output".format(b))
11      return
12
13  variable_definition()
14  variable_output()
```
__Output when module code above is run:__
```
a defined as 5 in variable_definition
b defined as Hello in variable_definition
Traceback (most recent call last):
  File "D:/ClassRepos/BME547/mysandbox.py", line 17, in <module>
    variable_output()
  File "D:/ClassRepos/BME547/mysandbox.py", line 10, in variable_output
    print("a has the value of {} in variable_output".format(a))
NameError: name 'a' is not defined
```
__Description:__

When this module is run in Python, the interpreter starts at the top of the 
file and see that a function called `variable definition` is defined and then
a function called `variable_output` is defined.  Then, it comes to line 13 with
a statement in the module which it will execute.  This statement will run the
`variable_definition()` functionat line 1.  This function defines local 
variables `a`
and `b` and then prints out some strings using these variables.  This function
ends and control is returned to line 13 where the function was called.  
Next, Python sees the `variable_output{}` statement in line 14, so runs that
function back at line 8.  This function tries to print the variable `a`.  This
variable does not exist in this function.  There was an `a` defined in 
`variable_definition`, but it was local to that function and does not exist
in other functions.  The program stops with an error.

### Example of Global Variables
__Module Code:__
```
1   def variable_output():
2       print("a has the value of {} in variable_output".format(a))
3       print("b has the value of {} in variable_output".format(b))
4       return
5
6   a = 10
7   b = "Goodbye"
8   variable_output()
```
__Output when module code above is run:__
```
a has the value of 10 in variable_output
b has the value of Goodbye in variable_output
```
__Description:__

When this module is executed, the Python interpretor starts at the top of the
file.  It sees that `variable_output` is defined as a function and then 
comes across line 6 with some code to execute.  First, it defines two variables
called `a` and `b`.  As these variables are defined at the module level outside
of a function, they are considered global variables.  They are accessible
anywhere within the code.  Next, the code reaches line 8 which calls the 
function `variable_output` at line 1.  When this function tries to run at line
2, it looks for the variable `a`.  Since `a` is a global variable, it finds
its value and prints it.  This program runs successfully.

Note:  Global variables can be defined anywhere in the module.  Often, they 
are defined at the top of the module before any functions are defined.

### Example of Conflicts Between Local and Global Variables
__Module Code:__
```
1   def variable_definition():
2       a = 5
3       b = "Hello"
4       print("a defined as {} in variable_definition".format(a))
5       print("b defined as {} in variable_definition".format(b))
6       return
7
8   def variable_output():
9       print("a has the value of {} in variable_output".format(a))
10      print("b has the value of {} in variable_output".format(b))
11      return
12
13  a = 10
14  b = "Goodbye"
15  variable_definition()
16  variable_output()
```
__Output when module code above is run:__
```
a defined as 5 in variable_definition
b defined as Hello in variable_definition
a has the value of 10 in variable_output
b has the value of Goodbye in variable_output
```
__Description:__

When the module code is run, the Python interpreter starts at the top of the
file.  It sees the definition of `variable_definition` in lines 1-6.  It then
sees the definition of `variable_output` in lines 8 through 11.  Then, it
comes across code in line 13.  It assigns values to `a` and `b` as global
variables.  Then, in line 15, the code calls the function `variable_definition`.
In line 2, the function `variable_definition` defines a local variable called
`a`.  This local variable has precendent over the global variable `a`.  The
same goes for the `b` variable.  So, when the function prints `a` and `b` in 
lines 4 and 5, it uses the values of the local variables.  The function ends
and control is returned to line 15.  At this point, the local variables `a` and
`b` defined in `variable_definition` no longer exist and the global variables
`a` and `b` continue to have their assigned values of `10` and `"Goodbye"`.
The next line, line 16, calls the `variable_output` function.  In line 9, this
function prints the `a` variable.  Since no local variable is defined as `a`,
it uses the global variable `a`.

### Use of `glabal` to Modify Global Variables 
In the example above, when a local function assigns a value to a variable with
the same name as a global variable, it creates a new local variable of the same
name and does not change the value of the global variable.  

Lets say we did want for a local function to modify the global variable instead
of creating a local variable.  The `global` keyword allows this to happen. 
The `variable_definition` function could be modified as follows:
```
def variable_definition():
    global a, b
    a = 5
    b = "Hello"
    print("a defined as {} in variable_definition".format(a))
    print("b defined as {} in variable_definition".format(b))
    return
```
The `global` keyword tells the function that `a` and `b` are global variables,
and so any use of those variables will impact the global variable, rather than
create a local variable.  The output for this modified code is as follows:
```
a defined as 5 in variable_definition
b defined as Hello in variable_definition
a has the value of 5 in variable_output
b has the value of Hello in variable_output
```


