# In Class Exercise

If needed, the starting code can be found at 

<https://github.com/BME547-Spring2024/bme-547-classwork-dward2/blob/testing/health_database.py>

## Dictionary Data Type
* Create a `dictionary` branch for this work.

### Convert `create_database_entry` function
Convert from creating a list to a dictionary.  
Keys:  
* First Name
* Last Name
* Age
* MRN
* Tests

### Write `get_full_name` and modify `print_database`
  * First, write a function that receives a patient dictionary and returns
    the full name.
  * Second, modify the `print_database` function that prints each patient on 
    a single line.  *Can remove any Room printing.*
  * The output for each patient should look like:
    ```
    MRN: 1, Full Name: Ann Ables, Age: 34
    ```
### Convert `get_patient`

### Convert `add_test_to_patient`
  
### Write `minor_or_adult` function
  * Function that receives a patient dictionary
  * Returns string `"adult"` if age 18 or older, otherwise, returns string
     `"minor"`
  * Use this function by printing a string such as "Chris Chou is an adult".

### Convert database from a list to a dictionary
  * Modify all code as needed

## When Finished
When you are finished, click on
<a href="http://daw.colab.duke.edu/done" target="_blank">this link</a>
to let me know you are finished.