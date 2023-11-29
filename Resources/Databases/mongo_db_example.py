# mongo_db_example.py
# David Ward, April 2019

from pymodm import connect, MongoModel, fields


def init_mongo_db():
    connect("mongodb+srv://<username>:<password>@<yourclustername>-nlfrn.mongodb.net/<dbname>?retryWrites=true")
    """
    The connect string above should be replaced by the one provided for you
    by MongoDb.  Make sure that the <username>, <password>, <yourclustername>,
    and <dbname> have all been replaced by the appropriate entries.
    Note that the connect string provided by MongoDB may not have a placeholder
    for the <dbname> in which case you will need to add the database name
    yourself.
    
    When running this program, if you get an error such as 
    "ServerSelectionTimeoutError" or "SSL:CERTIFICATE_VERIFY_FAILED], you will
    need to modify the "connect" command as follows:
    
    connect(<your connect string>, tlsAllowInvalidCertificates=True)
    """


class User(MongoModel):
    email = fields.EmailField(primary_key=True)
    first_name = fields.CharField()
    last_name = fields.CharField()
    age = fields.IntegerField()


def add_new_user(email_arg, first_name_arg, last_name_arg, age_arg):
    u = User(email=email_arg,
             first_name=first_name_arg,
             last_name=last_name_arg,
             age=age_arg)
    u.save()
    print("Saved to database")


def get_users():
    for user in User.objects.raw({}):
        print(user.email)
    return


if __name__ == '__main__':
    init_mongo_db()
    add_new_user("awaxye@yahoo.com", "Adam", "Wax", 30)
    add_new_user("david.a.ward@duke.edu", "David", "Ward", "45")
    get_users()
