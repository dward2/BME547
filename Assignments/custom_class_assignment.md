# Class Assignment

In this assignment, you will create a custom class to hold patient 
information about blood type and determine whether other patients could be 
blood donors for a patient or recipients of donations from a patient.

## Specifications

* Write your code in a module called `patient_data.py`.
* In that module, crease a custom class called `Patient`.
* __Attributes__
  * The `Patient` class should have the following attributes:
    * `mrn`: an integer to contain the patient medical record number
    * `name`: a string to contain the patient's name
    * `blood_type`: a string to contain the patient's blood type
    * `can_receive_from`: a list that will eventually contain tuples, each tuple 
      consisting of an integer and a string.
* __Initialization__
  * The `Patient` class should have an `__init__` method that receives a 
    single string parameter.  
    * That string will take one of two forms:
      * "mrn,name,blood_type"
      * "mrn,name"
    * The `__init__` method should parse this string and put the mrn, as an 
      integer, into the `mrn` attribute, the name into the `name` attribute, 
      and, if it exists, the blood_type into the `blood_type` attribute.
    * The function should convert the mrn found in the string to an integer 
      for storage.  It should also verify that the mrn is an integer and 
      does not contain any letters.  If it does, the method should raise a 
      `Value Error` with an appropriate error message (it cannot be the 
      default message raised by `ValueError` but is one you create).  
    * The blood_type should be verified as discussed below.
* __Methods__
  * The `Patient` class should have the following methods:
    * `add_blood_type(<str_variable>)`
      * This method will add a blood type to the patient.
      * This method should receive a single string parameter which will 
        contain a blood type.
      * The method should verify the blood_type as discussed below.
      * The blood_type should be stored in the `blood_type` attribute.
    * `get_blood_type()`
      * This method should return the patient blood type as a string.
    * `is_donor_to_match(<recipient_Patient_variable>)`
      * This method will check to see whether the current patient can donate 
        blood to the recipient patient that is sent as a parameter.  
      * This method should receive a single parameter that will be another 
        instance of the `Patient` class.
      * If the current patient can donate to the recipient, this method 
        should create a tuple as `(<mrn>, <name>)` where `<mrn>` and `<name>` 
        are the mrn and name of the current patient and this tuple should be 
        added to the recipient patient's `can_receive_from` attribute.  And, 
        the method should return the boolean `True`.
      * If the current patient cannot donate to the recipient, the method 
        should return the boolean `False`.
    * `is_recipient_from_match(<donor_Patient_variable>)`
      * This method will check to see whether the current patient can receive 
        a blood donation from the donor patient sent as a parameter.
      * This method should receive a single parameter that will be another 
        instance of the `Patient` class.
      * If the donor patient sent as a parameter can donate to the current 
        patient, this method should create a tuple as `(<mrn>, <name>)` where 
        `<mrn>` and `<name>` are the mrn and name of the donor patient and this 
        tuple should be added to the current patient's `can_receive_from` 
        attribute.  And, the method should return the boolean `True`.
      * If the current patient cannot receive blood from the recipient, the 
        method should return the boolean `False`.
    * `list_possible_donors()`
      * This method will return a string containing the names and medical 
        record numbers of possible donors.
      * The string should be formatted as follows:  
        `"patient_1_mrn: patient_1_name\npatient_2_mrn: patient2_name\n...
        "`
        In other words, for each patient in the `can_receive_from` 
        attribute should be formatted as `"patient_mrn: name"` and then add 
        a new line character `"\n"` between each patient.
      * If there are no patients in the list, return an blank string:  `""`
  * __Blood Type Verification__
    * Any time that the `Patient` class receives a blood type, either via 
      initialization or the `add_blood_type` method, the class must verify 
      that the string sent as a blood_type contains a valid blood type.
    * Valid blood types include:
      * O+
      * O-
      * A+
      * A-
      * B+
      * B-
      * AB+
      * AB-
    * If the blood type string does not contain one of the above blood 
      types, the class should raise the `ValueError` exception and provide 
      a meaningful error message.

### Notes
* For the parameter sent to the initialization function, you can assume 
  that it will always be a string and it will always be one of the two 
  formats given.  In other words, there will always be one or two commas, 
  there will always be content before/after the commas, and there will 
  never be leading or trailing spaces, or spaces before/after the commas.
* As mentioned above, you cannot assume that the medical record number 
  portion of the string will contain only numbers.
* You can assume that the parameter sent to the `add_blood_type` method 
  will be a string.  BUT, you can make no assumptions about the content of 
  the string.  Hence, the need for verification.
* Feel free to create additional methods or attributes within the class as 
  needed to perform the required tasks.
* Feel free to write code that uses the class to test it during development 
  and that code can remain inside the module, as long as it does not 
  execute during an import of the Patient class to another module.  This 
  additional code will not be evaluated.  
* You must create unit test functions for all of your class methods, 
  including the initialization.
* Docstrings are only required for the Patient class methods, including the 
  initialization.
* If you need a reminder about blood type compatability, you can refer to 
  the website 
  <https://www.lifeblood.com.au/patients/blood-for-transfusion/matching-blood-groups> 
  and look at the table in the section titled "1 Red cell compatibility".  
  In this table, "Patients blood group" refers to the blood recipient.

## Grading Expectations
* Correct design and usage of a custom class
* Comprehensive testing of class methods
* Good git usage and workflow
* Meeting the above specifications for the custom class
* Presence and content of docstrings
* Conforms to PEP-8 Style Guide
* Appropriate modularity in the methods
* GitHub Actions CI integration with all branches passing unit tests and 
  PEP-8 style before merging into the `main` branch.
* Appropriate use of virtual environments as demonstrated by a 
  `requirements.txt` file being present in your GitHub repository
* README.md need only consist of your name.  No further info necessary for 
  this assignment.
* Final submission pushed to GitHub be the deadline and tagged appropriately.
* Plus any expectations from previous assignments