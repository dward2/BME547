# Python Programming Assessment

This assessment is designed to help evaluate your initial understanding of basic
programming concepts within Python.  This assessment will not be formally
graded as this assessment is meant as a diagnostic to understand your current
level of knowledge.  However, the completion of this assessment will be part of
your participation grade.

Difficulty in completing some parts of this assessment will help indicate 
areas for additional study so that you are prepared for the
other assignments in this course.

Complete the following exercises in Python.
Upload the source code file(s) to the appropriate Canvas assignment.  Include
any comments you would like to share as comments within your code file.

If you cannot complete any part of these exercises, it is highly recommended 
that you review appropriate [Python Resources](Resources/python.md) to gain 
the required knowledge to complete the exercise.  Please feel free to contact
the instructor for guidance.

## Exercise One
Write a Python script that does the following: 
* Creates a list that contains with the following strings and assigns this list
  to a variable:
  + apple
  + banana
  + cranberry
  + date
  + eggplant
  + fennel
  + guava
* You can read in the words above from a data file or manually hard-code them
  into your variable.
* Write code that will parse the data in the variable above and create two new 
  variables, each of which contains a new list.  One of these new
  variables should contain all the strings from the list above with five 
  characters or less.  The second new variable should contain all the strings 
  with six characters or more.
* For each of the two new variables, write code that will output each string,
  on its own line, to either the screen or an output file.
  
## Exercise Two
In a Python code file, complete the following:
* Write a function that receives a number as a parameter and returns a boolean
  of `True` if the parameter is positive and returns `False` if not.
* Write a function that accepts three parameters (`a`, `b`, and `c`) and
  returns the two solutions to the quadratic formula.  You can ignore complex
  numbers for this assignment and assume that the values of `a`, `b`, and `c`
  will always yield two real roots.
* Write a program that 
  + accepts three inputs `a`, `b`, and `c` as either input from the keyboard, 
    input from a file, or entered directly into the code as variables,
  + uses the two functions developed above to determine whether the roots of 
    the quadratic equation based on the three inputted parameters 
    are of the same sign (i.e., both positive or negative), and
  + outputs the answer (same sign or different sign) to either the screen or
    a file.  

## Exercise Three
In a Python code file, complete the following:
* Write a function that receives a parameter.  
  * If the parameter is a number, assume it is the radius of a circle, 
    calculate the area of the circle based on that radius, and return that 
    value.
  * If the parameter is a string, return the first letter of the string.
* Test this function by calling it with various inputs for the parameter.

## Exercise Four
Assume you have the following data:

<table>
  <tr>
    <th>Name</th>
    <th>Patient ID</th>
  </tr>
  <tr>
    <td>Ann Ables</td><td>12</td>
  </tr>
  <tr>
    <td>Bob Boyles</td><td>25</td>
  </tr>
  <tr>
    <td>Chris Chou</td><td>43</td>
  </tr>
</table>

In a Python code file, complete the following:
* Create a variable with an empty list.
* Use the `.append()` method to populate this list with the data above where
  each item in the list is of the form: `[name, id]`.
* Show how you would print out the patient id of Bob Boyles from this list.

## Exercise Five
In a Python code file, complete the following:
* Create a variable that contains the following list:  
  `[-5, 10, 3, 4, 22, 'a', None]
* Write code that will create a new list that contains only the even numbers
  from this list and sorted into ascending order.
* Print out this list.