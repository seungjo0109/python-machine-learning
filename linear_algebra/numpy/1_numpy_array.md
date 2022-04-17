## Introduction to Numpy Arrays
* Arrays are the main data structure used in machine learning. In python, arrays from the NumPy library, called N-dimensional arrays of the __ndarray__, are used as the primary data structure for representing data.

</br>

### 1. NumPy N-dimensional Array
* Numpy is a Python library that can be used for scientific and numerical applications and is the tool to use for linear algebra operations.
* The main data structure in NumPy is the ndarray, which is a shorthand name for N-dimensional array.
* When working with NumPy, data in an __ndarray__ is simply referred to as an array. It is a fixed-sized array in memory that contains data of the same tpye, such as integers or floating point values.

</br>

### [Simple numpy array example](./simple_array.py)

</br>


### 2. Function to Create Arrays

* There are more convenience functions for creating fixed-sized arrays that you may encounter or be required to use.

</br>

### 2.1 Empty
* The empty() function will create a new array of the specified shape.
* The argument to the function is an array or tuple that specifies the length of each dimenstion of the array to create.
* The values or content of the created array will be random and will need to be assigned before use.

</br>

### 2.2 Zeros
* The zeros() function will create a new array of specified size with the contents filled with zero values.
* The argument to the function is an array or tuple that specifies the length of each dimension of the array to create.

</br>

### 2.3 ones
* The ones() function will create a new array of the specified size with the contents filled with on values.
* The argument to the function is an array or tuple that specifies the length of each dimension of the array to create.

</br>

### [Create array function example](./function_crate_array.py)

</br>

## 3. Combining Arrays

* Numpy provides many functions to create new arrays from existing arrays.
* Let's look at two of the most pupular functions you may need or encounter.

</br>

## 3.1 Vertical Stack
* Given two or more existing arrays, you can stack them vertically using the vstack() function.
* For example, given two one-dimensional arrays, you can create a new two-dimensional array with two rows by vertically stacking them.

## 3.2 Horizontal Stack
* Given two or more existing arrays, you can stack them horizontally using the hstack() function.
* For example, given two on-dimensional arrays, you can create a new one-dimensional array or one row with the columns of the first and second arrays concatenated.

</br>

### [Combining arrays example](./combining_array.py)

</br>

### Reference: Basics of Linear Algebra for Machine Learning - Discover the Mathematical Language of Data in Python