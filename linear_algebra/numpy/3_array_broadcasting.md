## NumPy Array Broadcasting
* Arrays with differenct sizes cannot be added, substracted, or generally be used in arithmetic.
* A way to overcome this is to duplicate the smaller array so that it has the dimensionality and size as the larger array.
* This is called array broadcasting and is availalble in NumPy when performing array arithmetic, which can greatly reduce and simplify your code.
* In this tutorial, you will discover the concept of array broadcasting and how to implement it in NumPy.

</br>

### 1. Limitation with Array Arithmetic
* You can perform arithmetic directly on NumPy arrays, such as addition and abstraction.
* For example, two arrays can be added together to create a new array where the values at each index are added together.
* Strictly, arithmetic may only be performed on arrays that have the same dimensions and dimensions with the same size.
* This means that a one-dimensional array with the length of 10 can only perform arithmetic with another one-dimensional array with the length 10.
* This limitation on array arithmetic is quite limiting indeed. Thankfully, NumPy provieds a built-in workaround to allow arithmetic between arrays with differing sizes.

</br>

### 2. Array Broadcasting
* Braodcasting is the name given to the mothod that NumPy uses to allow array arithmetic between arrays with a different shape or size.
* Although the technique was developed for NumPy, it has also been adopted more broadly in other numerical computational libraries, such as Theano, TensorFlow, and Octave.
* Broadcasting solves the problem of arithmetic between arrays of differing shapes by in effect replicating the smaller array along the last mismatched dimension.

</br>

* NumPy does not actually duplicate the smaller array; instead, it makes memory and computationally efficient use of existing structures in memory that in effect achieve the same result.
* The concept has also permeated linear algebra notation to simplify the explanation of simple operations.

</br>

### 3. Broadcasting in NumPy
* We can make broadcasting concrete by looking at three examples in NumPy.

</br>

### 3.1. Scalar and One-dimensional Array
* A single value or scalar can be used in arithmetic with a one-dimensional array.
* Running the example first prints the defined one-dimensional array, then the scalar, followed by the result where the scalar is added to each value in the array.

</br>

### 3.2. Scalar and Two-Dimensional Array
* A scalar value can be used in arithmetic with a two-dimensional array.
* Running the example first prints the defined two-dimensional array, then the scalar, then the result of the addition with the value 2 added to each value in array.

</br>

### 3.3. One-Dimensional and Two-Dimensional Arrays
* A one-dimensional array can be used in arithmetic with a two-dimensional array.
* The one-dimensional array is broadcast across each row of the tow-dimensional array by creating a second copy to result in a new two-dimensional array B.
* Running the example first prints the defined two-dimensional array, then the defined one-dimensional array, following by the result arr_3D where in effect each value in the two-dimensional array is doubled.

</br>

### 4. Limitation of Broadcasting
* Broadcasting is a handy shortcut that proves very useful in practice when working with NumPy arrays. That being said, it does not work for all cases, and in fact imposes a strict rule that must be satisfied for broadcasting to be performed.
* Arithmetic, including broadcasting, can only be performed when the shape of each dimension in the arrays are equal or one has the dimension size of 1.
* The dimensions are considered in reverse order, starting with the trailing dimension; for example, looking at columns before rows in a two-dimensional case.
* This make more sense when we consider that NumPy will in effect pad missing dimensions with a size of 1 when comparing arrays.

</br>

### [Array broadcasting example](./array_broadcasting.py)

</br>

### Reference: Basics of Linear Algebra for Machine Learning - Discover the Mathematical Language of Data in Python