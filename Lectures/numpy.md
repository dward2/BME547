# NumPy
## Introduction
NumPy is a Python package for scientific computing that contains:
* multi-dimensional arrays and supporting functions
* basic linear algebra functions
* basic Fourier transforms

Intended to improve easy and efficiency of data handling and calculation.

## Importing NumPy
The `numpy` package must be installed in your virtual environment.  Then, in
the Python code, it can be imported as follows: 
```
import numpy as np
```
Then, functions can be called using `np` such as:
```
a = np.array([0, 1, 2, 3])
```

## Creating NumPy Arrays
### `array()`
Array like structures in python can be converted to NumPy array as follows:
```
x = np.array([1, -3, 5, 10])

a = [0, 2, 10, -3, 2.5]
print(type(a))
    <class 'list'>
b = np.array(b)
print(type(b))
    <class 'numpy.ndarray'>
```
### `zeros()` and `ones()`
Will create an array filled with either zeros or ones of  type `float`.
```
a = np.zeros((2, 3))
print(a)
    [[0. 0. 0.]
     [0. 0. 0.]]
```

### `arange()`
Will create an array with regularly incrementing values.  Examples:
```
a = np.arange(10)
print(a)
    [0 1 2 3 4 5 6 7 8 9]

b = np.arange(2, 4, 0.2)
print(b)
    [2.  2.2 2.4 2.6. 2.8 3.  3.2 3.4 3.6 3.8]
```
### `linspace()`
Will create an array with a specified number of elements with the values
being equally spaced between the specified beginning and ending values.
```
a = np.linspace(1., 4., 6)
print(a)
    [1.  1.6 2.2 2.8 3.4 4. ]
```

## Array Indexing
### 1-D arrays
Assume x is the following numpy array:
```
[2 3 4 5 6 7 8 9 10 11]
```
The indeces of the values in the array run from 0 to the array length -1.  So,
```
a[0] = 2
a[2] = 4
a[9] = 11
``` 
You can also count backwards from the end of the array with the `-1` index
being the last element of the array.
```
a[-1] = 11
a[-3] = 9
```
You can index sections of an array:
```
a[3:6] = [5 6 7]
```

### 2-D Arrays
Assume `x` is the following array:
```
[[ 0.  1.  2.  3.]
 [ 4.  5.  6.  7.]
 [ 8.  9. 10. 11.]
 [12. 13. 14. 15.]]
 
 x[1, 3] = 7.0
 x[3, 1] = 13.0
 x[2, -1] = 11.0
 x[2] = [8. 9. 10. 11.] (or X[2,:]
 x[:,2] = [ 2. 6. 10. 14.]
 ```

## Equality of Numpy Arrays
When working on a numpy array, any action performed on the array is generally
applied to each element of the array to yield another array.  For example:

```python
array_1 = np.array([1, 2, 3, 4])
added_array = array_1 + 3
print(added_array)
```
yields the output:
```
[4 5 6 7]
```
The `+` operand operated on each element of the array to create a new array.

The equality or `==` operator does the same.  Example:
```python
array_1 = np.array([1, 2, 3, 4])
array_2 = np.array([1, 2, 3, 4])
print(array_1 == array_2)
```
yields the output
```
[ True  True  True  True]
```
Whereas in this example:
```python
array_1 = np.array([1, 2, 3, 4])
array_2 = np.array([1, 6, 3, 4])
print(array_1 == array_2)
```
yields the output
```
[ True False  True  True]
```
The `==` comparison actually compares each element of the two arrays and 
creates a new array with the results for each comparison.

What happens if we try to compare two numpy arrays within a unit test.  The
code `assert array_1 == array_2` confuses Python because `assert` is supposed
to receive a single boolean, not an array of booleans.  So,  you will get an
error that says: `ValueError: The truth value of an array with more than one 
element is ambiguous. Use a.any() or a.all()`.  

What is "ambiguous" is whether the test should pass if all elements of the
array are true or if it should pass if any one of the elements in the array is 
true.    

That is where `.all()`. and `.any()` come in.  If `.all()` is applied to this 
list of booleans, then all the values in the list must be true for the overall 
comparison to be true.  If `.any()` is applied to this list, only one needs to 
be true to yield the overall comparison to be true.

Examples:
```python
x = (np.array([1, 2, 3, 4]) == np.array([1, 2, 3, 4])).all()  # x is True
y = (np.array([1, 2, 3, 4]) == np.array([1, 2, 3, 4])).any()  # y is True

z = (np.array([1, 2, 6, 4]) == np.array([1, 2, 3, 4])).all()  # z is False
m = (np.array([1, 2, 6, 4]) == np.array([1, 2, 3, 4])).any()  # z is True
```
In the example above, I am using the `.all()` and `.any()` methods.  But, you can also use the `np.all()` or `np.any()` functions such as:
```python
n = np.all(np.array([1, 2, 6, 4]) == np.array([1, 2, 3, 4]))  # n is False
p = np.any(np.array([1, 2, 6, 4]) == np.array([1, 2, 3, 4]))  # p is True
```
  
 
 ## References
 * https://docs.scipy.org/doc/numpy/user/basics.html