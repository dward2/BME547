# Function Modularity

When we write code, it possible that we could just write a long series of
Python commands to do what we want to do in order. However, that is very
inefficient. Instead, we organize our code into functions that each complete a
specific and limited function of our overall program. We do this for three
reasons (among others).

### Reusability

We often find that we need to use a certain group of Python code lines many
times during our program to accomplish a particular task. Rather than rewrite
that code multiple times, it is better to put that code into a function that
can be called whenever it is needed. The function can be sent parameter inputs
to work on different sets of data each time. By having this code in a single
function rather than duplicated in many parts of the code, you only need to
make a change in one place if a change is necessary.

### Testability

As we will discuss later in the semester, we will be writing test to ensure
that our code works as expected. It is easier to write these tests when the
code is written in short, specific functions with defined inputs and outputs.

### Readability

When a program is split into functions with meaningful names, it is often
easier to see how the program flows and is organized.

### Rules of Thumb

* How big or small should a function be? One guideline is to come up with a
  single sentence to describe what the function is supposed to do. If you need
  to use the word "and", that function should probably be broken down further.
  For example, if you would describe a function as "This function reads in an
  input file and parses it into variables and does calculations on that data",
  this function should probably be broken down into three smaller functions
  that 1) reads in the data, 2) parses the data, and 3)
  does the calculations.
* A good function takes a specific set of inputs, does a specific and limited
  set of operations/decisions based on that data, and reports a result. If your
  function is doing lots of unrelated calculations or operations, consider
  breaking the function up further.
* Functions that do input/output should generally be separated from functions
  that do data manipulation, calculations, or decision making.


## Example

Let's look at an example of how we can improve the modularity, and therefore
testability and readability, of a code sample.

Here is some sample code:

```python
"""dosing.py
    Example program of calculating first-day dose of medicine for pediatric
        patients.
    NOTE:  This is a programming example, and should not be used for any
             type of medical treatment or diagnostics.
"""


def dose_amount():
    print("Day One Dosing Guidelines")
    print("")
    print("Choose diagnosis:")
    print("1 - Acute otitis media")
    print("2 - Acute bacterial sinusitis")
    print("3 - Community-acquired pneumonia")
    print("4 - Pharyngitis/tonsilitis")
    diagnosis = int(input("Enter a number: "))
    print("PATIENT WEIGHT")
    print("Enter patient weight followed by units of kg or lb.")
    print("Examples:  65.3 lb      21.0 kg")
    weight_input = input("Enter weight: ")
    weight_data = weight_input.split(" ")
    weight = float(weight_data[0])
    units = weight_data[1]
    if units == "lb":
        weight = weight / 2.205
    dosages_mg_per_kg = [30, 10, 10, 12]
    dosage_mg_per_kg = dosages_mg_per_kg[diagnosis - 1]
    dosage_mg_first_day = weight * dosage_mg_per_kg
    print("CORRECT DOSAGE")
    print("For a patient weighing {:.1f} kg,".format(weight))
    print("  the correct dosage is {:.1f} mg the first day"
          .format(dosage_mg_first_day))


if __name__ == '__main__':
    dose_amount()
```

The whole program is written in a single function which has a variety of
problems. First, it is hard to read and understand quickly. There are too many
lines of code one right after the other. Second, this one function does too
many things. It gets two types of output, does unit conversion, does
calculations, and outputs the result. Third, you cannot test any of its
functionality. It doesn't return anything and has too many different functions
to test.

So, a first step is to break it up into different functions based upon the
different tasks it performs.

```python
"""dosing.py
    Example program of calculating first-day dose of medicine for pediatric
        patients.
    NOTE:  This is a programming example, and should not be used for any
             type of medical treatment or diagnostics.
"""


def dose_amount():
    get_user_input()


def get_user_input():
    print("Day One Dosing Guidelines")
    print("")
    print("Choose diagnosis:")
    print("1 - Acute otitis media")
    print("2 - Acute bacterial sinusitis")
    print("3 - Community-acquired pneumonia")
    print("4 - Pharyngitis/tonsilitis")
    diagnosis = int(input("Enter a number: "))
    print("PATIENT WEIGHT")
    print("Enter patient weight followed by units of kg or lb.")
    print("Examples:  65.3 lb      21.0 kg")
    weight_input = input("Enter weight: ")
    weight_data = weight_input.split(" ")
    weight = float(weight_data[0])
    units = weight_data[1]
    if units == "lb":
        weight = weight / 2.205
    calculate_dosage(diagnosis, weight)


def calculate_dosage(diagnosis, weight):
    dosages_mg_per_kg = [30, 10, 10, 12]
    dosage_mg_per_kg = dosages_mg_per_kg[diagnosis - 1]
    dosage_mg_first_day = weight * dosage_mg_per_kg
    output_results(weight, dosage_mg_first_day)


def output_results(weight, dosage_mg_first_day):
    print("CORRECT DOSAGE")
    print("For a patient weighing {:.1f} kg,".format(weight))
    print("  the correct dosage is {:.1f} mg the first day"
          .format(dosage_mg_first_day))


if __name__ == '__main__':
    dose_amount()

``` 

In this code, we have now separated the input code from the calculation code
from the output code. The shape of the program is beginning to be more obvious
to the reader in that the functions and their names help outline its flow. But,
how these functions interact is still problematic. You will notice that the
starting function, `dose_amount` makes a call to the function
`get_user_output`. That function then calls `calculate_dosage` which then
calls `output_results`. The functions are "chained" together. So, while these
functions may help the flow of the program be more apparent, they still cannot
be individually called and tested because they automatically call the next one.

A better approach would be as follows:

```python
"""dosing.py
    Example program of calculating first-day dose of medicine for pediatric
        patients.
    NOTE:  This is a programming example, and should not be used for any
             type of medical treatment or diagnostics.
"""


def dose_amount():
    diagnosis, weight = get_user_input()
    dosage_mg_first_day = calculate_dosage(diagnosis, weight)
    output_results(weight, dosage_mg_first_day)


def get_user_input():
    print("Day One Dosing Guidelines")
    print("")
    print("Choose diagnosis:")
    print("1 - Acute otitis media")
    print("2 - Acute bacterial sinusitis")
    print("3 - Community-acquired pneumonia")
    print("4 - Pharyngitis/tonsilitis")
    diagnosis = int(input("Enter a number: "))
    print("PATIENT WEIGHT")
    print("Enter patient weight followed by units of kg or lb.")
    print("Examples:  65.3 lb      21.0 kg")
    weight_input = input("Enter weight: ")
    weight_data = weight_input.split(" ")
    weight = float(weight_data[0])
    units = weight_data[1]
    if units == "lb":
        weight = weight / 2.205
    return diagnosis, weight


def calculate_dosage(diagnosis, weight):
    dosages_mg_per_kg = [30, 10, 10, 12]
    dosage_mg_per_kg = dosages_mg_per_kg[diagnosis - 1]
    dosage_mg_first_day = weight * dosage_mg_per_kg
    return dosage_mg_first_day


def output_results(weight, dosage_mg_first_day):
    print("CORRECT DOSAGE")
    print("For a patient weighing {:.1f} kg,".format(weight))
    print("  the correct dosage is {:.1f} mg the first day"
          .format(dosage_mg_first_day))


if __name__ == '__main__':
    dose_amount()

```

In this example, each function returns its result to the `dose_amount` function
that acts as a driver and calls each function in turn, sharing the needed
variables.  `dose_amount` easily shows the flow of the program. Each function
can now be used independently and reused in other parts of the code if needed.

If we look specifically at the `calculate_dosage` function, this now represents
a good unit function. It takes specific input (diagnosis and weight), makes a
specific calculation (the dosage based on the diagnosis and weight), and
returns a result. This function has a specific purpose and can easily be
tested.

`get_user_input`, on the other hand, still isn't as easily tested. It still
does multiple tasks:  it gets two different inputs and does some string
manipulation and unit conversion. So, it still cannot be tested. First, lets
split this into the two types of inputs:

```python
def get_user_input_diagnosis():
    print("Day One Dosing Guidelines")
    print("")
    print("Choose diagnosis:")
    print("1 - Acute otitis media")
    print("2 - Acute bacterial sinusitis")
    print("3 - Community-acquired pneumonia")
    print("4 - Pharyngitis/tonsilitis")
    diagnosis = int(input("Enter a number: "))
    return diagnosis


def get_user_input_patient_weight():
    print("PATIENT WEIGHT")
    print("Enter patient weight followed by units of kg or lb.")
    print("Examples:  65.3 lb      21.0 kg")
    weight_input = input("Enter weight: ")
    weight_data = weight_input.split(" ")
    weight = float(weight_data[0])
    units = weight_data[1]
    if units == "lb":
        weight = weight / 2.205
    return weight
```

When we look at both of these functions, they each take some user input and do
some brief calculations on those inputs. This is still a problem for testing.
pytest has no way of accepting user input, and so the tests will fail. We need
to further separate all I/O statements from any code that does data
manipulation or calculation. That split would like like this:

```python
def get_user_input_diagnosis():
    print("Day One Dosing Guidelines")
    print("")
    print("Choose diagnosis:")
    print("1 - Acute otitis media")
    print("2 - Acute bacterial sinusitis")
    print("3 - Community-acquired pneumonia")
    print("4 - Pharyngitis/tonsilitis")
    diagnosis = input("Enter a number: ")
    return diagnosis


def convert_entry_to_int(entry):
    return int(entry)


def get_user_input_patient_weight():
    print("PATIENT WEIGHT")
    print("Enter patient weight followed by units of kg or lb.")
    print("Examples:  65.3 lb      21.0 kg")
    weight_input = input("Enter weight: ")
    return weight_input


def convert_weight_entry_to_weight_kg(weight_input):
    weight_data = weight_input.split(" ")
    weight = float(weight_data[0])
    units = weight_data[1]
    if units == "lb":
        weight = weight / 2.205
    return weight
```

From the `get_user_input_diagnosis` function, we removed the data manipulation
step of converting the string to an integer and put it in a separate function.

From the `get_user_input_patient_weight` function, we removed the string
manipulation and unit conversion code into a separate function.

The final code now looks like this:

```python
"""dosing.py
    Example program of calculating first-day dose of medicine for pediatric
        patients.
    NOTE:  This is a programming example, and should not be used for any
             type of medical treatment or diagnostics.
"""


def dose_amount():
    diagnosis_entry = get_user_input_diagnosis()
    diagnosis = convert_entry_to_int(diagnosis_entry)
    weight_entry = get_user_input_patient_weight()
    weight = convert_weight_entry_to_weight_kg(weight_entry)
    dosage_mg_first_day = calculate_dosage(diagnosis, weight)
    output_results(weight, dosage_mg_first_day)


def get_user_input_diagnosis():
    print("Day One Dosing Guidelines")
    print("")
    print("Choose diagnosis:")
    print("1 - Acute otitis media")
    print("2 - Acute bacterial sinusitis")
    print("3 - Community-acquired pneumonia")
    print("4 - Pharyngitis/tonsilitis")
    diagnosis = input("Enter a number: ")
    return diagnosis


def convert_entry_to_int(entry):
    return int(entry)


def get_user_input_patient_weight():
    print("PATIENT WEIGHT")
    print("Enter patient weight followed by units of kg or lb.")
    print("Examples:  65.3 lb      21.0 kg")
    weight_input = input("Enter weight: ")
    return weight_input


def convert_weight_entry_to_weight_kg(weight_input):
    weight_data = weight_input.split(" ")
    weight = float(weight_data[0])
    units = weight_data[1]
    if units == "lb":
        weight = weight / 2.205
    return weight


def calculate_dosage(diagnosis, weight):
    dosages_mg_per_kg = [30, 10, 10, 12]
    dosage_mg_per_kg = dosages_mg_per_kg[diagnosis - 1]
    dosage_mg_first_day = weight * dosage_mg_per_kg
    return dosage_mg_first_day


def output_results(weight, dosage_mg_first_day):
    print("CORRECT DOSAGE")
    print("For a patient weighing {:.1f} kg,".format(weight))
    print("  the correct dosage is {:.1f} mg the first day"
          .format(dosage_mg_first_day))


if __name__ == '__main__':
    dose_amount()
```

Now, all of the functions either do ONLY I/O or ONLY data manipulation. All of
the functions that do data manipulation can now be tested as they have defined
inputs, a single purpose, and defined outputs.
