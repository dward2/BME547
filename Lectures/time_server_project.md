# Mini-Project:  Time Server

Develop a server with the following endpoints:

* `GET URL/time`
  + returns the current time (see below for info on using dates and times with 
  Python)
* `GET URL/date`
  + returns the current date
* `POST URL/age`
  + receives a JSON in the following format:  
  `{'date': "10/10/1999", 'units': "years"}`
  + returns the length of time between the given date and the current time.
  + The default return units should be years.  If you want to learn more
  about times, allow for different units to be entered and return the results
  in the given units.
 * `GET URL/until_next_meal/<meal>`
   + where `<meal>` could be `breakfast`, `lunch`, or `dinner`.  
   + Returns the number of hours until that meal.
   
### Python Date and Time
The `datetime` package (<https://docs.python.org/3/library/datetime.html>) is
a native Python package that can be imported as follows:

`from datetime import datetime`

#### Getting current date/time

`datetime.now()` returns a `datetime` object that contains the 
current date and time.

`datetime.now().date()` returns a `datetime` object that contains the current
date.  

`datetime.now.time()` returns a `datetime` object that contains the current 
time.

#### Specifying a specific date/time
`datetime(2010, 2, 14, 18, 5, 13)` returns a `datetime` object that contains
the date and time defined by the parameters in the following order: year,
month, date, hour (24 hr clock), minutes, seconds.

#### Convert `datetime` object to `str`

`datetime.strftime(datetime_variable, "%m-%d-%y %H:%M:%S")` converts the 
`datetime_variable` into a string with format given by the specified format
string.  Example:
```
x = datetime(2010, 2, 14, 18, 5, 13)
y = datetime.strftime(x, "%m-%d-%y %H:%M:%S")
print(y)   # Output: 02-14-10 18:05:13 
```
The `strftime` command is short for `str`ing `f`rom `time`.  Additional 
information on the string formatting can be found at 
<https://docs.python.org/3/library/datetime.html#strftime-and-strptime-format-codes>

#### `timedelta` objects
The difference between two times is captured in a `timedelta` object.  Example:
```
a = datetime(2019, 10, 20)
b = datetime(2018, 10, 20)
c = a - b
print(type(c))  # Output:  <class 'datetime.timedelta'>
print(c)        # Output:  365 days, 0:00:00
print(c.days)   # Output:  365

d = datetime(2019, 10, 20, 13, 5, 35)
e = datetime(2019, 10, 20, 15, 22, 55)
f = e - d
print(f.seconds)  # Output: 8240
```

Note that there also objects to just contain the `date` and `time`.  See
the documentation at <https://docs.python.org/3/library/datetime.html> for
more information.
