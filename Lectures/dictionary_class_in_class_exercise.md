# In Class Exercise

If needed, the starting code can be found at 
https://github.com/dward2/Classwork_Spring2023/blob/main/database.py

## Dictionary Data Type

### Convert `create_patient_entry` function
Convert from creating a list to a dictionary.  
Keys:  
* First Name
* Last Name
* MRN
* Age
* Tests

### Write `get_full_name` and `print_database`
  * First, write a function that receives a patient dictionary and returns
    the full name.
  * Second, write a function that prints each patient on a single line.
  * The output for each patient should look like:
    ```
    MRN: 1, Full Name: Ann Ables, Age: 34
    ```

### Convert `add_test_to_patient` and `get_test_result`
  * Requires also modifying `get_patient_entry`


### Write `minor_or_adult` function
  * Function that receives a patient dictionary
  * Returns string `"adult"` if age 18 or older, otherwise, returns string
     `"minor"`
  * Use this function by printing a string such as "Chris Chou is an adult".

### Convert database from a list to a dictionary
  * Modify all code as needed

## Classes
Convert patient storage from dictionary to class
