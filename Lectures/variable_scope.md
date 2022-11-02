# Scope
The scope of a variable is the area in the code in which this variable
is accessible.  It's scope is defined by where the variable is initially
created (using an assignment statement such as `count = 5` or 
`name_list = ["Apple", "Banana"]`).

A variable which is created within a function is a **local** variable whose 
scope is limited to that function.  It will not be accessible outside of the 
function.

A variable which is created and assigned outside of any function is a 
**global** variable and can be accessible anywhere in the module, including
functions.

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
file and sees that a function called `variable definition` is defined and then
a function called `variable_output` is defined.  Then, it comes to line 13 with
a statement in the module which it will execute.  This statement will run the
`variable_definition` function at line 1.  Lines 2 and 3 create and assign
variables `a` and `b`.  Since they are created inside this function, they are
*local* variables and their scope is limited to this function.  The function 
then prints out some strings using these 
variables.  This function ends and control is returned to line 13 where the 
function was called.  After the `variable_definition` function ends, the 
*local* variables `a` and `b` no longer exist.

Next, Python sees the `variable_output{}` statement in line 14, so runs that
function back at line 8.  This function tries to print the variable `a`.
First, Python looks at the local scope of this function and does not find any
variables in the local scope named `a`.  Python then looks at the global scope a
nd does not find any global variables named `a`.  While there was previously
a variable `a` defined 
in the `variable_definition` function, it was local to that function and 
does not exist outside of that function.  Therefore, the program stops with a 
`NameError` since no variable named `a` exists in the current scope.

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

When this module is executed, the Python interpreter starts at the top of the
file.  It sees that `variable_output` is defined as a function and then 
comes across line 6 with some code to execute.  First, it defines two variables
called `a` and `b`.  As these variables are created and assigned a value at the 
module level outside
of a function, they are considered *global* variables.  They are accessible
anywhere within the code.  Next, the code reaches line 8 which calls the 
function `variable_output` at line 1.  When this function tries to run at line
2, it looks for the variable `a`.  It firsts looks for a *local* variable `a`,
and when it doesn't find one, it will look for and find the *global* variable
`a`.  It will use this global variable in the
`print` statement.  The same occurs for line 3 and the `b` variable.  This 
program runs successfully.

Note:  Global variables can be defined anywhere in the module.  Usually, they 
are defined at the top of the module before any functions are defined.  But,
they must be defined before they are used in the flow of the code. For example,
in the code immediately above, the `a` and `b` variables are defined in the
flow of the operating program before they are needed in the call to the 
`variable_output` function.  

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
comes across code in line 13.  It creates a variable `a` and assigns it the
value of `10`.  On line 14, the
variable `b` is then created and and assigned the string value of `"Goodbye"`.
Since these variables were created outside of a function, they are considered
*global* variables.

Then, in line 15, the code calls the function `variable_definition`.  On line 
2, the code creates and assigns the value of `5` to the variable `a`.  Since
this creation and assignment is happening inside a function, a new *local*
variable `a` is created.  Line 3 also creates a new *local* variable `b`.
Next, lines 4 and 5 are executed that need the variables `a` and `b` for
printing.  Python first looks for *local* variables, and finds local versions
of `a` and `b` and therefore prints the values of `5` and `"Hello"`.
The function ends
and control is returned to line 15.  At this point, the local variables `a` and
`b` defined in `variable_definition` no longer exist and the global variables
`a` and `b` continue to have their assigned values of `10` and `"Goodbye"`.

The next line, line 16, calls the `variable_output` function.  In line 9, this
function prints the `a` variable.  Since no local variable is defined as `a`,
it uses the global variable `a`.  Same for line 10 and the `b` variable.

### Use of `global` to Modify Global Variables 
In the example above, when a local function assigns a value to a variable with
the same name as a global variable, it creates a new local variable of the same
name and does not change the value of the global variable.  

Let's say we did want for a local function to modify the global variable instead
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
and so any use of those variables will use the global variable, rather than
create a local variable.  The output for this modified code is as follows:
```
a defined as 5 in variable_definition
b defined as Hello in variable_definition
a has the value of 5 in variable_output
b has the value of Hello in variable_output
```

### Another example of when `global` needs to be used
__Module Code:__
```
1  def add_to_inventory(number_of_additions):
2      stock_count = stock_count + number_of_additions
3      print("The new stock count is {}".format(stock_count))
4      return
5  
6  stock_count = 15
7  add_to_inventory(12)
```
__Output when module code above is run:__
```
Traceback (most recent call last):
  File "D:\ClassRepos\BME547\mysandbox.py", line 7, in <module>
    add_to_inventory(12)
  File "D:\ClassRepos\BME547\mysandbox.py", line 2, in add_to_inventory
    stock_count = stock_count + number_of_additions
UnboundLocalError: local variable 'stock_count' referenced before assignment
```
__Description:__

The first line of code to be executed is line 6 where the `stock_count`
*global* variable is created and assigned the value of `15`.  Then, the 
`add_to_inventory(12)` command is executed.  Line 2
is executed next.  On this line, the Python interpreter sees the left side of
the assignment and realizes that a variable assignment is being made.  So,
since this is happening within a function, Python creates a new *local*
variable called `stock_count`.  Then, the Python interpreter looks at the right 
side of the assignment and tries to get the value of the `stock_count` variable.  
Since there is now a *local* version of `stock_count`, it tries to use that value.
But, it hasn't been assigned a value yet.  So, an error is generated because
the value of `stock_count` was needed before it was assigned.

This can again be fixed by using the `global` command.

__Modified Code:__
```
1  def add_to_inventory(number_of_additions):
2      global stock_count
3      stock_count = stock_count + number_of_additions
4      print("The new stock count is {}".format(stock_count))
5      return
6  
7  stock_count = 15
8  add_to_inventory(12)
```
__Output when modified code above is run:__
```
The new stock count is 27
```
For this case, when `add_to_inventory` is run, Python is told to use the
*global* version of `stock_count` and no *local* version is created.

### Mutable Variables
Mutable variable types work a bit differently.  If a mutable variable is
created and assigned in a function, it is created as a local variable.  For 
example:

__Module Code:__
```
1  name_list = ["Ape", "Bonobo", "Chimp"]
2
3  def print_names():
4      name_list = ["Zebra", "Yak", "Xenops"]
5      for i, person_name in enumerate(name_list):
6          print(i, person_name)
7      return
8
9  print_names()
10 print("The global name_list is {}".format(name_list))
```
__Output when module code above is run:__
```
0 Zebra
1 Yak
2 Xenops
The global name_list is ['Ape', 'Bonobo', 'Chimp']
```

In this case, a *global* variable `name_list` is created on line 1.  Then,
when `print_names()` is called on line 9, line 4 is executed.  This line is 
creating and assigning a new list to the `name_list` variable and so creates a
*local* variable `name_list`.  This local version is used for the print loop.
The *global* variable `name_list` is not changed as
evidenced by the print output from line 10.

If we wanted to change the global variable instead of creating a local one, we 
would need to use the `global` keyword.

__Modified Code:__
```
1  name_list = ["Ape", "Bonobo", "Chimp"]
2
3  def print_names():
4      global name_list
5      name_list = ["Zebra", "Yak", "Xenops"]
6      for i, person_name in enumerate(name_list):
7          print(i, person_name)
8      return
9
10  print_names()
11 print("The global name_list is {}".format(name_list))
```
__Output when modified code above is run:__
```
0 Zebra
1 Yak
2 Xenops
The global name_list is ['Zebra', 'Yak', 'Xenops']
```

But, here is where mutable variables can act differently.  If you "modify" an
existing *global* mutable variable, rather than give it a new assignment, you 
do not create a *local* version but can use the *global* version, and there is
no need to use the `global` keyword.  In the following
example, a list is modified using the `append` method.

__Module Code:__
```
1  name_list = ["Ape", "Bonobo", "Chimp"]
2
3  def print_names():
4      name_list.append("Zebra")
5      for i, person_name in enumerate(name_list):
6          print(i, person_name)
7      return
8
9  print_names()
10 print("The global name_list is {}".format(name_list))
```
__Output when module code above is run:__
```
0 Ape
1 Bonobo
2 Chimp
3 Zebra
The global name_list is ['Ape', 'Bonobo', 'Chimp', 'Zebra']
```

In this code, when line 4 is executed by the Python interpreter, it is not
creating and assigning a new variable.  Rather, it is modifying an existing
variable.  So, the interpreter first looks to see if there is a local variable
called `name_list`.  Since there is not, it then looks for and finds the 
global `name_list` variable and makes a change to it.

Other mutable variable types, such as dictionary and classes, will work the
same way.  As long as you are not creating a new instance of that data type,
you can modify the existing variable without the need of the `global` keyword.

In these cases, it is still okay to use the `global` variable if you like to
make it even more clear that you are using the *global* variable.


## References
For a more "pythonic" explanation of scope, refer to 
<https://docs.python.org/3/tutorial/classes.html#python-scopes-and-namespaces>.

