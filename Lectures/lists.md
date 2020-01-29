# Lists:  A brief introduction

Python Documentation for Lists - 
https://docs.python.org/3/library/stdtypes.html#lists

The "list" in Python is a sequence of items that are mutable (can be changed).
The items in the list can be any Python object, and do not need to all be the
same type of object.

A list can be created in multiple ways.  The first is explicitly using the `[]`
brackets and separating the list items by commas.
```
x = [1, 4, -4, 2]
y = ["hello", 4, 3.5, "goodbye", True]
```

Existing variables can be used when creating the list:
```
first_name = "Ann"
last_name = "Applebee"
full_name = [first_name, last_name]
```

Emtpy lists can be created in one of two ways:
```
list_1 = []
list_2 = list()
```

Items can be added to an existing list using the `append` method:
```
patient = list()
patient.append(full_name)
patient.append(30)
patient.append(True)
print(patient)

Output:
[['Ann', 'Applebee'], 30, True]
```
Notice that lists can be nested within lists.

List entries are accessed using their index, starting with zero as the first 
item.

```
print("Patient age is {}".format(patient[1]))

Output:
Patient age is 30
```

```
# Modify age
patient[1] = 35
print(patient)

Output:
[['Ann', 'Applebee'], 35, True]
````

Nested items are referenced as shown by this example:
```
print("First name is {}".format(patient[0][0]))
print("Last name is {}".format(patient[0][1]))

Output:
First name is Ann
Last name is Applebee
```
In the example above, `patient[0]` returns the list `['Ann', 'Applebee']`.  To
get the first item of that new list, we add another `[0]`.

Note that strings are also considered lists.
```
my_name = "Bill"
print(my_name[1])
print(patient[0][1][5])
Output:
i
b
```
