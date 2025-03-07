# mongo_db_example.py
# David Ward, March 2025

from pymongo import MongoClient


def init_mongo_db():
    """
    The <connect_string> below should be replaced by the one provided for you
    by MongoDb.  Make sure that the <db_username> and <db_password> have all
    been replaced by the appropriate entries.
    """
    uri = "<connect_string>"
    client = MongoClient(uri)
    database = client["pymongo_demo"]
    user_collection = database["users"]
    return user_collection


def add_new_user(user_collection, email_arg, first_name_arg, last_name_arg,
                 age_arg):
    """
    The user e-mail will be used as the unique id in MongoDB
    """
    new_user = {
        "_id": email_arg,
        "first_name": first_name_arg,
        "last_name": last_name_arg,
        "age": age_arg
    }
    user_collection.insert_one(new_user)
    print("Saved to database")


def get_users(user_collection):
    for user in user_collection.find():
        print("E-mail: {}".format(user["_id"]))
    return


if __name__ == '__main__':
    user_collection = init_mongo_db()
    add_new_user(user_collection, "awaxye@yahoo.com", "Adam", "Wax", 30)
    add_new_user(user_collection, "david.a.ward@duke.edu", "David", "Ward",
                 "45")
    get_users(user_collection)
