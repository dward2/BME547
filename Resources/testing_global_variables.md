# Unit Testing of Functions That Modify Global Variables

Typically, when we write a unit test for a function, we send some known data
to the function to be tested and verify that what the function returns is
the correct information based on the sent input.

But, what if the function being tested changes the value of a global variable?
How can we test that the appropriate change was made to the global variable?

## Import a global variable
In addition to importing functions, you can also import variables.  Let's look
at this example:

```python
inventory_lbs = {}

prices_per_lb = {"apples": 2.95,
                 "bananas": 0.65,
                 "cherries": 2.50}

def add_to_inventory(item, pounds):
    if item in inventory_lbs:
        inventory_lbs[item] += pounds
    else:
        inventory_lbs[item] = pounds
    total_cost = pounds * prices_per_lb[item]
    return total_cost
```

A unit test for the function above might look like this:
```python
def test_add_to_inventory():
    from module import add_to_inventory
    input_item = "bananas"
    input_lbs = 1.6
    expected_cost = 1.04
    answer = add_to_inventory(input_item, input_lbs)
    assert answer == expected_cost
```

This unit test function will check that the correct value is returned from the 
function being tested.  But, it does not verify that the `inventory_lbs` global 
variable is correctly modified.  But, we can do such a check if we modify the 
unit test as follows:
```python
def test_add_to_inventory():
    from module import add_to_inventory, inventory_lbs
    input_item = "bananas"
    input_lbs = 1.6
    expected_sale_income = 1.04
    answer = add_to_inventory(input_item, input_lbs)
    answer_inventory = inventory_lbs[input_item]
    assert answer == expected_sale_income
    assert answer_inventory == input_lbs
```

By importing the global variable into the unit test function, we can check
how it is changed by the function being tested.

## Resetting global variables for subsequent unit tests

It must be remembered that the change in the global variable made by a
unit test stays in place and any further unit tests would be using the
updated global variable.  If the other unit tests expect the global variable
to have not changed, we need to "reset" the global variable back to its 
original value before the unit test is ended.  Here is an example of doing 
that:
```python
def test_add_to_inventory():
    from module import add_to_inventory, inventory_lbs
    input_item = "bananas"
    input_lbs = 1.6
    expected_sale_income = 1.04
    answer = add_to_inventory(input_item, input_lbs)
    answer_inventory = inventory_lbs[input_item]
    inventory_lbs.clear()
    assert answer == expected_sale_income
    assert answer_inventory == input_lbs
```
In the function above, the line `inventory_lbs.clear()` is added.  It erases
the entry made into the global variable, so it will be empty for the next
unit test.  Notice that this reset of the global variable is done before any
of the `assert` statements.  When a unit test fails, an `assert` statement
with a `False` condition raises an `AssertionError`.  This causes the unit
test function to immediately stop.  If the global variable "reset" was done
after these failed assertions, the global variable would not be reset and 
subsequent unit tests would also fail.  So, always reset your global variables
before doing any asserts.  This may require you to store the value to be
checked in a separate variable, such as the `answer_inventory` variable above.

## Setting Up Global Variable for a Test
There may be times when you want to initialize a global variable to start with
a certain value for your unit test.  For example, let's look at another
function in the same module as above:
```python
def sell_from_inventory(item, pounds):
    if item in inventory_lbs and pounds < inventory_lbs[item]:
        inventory_lbs[item] -= pounds
        sale_total = pounds * prices_per_lb[item]
    else:
        sale_total = 0
    return sale_total
```
To test this function, we would need to make sure that the global variable
has some content in it so that the function has something to sell.  We can
initialize the content of the global variable in a unit test as follows:
```python
1:  def test_sell_from_inventory():
2:      from module import sell_from_inventory, inventory_lbs
3:      inventory_lbs["cherries"] = 20
4:      answer = sell_from_inventory("cherries", 5)
5:      answer_inventory = inventory_lbs["cherries"]
6:      inventory_lbs.clear()
7:      assert answer == 12.50
8:      assert answer_inventory == 15
```
We can see that:
* an initial value is added to the global variable (line 3)
* the function under test is called (line 4)
* the updated value of the global variable is stored in a local variable 
  (line 5)
* the global variable is reset (line 6)
