# SQL Databases
Relational databases, often called SQL databases, have a pre-defined structure 
(called a schema)
that allows for "relationships" to be drawn between different sets of data.
The data tables and variable types in these data tables are pre-defined, which
can improve the efficiency and size of the database.  The
data tables consist of rows (records) and columns (fields).
  
SQL (Structured Query Language) is used to create, access, and manipulate the
data in the database.  Most databases have type checking to ensure that data
being entered into the database matches the requirements.

There are a variety of options for setting up an SQL database.  This page will
discuss using [SQLite](https://www.sqlite.org/index.html) within Python.
SQLite is a small, self-contained, serverless SQL database engine.  Its use
cases include:
* when a device needs to implement an SQL database but does not
need the scale or cloud-access that a server-based SQL database
* as a development tool to test prototpye code before scaling it up
to a larger SQL database server.

## SQLite3
`sqlite3` is a Python package that provides access to SQLite functionality.
Python documentation for `sqlite3` can be found 
[here](https://docs.python.org/3.8/library/sqlite3.html).

## SQL Commands
A basic understanding of SQL commands is needed for effective use of `sqlite3`.
An excellent tutorial/reference guide for SQL can be found at 
<https://www.w3schools.com/sql/default.asp>.  

## Examples
The following code snippets are taken from a Python program that sets up an 
SQLite database for a financial program.
###  Creating a database and initial tables
```
import sqlite3

db = sqlite3.connect("database_file_name.db")
db_cursor = db.cursor()
db_cursor.execute("CREATE TABLE AccountTypes (Account_Type TEXT)")
db_cursor.execute("CREATE TABLE ChartOfAccounts (Name TEXT, Type TEXT, Description TEXT)")
db_cursor.execute("CREATE TABLE GeneralLedger (ID INTEGER PRIMARY KEY, " +
                  "Date DATE, " +
                  "Description TEXT, Amount REAL, " +
                  "DebitAccount TEXT, CreditAccount TEXT, " +
                  "BankReference TEXT)")
db.commit()
db.close()

```
* `import sqlite3` imports the Python package.
* `db = sqlite3.connect("database_file_name.db")` opens a database connection to
the file specified and stores it in the `db` variable.  If the file does not 
exist, it is created. 
* `db_cursor = db.cursor()` creates a cursor object for the `db` database
connection.  This cursor object is used to interact with the database.
* `db_cursor.execute(SQL_string)` executes the SQL commands given in the 
SQL_string.  In the code above, three different tables are created.  The 
basic SQL command for creating a table is:
  + `CREATE TABLE TableName (Column1 COLUMN1TYPE, Column2 COLUMN2TYPE)` where
  `TableName` is the user defined table name, `Column1` is the name of the 
  first data column, `COLUMN1TYPE` is the SQL data type for the first column,
  etc.  There can be as many columns as desired by the user.
  + ColumnTypes can include: INTEGER, REAL, TEXT.  `sqlite3` in python also has 
  a DATE type.
  + `PRIMARY KEY` after a column Type sets that column to be a column that
  cannot have duplicated entries.
* While the `execute` command does make changes to the datbase, those changes
are not observable to other database users until the `db.commit()` command is
given.
* `db.close()` closes the connection to the database.

### Adding an entry to a table
The examples below all assume that `db.connect()`, and `db_cursor = db.cursor()`
have already been executed.  And, that `db.commit()` and `db.close()` will be
done after.

```
db_cursor.execute("INSERT INTO AccountTypes VALUES ('Bank')")
db_cursor.execute("INSERT INTO ChartOfAccounts VALUES ('Bank of America', 'Bank', 'Checking Account')
db_cursor.execute("INSERT INTO GeneralLedger (Date, Description, Amount) VALUES ('1/10/95', 'Check No 1456', '25.43')")
```
* The general SQL string for adding an item to a table is:
  + `INSERT INTO TableName VALUES (Col1Value, Col2Value)` where
  + `TableName` is the table name into which to insert
  + `Col1Value`, `Col2Value` etc. are the values to be inserted into each column.
  There should be as many column values as there are columns defined in the 
  `CREATE TABLE` command.
  + If you only want to enter some columns, you include a list of the columns
  you want to add data to.  
  For example: `INSERT INTO TableName (Column1, Column2) VALUES (Col1Value, Col2Value)`
  + For `INTEGER PRIMARY KEY` fields, if an entry is not specified, the next
  highest integer will be automatically added.
  
### Getting items from a table
```
db_cursor.execute("SELECT * FROM AccountTypes")
acct_types = db_cursor.fetchall()

db_cursor.execute("SELECT * FROM ChartOfAccounts WHERE Name='Bank of America')
bank_acct_info = db_cursor.fetchall()

db_cursor.execute("SELECT Date, Amount FROM GeneralLedger")
transaction_info = db_cursor.fetchall()
```  
* The general SQL string for retreiving items from a table is:
  + `SELECT ColumnA, ColumnB FROM TableName WHERE ColumnC=Value`
  + After `SELECT`, list the columns from the table to be retrieved.  If all of
  the columns are desired, simply enter `*`
  + If you want only data that meets certain conditions, include those after 
  the `WHERE` clause in the form of `ColumnName=Value` where `Value` is the
  conditions to search for.  If you want all entries in the table, do not
  include a `WHERE` clause.
* `db_cursor.fetchall()` returns a list of the retrieved data from the table.
  
### Updating an existing record
```
db_cursor.execute("UPDATE GeneralLedger SET BankReference='Deposit', CreditAccount="Expenses" WHERE ID=2")
```
* The general SQL string for updating items in a table is:
  + `UPDATE TableName SET Column1=Col1Value, Column2=Col2Value WHERE Column3=Value`
  + You can include as many columns after `SET` as needed
  + All entries in the table that meet the `WHERE` condition will be updated.  So,
  be sure you have a search in the `WHERE` column that is targeted to your needs.
  
### Deleting an entry
```
db_cursor.execute("DELETE FROM GeneralLedger WHERE ID=2")
```
* The general SQL string for deleting items in a table is:
  + `DELETE FROM TableName WHERE Column1=Value`
  
### Foreign Key Support
To activate Foreign Key Support, include the following:
```
db_cursor.execute("PRAGMA foreign_keys = ON")
```
You can check status of foreign key activation by:
```
rows = db_cursor.execute("PRAGMA foreign_keys")
print("rows: {}".format(rows))
for i in rows:
    print(i)
    
# (0,) means off
# (1,) means on
```