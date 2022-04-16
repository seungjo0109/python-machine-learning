## Linear Algebra in Machine Learning

* Linear algebra is a sub-field of mathematics concerned with vectors, matrices and linear transformations.
* It is a key foundation to the field of machine learning from notations used to describe the operation of algorithms, to the implementations of algorithms in code.
* we will review 10 obvious and concrete examples of linear algebra in machine learning.

    1. Dataset and Data Files
    2. Images and Photographs
    3. One Hot Encoding
    4. Linear Regression
    5. Regularization
    6. Principle Component Analysis
    7. Singular-Value Decomposition
    8. Latent Semantic Analysis
    9. Recommander Systems
    10. Deep Learning

</br>

### 1. Dataset and Data Files
* In machine learning, you fit a model on a dataset. This is the table like set of numbers where each row represents an observation and each column represents a feature of the observation.

</br>

```
5.1, 3.5, 4, 0.2, Iris-setosa
4.9, 3.4, 3, 0.2, Iris-setosa
5.2, 3.6, 5, 0.2, Iris-setosa
5.3, 3.1, 3, 0.2, Iris-setosa
5.0, 3.2, 4, 0.2, Iris-setosa
...
```

</br>

* This data is in fact a matrix, a key data structure in linear algebra. 
* Further, when you split the data into inputs and outputs to fit a supervised machine learning model, such as the measurements and the flower species, you have a matrix $(X)$ and a vector $(y)$. The vector is another key data structure in linear algebra.

</br>

### 2. Images and Phorographs
* Perhaps you are more used to working with images or photographs in computer vision applications. Each image that you work with is itself a table structure with a width and height and one pixel value in each cll for black and white images or 3 pixel values in each cell for a color image.
* A photo is yet another example of a matrix from linear algebra.
* Operations on the images, such as cropping, scaling, shearing and so on are all described using the notation and operations of linear algebra.

</br>

### 3. One Hot Encoding
* Sometimes you work with categorical data in machine learning. Perhaps the class labels for classification problems, or perhaps categorical input variables.
* It is common to encode categorical variables to make their easier to work with and learn by some techniques.
* A popular eoncoding for categorical variables is the one hot encoding. A one hot encoding is whrere a table is created to represent the variable with one column for each category and a row for each example in the dataset.

</br>

``` python
# categorical variable
red
green
blue

# one hot encoded categorical variable
red, green, blue
  1,     0,    0
  0,     1,    0
  0,     0,    1
```

</br>

* Each row is encoded as a binary vector, a vector with zero or one values and this is an example of a sparse representation, a whole sub-field of linear algebra.

</br>

### 4. Linear Regression
* Linear regression is an old method from statistics for describing the relationships between variables.
* It is often used in machine learning for predicting numerical values in simpler regression problems.
* There are many ways to describe and solve the linear regression problem, i.e. finding a set of coefficients that when multiplied by each of the input variables and added together results in the best prediction of the output variable.
* If you have used a machine learning tool or library, the most common way of solving linear regression is via a least squares optimization that is solved using matrix factorization methods from linear regression, such as an LU decomposition or an singular-value decomposition or SVD.

</br>

### 5. Regularization
* In applied machine learning, we often seek the simplest possible models that achieve the best skill on our problem.
* Simpler models are often better at generalizing from specific examples to unseen data.
* In many methods that involve coefficients, such as regression methods and artificial neural networks, simpler models are often characterized by models that have smaller coefficient values.
* A techique that is often used to encourage a model to minimize the size of coefficients while it is being fit on data is called regularization.
* Common implementations include the $*L^2*$ and $*L^1*$ forms of regularization.
* Both of these forms of regularization are in fact a measure of the magnitude or length of the coefficients as a vector and are methods lifted directly from linear algebra called the vector norm.

</br>

### 6. Princple Component Analysis
* Often a dataset has many columns, perhaps tens, hundreds, thousands or more.
* Modeling data with many features is challenging, and models built from data that include irrelevant freatures are often less skillful than models trained from the most relevant data.
* It is hard to know which features of the data are relevant and which are not.
* Methods for automatically reducing the number of columns of a dataset are called dimensionality reduction, and perhaps the most used in machine learning to create projections of high-dimensionality data for both visualization and for training models.
* The core of the PCA method is a matrix factorization method from linear algebra. The eigendecomposition can be used and more robust implementations may use the singular-value decomposition or SVD.

</br>

### 7. Singular-Value Decomposition
* Another popular dimensionality reduction method is the singular-value decomposition method or SVD for short.
* As mentioned and as the name of the method suggests, it is a matrix factorization method from the field of linear algebra.
* It has wide use in linear algebra and can be used directly in applications such as feature selection, visualization, noise reduction and more.

</br>

### 8. Latent Semantic Analysis
* In the sub-field of machine learning for working with text data called natural language processing, it is common to represent documents as large matrices of word occurrences.
* For example, the columns of the matrix may be the known words in the vocabulary and rows may be setences, paragraphs, pages or documents of text with cells in the matrix mared as the count of frequency of the number of times the word occurred. This is a sparse matrix representation of the text.
* Matrix factorization methods such as the singular-value decomposition down can be applied to this sparse matirix which has the effect of distilling the representation down to its most relevant essence.
* Documents processed in thus way are much easier to compare, query and use as the basis for a supervised machine learning model.
* This form of data preparation is called Latent Semantic Analysis or LSA for short, and is also known by the name Latent Semantic Indexing or LSI. 

</br>

### 9. Recommender Systems
* Predictive modeling problems that invlove the recommendation of products are called recommender systems, a sub-field of machine learning.
* The development of recommender systems is primarily concerned with linear algebra methods.
* A simple example is in the calculation of the similarity between sparse customer behavior vectors using distance measures such as Euclidean distance or dot products.
* Matrix factorization methods like the singular-value decomposition are used widely in recommender systems to distill item and user to their essence for querying and searching and comparison.

</br>

### 10. Deep learning
* Artificial neural networks are nonlinear machine learning algorithms that are inspired by elements of the information processing in the brain and have proven effective at a range of problems not least predictive modeling.
* Deep learning is the recent resurged use of artificial neural networks with newer mthods and faster hardware that allow for the development and training of larger and deeper (more layeres) networks on very large datasets.
* At their core, the execution of neural networks involves linear algebra data structures multiplied and added together.
* Scaled up to multiple dimensions, deep learning methods work with vectors, matrices and even tensors of inputs and coefficients, where a tensor is a matrix with more than two dimensions.
* Linear algebra is central to the description of deep learning methods via matrix notation to the implementation of deep learning methods such as Google's TensorFlow Python library that has the word "tensor" in its name.