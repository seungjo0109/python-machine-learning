## Vectors and Vector Arithmetic
* Vectors are a foundational element of linear algebra. Vectors are used throughout the filed of machine learning in the description of algorithms and processed such as the target variable ($y$) when training an algorithm.

</br>

### 1. What is a Vector
* A Vector is a tuple of one or more values called scalars.
* Vectors are often represented using a lowercase character such as $v$; for example:
<br>$v = (v_1, v_2, v_3)$

* Where $v_1, v_2, v_3$ are scalar values, often real values.
* Vectors are also shown using a vertical representaion or a column.
* It is common to represent the target variable as a vector with the lowercase $y$ when describing the training of a machine learning algorithm.
* It is commonm to introduce vectors using a geometric analogy, where a vector represents a point or coordinate in an n-dimensional space, where $n$ is the number of dimensions.
* The vector can also be thought of as a line from the origin of the vector space with a direction and a magnitude.

</br>

### 2. Defining a Vector
* We can represent a vector in Python as a NumPy array.
* A NumPy array can be created from a list of numbers.

</br>

[Defining vector example](./defining_vector.py)

</br>

### 3. Vector Arithmetic
* In this section will demostrate simple vector-vector arithmetic, where all operations are performed element-wise between two vectors of equal length to result in a new vector with the same length.

</br>

### 3.1. Vector Addition
* Two vectors of equal length can be added together to create a new third vector.
<br>$c = a + b$

* The new vector has the same length as other two vectors. Each element of the new vector is calculated as the addition of the elements of the other vectors at the same index

</br>

### 3.2. Vector Substraction
* On vector can be substracted from another vector of equal length to create a new third vector.
<br>$c = a - b$

* As with addition, the new vector has the same length as the parent and each element of the new vector is caculated as the subsctraction of the elements at the same indices.
<br>$c = (a_1 - b_1, a_2 - b_2, a_3 - b_3)$

</br>

### 3.3. Vector Multiplication
* Two vectors of equal length can be multiplied together.
<br>$c = a \times b$

* As with addition and substraction, this operation is performed element-wise to in a new of the same length.
<br>$c = (a_1 \times b_1, a_2 \times b_2, a_3 \times b_3)$

</br>

### 3.4. Vector Division
* Two vectors of equal length can be deivided.
<br> $c = \frac{a}{b}$

* As with other arithmetic operations, this operation is performed element-wise to result in a new vector of the same length.
<br>$c = (\frac{a_1}{b_1}, \frac{a_2}{b_2}, \frac{a_3}{b_3})$

</br>

[Vector Arithmetic example](./vector_arthmetic.py)

</br>

### 4. Vector Dot Product
* We can calculate the sum of the multiplied elements of two vectors of the same length to giva a scalar. This is called the dot product, named because of the dot operator used when describing the operation.

* $c = a \cdot b$
* $c= (a_1 \times b_1 + a_2 \times b_2 + a_3 \times b_3) $

</br>

[Vector dot product](./vector_dot_product.py)

### 5. Vector-Scalar Multiplication
* A vector can be multiplied by a scalar, in effect scailing the magnitude of the vector. To keep notation simple, we will use lowercase $s$ to represent the scalar value.
* $c = s \times v$
* $c= (s \times v_1, s \times v_2, s \times v_3) $

</br>

### Reference: Basics of Linear Algebra for Machine Learning - Discover the Mathematical Language of Data in Python