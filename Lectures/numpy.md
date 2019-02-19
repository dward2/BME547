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
 
 ## References
 * https://docs.scipy.org/doc/numpy/user/basics.html