## Vector Norms
* Calculating the length or magnitude of vectors is often required either directly as a regularization method in machine learning, or as part of broader vector or matrix operations.
* In this tutorial, you will discover the different ways to calculate vector lengths or magnitudes, called the vector norm.

</br>

### 1. Vector Norm
* Caculating the size of length of a vector is often required either directly or as part of a broader vector or vector-matirx operation.
* The length of the vector is referred to as the vector norm or the vector's magnitude.
* The length of the vector is always a positive number, except for a vector of all zero values, It is calculated using some measure that summrizes the distance of the vector from the origin of the vector space.
* For example, the origin of a vector space for a vector with 3 elements is (0,0,0).
* Notations are used to represent the vector norm in broader calculations and the type of vector norm calculation almost always has its own uniquee notation.

</br>

### 2. Vector $L^1$ Norm
* The length of a vector can be calculated using the $L^1$ norm, where the 1 is a superscript of the $L$. The notation for the $L^1$ norm of a vector is $\lVert v \rVert_1 $, where 1 is a subscript.
* The $L^1$ norm is calculated as the sum of the absolute vector values, where the absolute value of a scalar uses the notation $\lvert a_1 \rvert$. 
* In effect, the norm is a calculation of the Manhattan distance from the origin of the vector space.

* $\lVert v \rVert_1 $ = $\lvert a_1 \rvert$ + $\lvert a_2 \rvert$ + $\lvert a_3 \rvert$

* In several machine learning applications, it is important to discriminate between elements that are exactly zero and elements that are samll but nonzero.
* In these cases, we turn to a function that grows at the same rate in all locations, but retains mathematical simplicity: the $L^1$ norm.

* The $L^1$ norm of a vector can be calculated in NumPy using the norm() function with a parameter to specify the norm order.

* The $L^1$ norm is often used when fitting mcahine learning algorithms as a regularization method, e.g. a method to keep the coefficients of the model small, and in turn, the model less complex.

</br>

[Vector L1 norm example](./vector_L1_norm.py)


</br>

### 3. Vector $L^2$ Norm
* The length of a vector can be calculated using the $L^2$ norm, where the 2 is a superscript of the $L$.
* The notation for the $L^2$ norm of a vector is $\lVert v \rVert_2$ where 2 is a subscript.
* $L^2(v) = \lVert v \rVert_2 $

* The $L^2$ norm calculates the distance of the vector coordinate from the origin of the vector space.
* As such, it is also known as the Euclidiean norm as it is calculated as the Euclidean distance from the origin.
* The result is a positive distance value.
* The $L^2$ norm is calculated as the square root of the sum of the squared vector values.
* $ \lVert v \rVert_2 = \sqrt{a_1^2 + a_2^2 + a_3^2} $
* Like the $L^1$ norm, the $L^2$ norm is often used when fitting machine learning algorithms as a regularization method, e.g. a method to keep the coefficients of the model small and, in turn, the model less complex.
* By far, the $L^2$ norm is more commonly used than other vector norms in machine learning.

</br>

[Vector L2 norm example](./vector_L2_norm.py)

</br>

### 4. Vector Max Norm
* The length of a vector can be calculated using the maximum norm, also called max norm.
* Max norm of a vector is referred to as $L^{inf}$ where inf is a superscript and can be represented with the infinity symbol.
* The notation for max norm is $ \lVert v \rVert_{inf} $, where inf is a subscript.

* $L^{inf}(v) = \lVert v \rVert_{inf} $

* The max norm is calculated as returning the maximum value of the vector, hence the name.
* $ \lVert v \rVert_{inf} = max  a_1, a_2, a_3 $
* The max norm of a vector can be calculated in NumPy using the norm() function with the order parameter set to inf.
* Max norm is also used as a regularization in machine learning, such as on neural network weights, called max norm regularization.

</br>

[Vector max norm example](./vector_max_norm.py)

</br>

### Reference: Basics of Linear Algebra for Machine Learning - Discover the Mathematical Language of Data in Python