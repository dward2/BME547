# Dictionary Data Type
What is a dictionary in our common understanding?  A list of words and
definitions associated with each of those words:

* day:  the time between sunset and sundown
* food:  any nutritious substance that people or animals eat or drink

### Creating Dictionaries in Python
```
def create_dictionary():
    new_dictionary = {"day": "between sunrise and sunset",
                      "food": "something to eat",
                      "night":  "when the moon is out"}
    return new_dictionary
    
def output_dictionary(in_dictionary):
    print("Variable type:")
    print(type(in_dictionary))
    print("Dictionary contents:")
    print(in_dictionary)

if __name__ == "__main__":
    my_dictionary = create_dictionary()
    output_dictionary(my_dictionary)
    
OUTPUT:
Variable type:
<class 'dict'>
Dictionary contents:
{'day': 'between sunrise and sunset', 'food': 'something to eat', 
    'night': 'when the moon is out'}
```


* Dictionary maps a `key` to a `value`.  In the example above, keys are the
words and values are the definitions.

* Lookups in a dictionary using a key are very efficient -- no matter how large 
a dictionary is, asking for the value corresponding to a key happens in the 
same amount of time.

### Retrieving values from a dictionary 
```
def create_dictionary():
    new_dictionary = {"day": "between sunrise and sunset",
                      "food": "something to eat",
                      "night":  "when the moon is out"}
    return new_dictionary
    
def retrieve_definitions(in_dictionary):
    x = in_dictionary["day"]
    print(x)
    y = in_dictionary.get("food")
    print(y)

if __name__ == "__main__":
    my_dictionary = create_dictionary()
    retrieve_definitions(my_dictionary)
    
OUTPUT:
between sunrise and sunset
something to eat
```

* `dictionary["key"]` returns the corresponding value for "key", but will raise
 a `KeyError` if key does not exist.  
* `dictionary.get("key")` will also return the value for "key", but will NOT 
throw an error if key does not exist, but rather return `None`.

### Adding values to a dictionary
```
def create_dictionary():
    new_dictionary = {"day": "between sunrise and sunset",
                      "food": "something to eat",
                      "night": "when the moon is out"}
    return new_dictionary

def add_to_dictionary(in_dictionary):
    in_dictionary["drink"] = "swallowing a liquid"
    return in_dictionary

if __name__ == "__main__":
    my_dictionary = create_dictionary()
    my_dictionary = add_to_dictionary(my_dictionary)
    print(my_dictionary["drink"])

OUTPUT:
swallowing a liquid
```

### Dictionaries have many built-in methods.
<https://docs.python.org/3/library/stdtypes.html#mapping-types-dict>

### Contents of Dictionaries
Keys are usually strings, but the values can be any python type.  In the
example below, a dictionary is created that has values containing strings,
numbers, and booleans.
```
def create_person():
    bob = {"First Name": "Robert",
           "Last Name":  "Smith",
           "Age": 35,
           "Ave Heart Rate": 65,
           "HIPPA On File": True}
    return bob
    
def output_person_info(person):
    x = full_name(person)
    print("Full name = {}".format(x))
    a = person["Age"]
    print("Age = {}".format(a))
    m = minor_or_adult(person)
    print(m)

def full_name(person):
    return person["First Name"] + " " + person["Last Name"]

def minor_or_adult(person):
    if person["Age"] > 17:
        return "Adult"
    else:
        return "Minor"
    
if __name__ == "__main__":
    newPerson = create_person()
    print(type(newPerson))
    print(newPerson)
    output_person_info(newPerson)
    
OUTPUT:
<class 'dict'>
{'First Name': 'Robert', 'Last Name': 'Smith', 'Age': 35, 'Ave Heart Rate': 65,
    'HIPPA On File': True}
Full name = Robert Smith
Age = 35
Adult

```

Values in a dictionary can also be tuples, lists, or dictionaries.
```
bob = {"First Name": "Robert",
           "Last Name":  "Smith",
           "Age": 35,
           "Visits": ["1/3/2014", "2/15/2015", "5/22/2016"]}
print(bob["Visits"])
print(bob["Visits"][1])

OUTPUT:
['1/3/2014', '2/15/2015', '5/22/2016']
2/15/2015
           
```
In the examples above, we have made dictionaries to contain definitions and
dictionaries to contain personal information.  We have written functions that
are designed to manipulate the data in those dictionaries.

Now, imagine that you have a very large code base with many different types of
dictionaries, and each type of dictionary has specific functions to manipulate
or act on those dictionaries.  It could start to get confusing about which
functions are meant to act on which dictionaries.  Also, when a second version
of a dictionary is made (for example, a new person dictionary), we need to 
ensure that it contains the same information.  

"Classes" exist to address some of these concerns. 
