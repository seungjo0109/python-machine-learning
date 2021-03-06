## Types of Matrices
* A lot of linear algebra is concerned with operations on vectors and matrices, and there are many different types of matrices, There are many different types of matrices.

* There are a few types of matrices that you may encounter again and again when getting started in linear algebra, particularity the parts of linear algebra relevant to machine learning.

</br>

### 1. Square Matrix
* A square matrix is a matrix where the number of rows $(n)$ is equivalent to the number of column $(m)$.
* The square matrix is contrasted with the rectangular matrix where the number of rows and columns are not equal.
* Given that the number of rows and columns match, the dimensions are usually denoted as $n$, e.g. $n \times n$.
* The size of the matrix is called the order, so an order 4 square matrix is $4 \times 4$.
* The vector of values along the diagonal of the matrix from the top left to the bottom right is called the main diagonal.

</br>

* $M= \begin{pmatrix} 1  & 2 & 3\\1  & 2 & 3 \\ 1  & 2 & 3 \end{pmatrix}$


</br>


* Square matrices are readily added and multiplied together and are the basis of many simple linear transformations, such as rotations(as in the rotation of images).

</br>

### 2. Symmetric Matrix
* A symmetric matrix is a type of square matrix where the top-right triangle is the same as the bottom-left triangle.
* It is no exaggeration to say that symmetric matrices S are the most important matrices the world will ever see - in the theory of linear algebra and also in the applications.
* To be symmetric, the axis of symmetry is always the main diagonal of the matrix, from the top left to the bottom right.

</br>

* $M= \begin{pmatrix} 1  & 2 & 3 & 4 & 5\\2  & 1 & 2 & 3 & 4 \\ 3  & 2 & 1 & 2 & 3 \\ 4 & 3 & 2 & 1 & 2 \\ 5 & 4 & 3 & 2 & 1 \end{pmatrix}$

</br>

* A symmetric matrix is always square and equal to its own transpose. The transpose is an operation that flips the number of rows and columns.

</br>

* $M = M^T$

</br>

### 3. Triangular Matrix
* A triangular matrix is a type of square matrix that has all values in the upper-right or lower-left of the matrix with the remaining elements filled with zero values.
* A triangular matrix with values only above the main diagonal is called an upper triangular matrix. Whereas, a triangular matrix with values only below the main diagonal is called a lower triangular matrix.

</br>

* $M= \begin{pmatrix} 1  & 2 & 3\\0  & 2 & 3 \\ 0  & 0 & 3 \end{pmatrix}$

</br>

* NumPy provides functions to calculate a triangular matrix from an existing square matrix.
* The `tril()` function to calculate the lower triangular matrix from a given matrix and the `triu()` to calculate the upper triangular matrix from a given matrix.

</br>

[Triangular matrix example](./triangular_matrix.py)

</br>

### 4. Diagonal Matrix
* A diagonal matrix is one where values outside of the main diagonal have a zero value, where the main diagonal is taken from the top left of the matrix to the bottom right.
* A diagonal matrix is often denoted with the variable $D$ and may be represented as a full matrix or as a vector of values on the main diagonal.

</br>

* $D= \begin{pmatrix} 1  & 0 & 0\\0  & 2 & 0 \\ 0  & 0 & 3 \end{pmatrix}$

</br>

* A diagonal matrix does not have to be square. In the case of a rectangular matrix, the diagonal would cover the dimension with the smallest length
* NumPy provides the function `diag()` that can create a diagonal matrix from an existing matrix, or transform a vector into a diagonal matrix.

</br>

[Diagonal Matrix example](./diagonal_matrix.py)

</br>

### 5. Identity Matrix
* An identity matrix is a square matrix that does not change a vector when multiplied. The values of an identity matrix are known. All of the scalar values along the main diagonal (top-left to bottom-right) have the value one, while all other values are zero.
* An identity matrix is often represented using the notation $I$ or with the dimensionality $I^n$, where $n$ is a subscript that indicates the dimensionality of the square identity matrix.
* In some notations, the identity may be referred to as the unit matrix, or $U$, to honor the one value it contains (this is different from a Unitary matrix).
* In NumPy, an identity matrix can be created with a specific size using the `identity()` function.

</br>

[Identity matrix example](./identity.py)

</br>

### 6. Orthogonal Matrix
* Two vectors are orthogonal when their dot product equals zero. The length of each vector is 1 then the vectors are called orthonormal because they are both orthogonal and normalized.

$ v \cdot w = 0 $  or  $ v \cdot w^T = 0 $

* This is intuitive when we consider that one line is orthogonal with another if it is perpendicular to it.
* An orthogonal matrix is a type of square matrix whose columns and rows are orthonromal unit vectors, e.g. perpendicular and have a length or magnitude of 1.

* An orthogonal matrix is a square matrix whose rows are mutually orthonormal and whose are mutually orthnormal.

* Where $Q$ is the orthogonal matrix, $Q^T$ indicates the transpose of $Q$, and $I$ is the identity matrix. A matrix is orthogonal if its transpose is equal to its inverse.

* $Q^T = Q^{-1}$

* Orthogonal matrices are used a lot for linear transformations, such as relections and permutations.

[Orthogonal matrix example](./orthgonal_matrix.py)

</br>

* Running the example first prints the orthogonal matrix, the inverse of the orthogonal matrix, and the transpose of the orthogonal matrix are then printed and are shown to be equivalent.
* Finally, the identity matrix is printed which calculated from the dot product of the orthogonal matrix with its transpose.

</br>

### Reference: Basics of Linear Algebra for Machine Learning - Discover the Mathematical Language of Data in Python