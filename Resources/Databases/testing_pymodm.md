# Writing Unit Tests for PyMODM

Assume your code is set up in the following manner:
* You have a MongoModel class in a separate module called `db_class`, defined
  as follows:  
  ```python
  class User(MongoModel):
    name = fields.CharField(primary_key=True)
    age = fields.IntegerField()
  ```
* You have a module called `server.py` that contains the following functions:
  + `init_db()` that creates a `pymdodm.connect` connection with the MongoDB
    database
  + `add_user_to_db(user_info)` that takes a dictionary and adds the 
    information to the database
  + `find_user_in_db(user_name)` that retrieves information from the database
    and returns an instance of the `User` class
    
### Testing `add_user_to_db`
For testing addition to the database, you can use the `add_user_to_db` function
to add a test `User`, then, have the `add_user_to_db` function return what was
added to the database, and then you can delete the test entry.

When you use the `pymodm` `u.save()` command to save an entry to the database,
it returns what was saved to the database.  So, if you return this to the 
unit test, you can check to see that the entry was saved.  For example:

```python
def add_user_to_db(user_info):
    u = User(name=user_info["name"], age=user_info["age"])
    result = u.save()
    return result.name
```
Then, the unit test could look like this:
```python
def test_add_user_to_db():
    from server import add_user_to_db
    from db_class import User
    from server import init_db
    init_db()
    info_for_test = {"name": "Ann", "age": 25}
    answer = add_user_to_db(info_for_test)
    User.objects.raw({"_id": info_for_test["name"]}).first().delete()
    assert answer == info_for_test["name"]
```
It sends some user data to be stored in the database, and makes sure that the
information returned matches.  It also deletes the test entry so that the
test can be performed again later.

**NOTE**: The unit test above makes a connection with the database by calling
`init_db()`.  If you do this in every test function, your tests will take a
long time to run.  I would suggest putting the `from server import init_db` and
`init_db()` statements in the global section of the test module at the top.
This way, the connection is only made once and can be used by all unit tests.

### Testing `find_user_in_db`
This test is done in a similar manner.  First, a test entry is made to the 
database, and then the retrieve function is tested.  (It is assumed that the
database connection has already been made following the suggestion in the
**NOTE** above).

```python
def test_find_user_in_db():
    from server import find_user_in_db
    from server import add_user_to_db
    from db_class import User
    info_for_test = {"name": "Ann", "age": 25}
    test_user = User(name=info_for_test["name"], age=info_for_test["age"])
    test_user.save()
    answer = find_user_in_db(info_for_test["name"])
    User.objects.raw({"_id": info_for_test["name"]}).first().delete()
    assert answer == info_for_test
```
Some test information is added to the database.  Then, the function to be 
tested that retrieves the information is called, and the response from that
function is compared against the information sent.  Note, the assert statement
may need to be altered depending on what information the `find_user_in_db`
function returns.

