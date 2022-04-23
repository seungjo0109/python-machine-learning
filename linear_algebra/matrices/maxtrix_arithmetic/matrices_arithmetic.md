## Matrix Arithmetic
* Matrices are a foundational element of linear algebra. 
* Matrices are used throughout the field of machine learning in the description of algorithms and processes such as the input data variable $(X)$ when training algorithm.

</br>

### 1. What is a Matrix
* A matrix is a two-dimensional array of scalars one or more columns and one or more rows.
* A matrix is a two-dimensional array (a table) of numbers.
* The notation for a matrix is often an uppercase letter, such as $A$, and entries are referred to by their two-dimensional subscript of row $(i)$ and clumn $(j)$, such as $a_{ij}$.

</br>

* $ A = ((a_{1,1}, a_{1,2}), (a_{1,2}, a_{2,2}), (a_{3,1}, a_{3,2}))$

</br>

* It is more common to see matrices defined using a horizontal notation.

</br>

* $A= \begin{pmatrix} a_{1,1} & a_{1,2}\\a_{2,1} & a_{2,2} \\ a_{3,1} & a_{3,2}   \end{pmatrix}$

</br>

* A likely first place you may encounter a matrix in machine learning in model training data comprised of many rows and columns and often represented using the capital letter $X$.
* The geometric analogy used to help undertand vectors and some of their operations does not hold with matrices.
* Futher, a vector itself may be considered a matrix with one column and multiple rows.

</br>

### 2. Defining a Matrix
* We can represent a matrix in Python using a two-dimensional NumPy array.
* A NumPy array can be constructed given a list of lists.

</br>

[Defining matrix example](./defining_matrix.py)

</br>

### 3. Matrix Arithmetic
* In this section will demonstrate simple matrix-matirx arithmetic, where all operations are performed element-wise between two matrices of equal size to result in a new matrix with the same size.

</br>

### 3.1. Matrix Addition
* Two matrices with the same dimension  can be added together to create a new third matirx

</br>

* $ C = A + B$

</br>

* The scalar elements in the resulting matrix are calculated as the addition of the elements in each of the matrices being added.

</br>

* $C= \begin{pmatrix} a_{1,1} + b_{1,1} & a_{1,2} + b_{1,2}\\a_{2,1} + b_{2,1} & a_{2,2} + b_{2,2} \\ a_{3,1}+ b_{3,1} & a_{3,2}+ b_{3,2}   \end{pmatrix}$

</br>

### 3.2. Matrix Substraction
* Similarly, one matrix can be substracted from another matrix with the same dimensions.

</br>

* $ C = A - B$

</br>

* * $C= \begin{pmatrix} a_{1,1} - b_{1,1} & a_{1,2} - b_{1,2}\\a_{2,1} - b_{2,1} & a_{2,2} - b_{2,2} \\ a_{3,1} - b_{3,1} & a_{3,2} - b_{3,2}   \end{pmatrix}$

</br>

### 3.3. Matrix Multiplication (Hadamard Product)
* Two matrices with the same size can be multiplied together, and this is often called element-wise matrix multiplication or the Hadamard product.
* It is not the typical operation meant when referring to matrix multiplication, therefore a different operator is often used, such as a circle 

</br>

* $ C = A \circ B $

</br>

* As with element-wise substraction and addition, element-wise multiplication invloves the multiplcation of elements from each parent matrix to calculate the values in the new matrix.

</br>

* $C= \begin{pmatrix} a_{1,1} \times b_{1,1} & a_{1,2} \times b_{1,2}\\a_{2,1} \times b_{2,1} & a_{2,2} \times b_{2,2} \\ a_{3,1} \times b_{3,1} & a_{3,2} \times b_{3,2}   \end{pmatrix}$

</br>

### 3.4. Matrix Division
* One matrix can be divided by another matrix with the same dimensions.

</br>

* $C = \frac{A}{B}$

</br>

* $C= \begin{pmatrix} \frac{a_{1,1}}{b_{1,1}} & \frac{a_{1,2}}{b_{1,2}} \\\frac{a_{2,1}}{b_{2,1}} & \frac{a_{2,2}}{b_{2,2}} \\ \frac{a_{3,1}}{b_{3,1}} & \frac{a_{3,2}}{b_{3,2}}   \end{pmatrix}$

</br>

[Matrix arithmetic example](./matrix_arithmetic.py)

</br>

### Reference: Basics of Linear Algebra for Machine Learning - Discover the Mathematical Language of Data in Python