# Adapt `Patient` class to use PyMongo

In the `database.py` file, there is the `Patient` class that holds information
about a patient.  Each instance of this class is then stored in a `db` list.

**Task**: Modify `Patient` such that it stores patient information in a MongoDB
database instead of a local list.

* Add a class method called `make_connection` that establishes the connection
  to MongoDB.  Make sure that there is a class attribute called `collection` as
  that is needed by the test module.
* Add a method called `save` that saves the patient information to MongoDB.
* Add a class method called `find_by_mrn` that receives an integer mrn as an
  argument.  This method should return an instance of `Patient` with the 
  information found in the MongoDB for that mrn.  If the mrn does not exist,
  it should return `None`.
* Add a method called `delete` that deletes the current patient from MongoDB.

The test code below can be run using `pytest` and tests the CRUD functionality
of the modified `Patient` class.  

Make the modifications as described above such that all of the test functions
below pass.

Commit and push your completed files to your GitHub classwork repository.

### test_database_Patient.py
```python
# test_database_Patient.py
from database import Patient
import random

mrn = 0


def test_Patient_make_connection():
    Patient.make_connection()
    try:
        Patient.client.admin.command("ping")
        assert True
    except Exception as e:
        assert False


def test_Patient_create():
    global mrn
    mrn = random.randint(1, 1000000000000)
    patient = Patient("One", mrn, "1/1/2001")
    patient.save()
    answer = Patient.collection.find_one({"_id": mrn})
    assert answer is not None
    assert answer["_id"] == mrn
    assert answer["name"] == "One"


def test_Patient_retrieve():
    patient = Patient.find_by_mrn(mrn)
    assert patient is not None
    assert patient.mrn == mrn
    assert patient.name == "One"


def test_Patient_retrieve_not_found():
    patient = Patient.find_by_mrn(0)
    assert patient is None


def test_Patient_update():
    patient = Patient.find_by_mrn(mrn)
    test_result = ["HDL", 50.0]
    patient.tests.append(test_result)
    patient.save()
    answer = Patient.collection.find_one({"_id": mrn})
    assert answer["tests"] == [test_result]


def test_Patient_delete():
    patient = Patient.find_by_mrn(mrn)
    assert patient is not None
    patient.delete()
    answer = Patient.collection.find_one({"_id": mrn})
    assert answer is None


```