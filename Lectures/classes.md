# Classes
* Classes can group together a set of variables and functions that are related.
* Variables associated with the class are called attributes or properties.
* Functions associated with the class are called methods.

## Creating a class

A class is defined with the following heading:
```
class Person:
```
`Person` is the name of the class.  If the class should inherit the properties
of another class, you would define the class as:
```
class Person(object):
```
where `object` is replaced by the name of the class to inherit from.  If
`object` is not replaced, the two class definitions above act identically.

The contents of the class are then defined in the indented block after this
heading.

## Creating class properties

The properties (variables) of the class are created in one of two ways.  If
the properties are going to start empty, or always start with a specific value,
they can be created in the class as follows:

```python
class Person:
    firstname = None
    lastname = None
```
Replace `None` with a value if desired for the properties to start with a
specific value.

## Creating an instance of the class
Once defined, an instance of the class can be created in code as a variable as 
follows:
```
x = Person()
```
The variable `x` is now an object that has the structure defined by the 
`Person` class.

## Accessing class properties

To access the properties of a class instance in our code, we reference the 
object variable name, followed by a `.` and the property name:
```
x = Person()
print(x.firstname)
print(x.lastname)

OUTPUT:
None
None
```
The value of a property is set in a similar manner:
```
x.firstname = "Robert"
x.lastname = "Smith"
print(x.firstname)
print(x.lastname)

OUTPUT:
Robert
Smith
```
## Creating class methods
In addition to variables or properties, classes can have functions, called
methods, that act on the variables found in the class.  Consider the
following method added to the `Person` class.
```python
class Person:
    firstname = None
    lastname = None
    
    def return_full_name(self):
        return self.firstname + " " + self.lastname
```
In order for the method to have access to the properties of the class, we
must establish those variables within the local scope of the method.  To
do that, we define a parameter called `self` in the parameter list of the
method.  Python understands `self` to refer to the instance of the object
itself and is how the method has access to the properties and other methods 
of this instance.  In the method above, the class properties of 
`firstname` and `lastname` are accessed within the method by `self.firstname`
and `self.lastname`.  Any variable created within a class method that does
not start with `self` is considered local to that function only.

NOTE:  All methods must have the `self` reference as the first parameter list,
even if you don't need it.  This is a Python syntax requirement. 

## Accessing class methods
This method can be called from our code as follows:
```
x = Person()
x.firstname = "Robert
x.lastname = "Smith"
print(x.return_full_name())

OUTPUT:
Robert Smith
```
Notice that when we refer to a method, we need to include `()` after the name
as it is a function call.  Also note that we do not include a `self` variable 
in the parameter list, even though it is present in the method definition.
Python automatically populates this with the instance referred to in the method
call (`x` in the case of `x.return_full_name()`).  If the method defines
additional parameters beyond `self`, they would be included inside the 
parentheses.  But, `self` is never included.  An example of this is shown below
on this page.

## Initializing properties when making an instance: `__init__()`
In the examples above, a class is made with empty properties and then the
properties are populated.  This can be done in an easier way by allowing
initial values of the properties to be declared when defining an instance of
a class.  This is done using a special class method called `__init__`.

```python
class Person:

    def __init__(self, first_name_arg, last_name_arg):
        self.firstname = first_name_arg
        self.lastname = last_name_arg
```
The `__init__` method is called immediately upon creating a new instance
of the class in a variable as shown here:
```
x = Person("Robert", "Smith")
```

After `self` in the parameter list of `__init__`, include any other 
parameters you 
want to initialize when creating a new object of this class.  In the 
example above, we include two parameters that are used for initializing the 
class properties of `self.firstname` and `self.lastname`.  The inclusion of 
`self.` in the variable name makes it available to all of the functions in 
the class.  This is an alternate means of creating a class property to that of
defining them directly within the class.

Note that the `__init__` method can do more than just assign variables.  It
can do other calculations or call other methods in the class as needed to 
initialize it for use.

Again, while `self` must be included in the parameter list when defining
the method in the class, it is not included in the call to create an
instance of the class.


## Default Parameters

Let's add `age` as a property in our Class definition.
```python
class Person(object):

    def __init__(self, first_name_arg, last_name_arg, age_arg):
        self.firstname = first_name_arg
        self.lastname = last_name_arg
        self.age = age_arg
```
But, let's say we forgot to update our line of code that read 
`x = Person("Robert", "Smith")`.  Python will return 
```
TypeError: __init__() missing 1 required positional argument: 'age_arg'
```
We can avoid this error by giving the `__init__` method a default
value for the `age_arg` parameter as follows:
```
    def __init__(self, first_name_arg, last_name_arg, age_arg=None):
``` 
Now, if no value is provided for `age_arg`, the `__init__` method will fill
it with `None` and avoid an error.  We can then later set the age by
directly accessing the property of the class as such:
```
x = Person("Robert", "Smith")`
x.age = 35
```

## Referring to other methods in a class
When one method in a class calls another, it also needs to use the `self` 
reference.  For example:
```python
class Person(object):

    def __init__(self, first_name_arg, last_name_arg, age_arg):
        self.firstname = first_name_arg
        self.lastname = last_name_arg
        self.age = age_arg
    
    def return_full_name(self):
        return self.firstname + " " + self.lastname
        
    def print_info(self):
        full_name = self.return_full_name()
        print("{} is aged {}".format(full_name, self.age))
```


## Creating and storing multiple objects

A Class is a blueprint/template for a collection of properties and methods.
We can then make may different instances of a class, called objects.  Each
object will have its own set of values for the properties and does not know
the contents or properties of other objects.  

Using the example `Person` class above, we can now make a database of Person
objects.
```
def create_persons_database():
    database = []
    new_person = Person("Ann", "Jones", 35)
    database.append(new_person)
    new_person = Person("Bruce", "Wayne", 40)
    database.append(new_person)
    for x in database:
        print(x.return_full_name())
    print(database[0].age)

```
The function above creates an empty list called `database`.  An instance of
the `Person` class is created in the variable `new_person` and then
appended to the `database` list.  Then, a new instance of the `Person`
class is created also using the `new_person` variable.  While `new_person`
now points to this new instance, the first instance still exists inside the
`database` list.  The second instance is then appended to the `database`
list.

The objects found in the `database` list can be access as shown by the two
example:  one using a `for` loop and one accessing a specific item via an
index.

# Hidden Properties and Set/Get Functions
There may be times when, upon the setting of a property in a class, I may
want to do some calculations on that input before storing it in the 
property.  

Let's assume that I want to add the persons weight to the `Person` class. 
And, let's imagine that I have a really old
scale that, depending on how it is used, might record a negative weight.  I
would want this converted to a positive weight in the persons file.

First, I need to define the weight property in the class.  But, unlike
other properties, I don't want the user to be able to access it directly
because I don't want a negative number to be used.  So, I "hide" the
property by including double underscore before its name when creating it
in the `__init__` function.
```python
    def __init__(self, first_name_arg, last_name_arg, age_arg=None):
        self.firstname = first_name_arg
        self.lastname = last_name_arg
        self.age = age_arg
        self.__weight = None

```
This property `__weight` is not accessible outside of the class.  So, in 
order for the code outside of the class to set or return the weight , 
I need to define specific functions in the class to perform those functions.
```python
    def set_weight(self, weight_arg):
        if weight_arg < 0:
            self.__weight = -weight_arg
        else:
            self.__weight = weight_arg

    def get_weight(self):
        return self.__weight
```
With these functions, some code is now run to manipulate the inputs before
setting the property of the class.
```pythonstub
john = Person("John", "Smith", 45)
john.set_seight(-150)
x = john.get_weight()
print(x)

OUTPUT:
150
```

Let's say that John has gained 17 pounds.  Adding 17 to the weight would
require the following `get_weight` and `set_weight` calls.
```
john.set_weight(john.get_weight()+17)
print(john.get_weight())

OUTPUT:
167
```
That is a very ugly way to add 17 to a variable.
  
# Property Decorator
 Property decorators allow the use of functions when getting and setting
 class properties. 
 
 First, the `@property` decorator is used before a class function that gets 
 (or returns) the property of interest. 
 ``` 
    @property
    def weight(self):
        return self.__weight
  ```
Now that `weight` is defined as a property, we use the `@weight.setter`
decorator before a class function that sets the weight.
```
  @weight.setter
  def weight(self, weight_arg):
      if weight_arg < 0:
          self.__weight = -weight_arg
      else:
          self.__weight = weight_arg
```

Now, in the code, we can get and set the weight as follows:
```
joan = Person("Joan", "Stevens", 45)
joan.weight = -150
x = joan.weight
print("Before weight = {}".format(x))
joan.weight += 17
y = joan.weight
print("After weight = {}".format(y))
```  
The `weight` property created by the `@property` decorator can now be used
like any other kind of property or variable, but the setting and getting
are now controlled by functions that we can control.

The generic format is:
```
    @property
    def name(self):
        {CODE THAT RETURNS YOUR HIDDEN VARIABLE}
        
    @name.setter
    def name(self,input):
        {CODE THAT TAKES INPUT, DOES DESIRED MANIPULATION,
           AND STORES RESULT IN HIDDEN VARIABLE}
```
where `name` can be chosen by user.
  
### Note:
The use of the double underscore before a variable name in a class is actually
called "name mangling."  The variable is not strictly hidden, but is given
a "mangled" name by the Python interpreter.  This is primarily done to 
assist in preventing name conflicts, but is a "hack" for hiding variables
from accidental use. See the Python documentation 
[here](https://docs.python.org/3.7/tutorial/classes.html#private-variables)
for more details.