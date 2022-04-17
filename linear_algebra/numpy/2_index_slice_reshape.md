## Index, Slice and Reshape Numpy Arrays
* Machine learning data is represented as arrays. In Python, data is almost universially represented as NumPy arrays.
* If you are new to Python, you may be confused by some of the Pythonic ways of accessing data, such as negative indexing and array slicing.
* In this tutorial, you will discover how to manipulate and access your data correctly in Numpy arrays.

</br>

### 1. From List to Arrays
* In general, I recommend loading your data from file using Pandas or even NumPy functions.
* This section assumes you have loaded or generated your data by other means and it is now represented using Python lists.

</br>

### 1.1. One-Dimensional List to Array
* You may load your data or generate your data and have access to it as a list. You can convert a one-dimensional list of data to an array by calling the array() NumPy function.


</br>

### 1.2. Two-Dimensional List of Lists to Array
* It is more likely in machine learning that you will have two-dimensional data. That is a table of data where each row represents a new observation and each column a new feature.
* Perhaps you generated the data or loaded it using custom code and now you have a list of lists.
* Each list represents a new observation. You can convert your list of lists to a NumPy array the same way as above, by calling the array() function.

</br>

### [From list to arrays example](./list_to_arrays.py)

</br>

### 2. Array Indexing
* Once your data is represented using a NumPy array, you can access it using indexing.

</br>

### 2.1. One-Dimensional Indexing
* Generally, indexing works you would expect from your experience with other programming languages, like Java, C#, C++.
* For example, you can access elements using the bracket operator [] specifying the zero-offset index for the value to retrieve.
* One key difference is that you can use negative indexes to retrieve values offset from the end of the array.
* For example, the index -1 refers to the last item in the array.

</br>

### 2.2 Two-Dimensional Indexing
* Indexing two-dimensional data is simialar to indexing one-dimesional data, exept that a comma is used to seperate the index for each dimension.
* If we are interested in all items in the first row, we could leave the second dimension index empty

</br>

### [Array indexing example](./array_indexing.py)

</br>

### 3. Array Slicing
* Array slicing is one feature that causes problems for beginners to Python and NumPy arrays.
* Structures like lists and NumPy arrays can be sliced. This means that a subsequence of the structure can be indexed and NumPy arrays can be indexed and retrieved.
* __This is most useful in machine learning when specifying input variables and output variables, or splitting training row from testing rows.__
* Slicing is specified using the colon operator : with a _from_ and _to_ index before and after the column respectively.

</br>

### 3.1. One-Dimensional Slicing
* You can access all data in an array dimesion by specifying the slice ':' with no indexes.
* The first item of the array can be sliced by specifying a slice that starts at index 0 and ends at index 1.
* We can also use negative indexs in slices. For exmpale, we can slice the last two items in the list by the slice to the end of the dimension.

</br>

### 3.2. Two-Dimensional Slicing

#### Split Input and Output Feature
* It is common to split yout loaded data into input varaiable($X$) and the output varaible($y$).
* We can do this by slicing all rows and all columns up to, but before the last column, then seperately indexing the last column.
* FOr the input features, we can select all row and all columns except the last one by specifying : for in the rows index, and :-1 in the columns index.

</br>

#### Split Train and Test Rows
* It is common to split a loaded dataset into seperate train and test sets.
* This is a splitting of rows where some portion will be used to train the model and the remaining protion will be used to estimate the skill fo the trained model. 
* This would involve slicing all columns by specifying : in the second dimensional index.

</br>

### [Array slicing example](./array_slicing.py)

</br>


### 4. Array Reshaping
* After slicing your data, you may need to reshape it. For examples, some libraries, such as scikit-learn, may require that a one-dimensional array of output variables (_y_) be shaped as a two-dimensional array with one column and outcomes for each column.
* Some algotrithms, like the Long Short-Term Memory recurrent neural network in Keras, require input to be specified as a three-dimensional array comprised of samples, timesteps, and features.
* It is important to know how to reshape your NumPy arrays so that your data meets the expectation of specific Python libraries.

</br>

### 4.1. Data Shape
* NumPy arrays have a shape attribute that returns a tuple of the length of each dimesnions of the array.
* You can user the size of your array dimensions in the shape dimension, such as specifying parameters.
* The elements of the tuple can be accessed just like an array, with the 0th index for the number of rows and the 1st index for the number of columns.

</br>

### 4.2. Reshape 1D to 2D Array
* It is common to need to reshape a one-dimensional  array into a two-dimensional array with one column and multiple arrays.
* NumPy provides reshape() function on the NumPy array object that can be used to reshape the data.
* The reshape() function takes a single argument that speicifies the new shape of the array. 

</br>

### 4.3. Reshape 2D to 3D Array
* It is common to need to reshape two-dimensional data where each row represents a sequence into a three-dimensional array for algorithms that expect multiple samples of one or more time steps and one or more freatures.
* A good example is the LSTM recurrent neural network model in the Keras deep learning library.
* The reshape function can be used directly, specifying the new dimensionality.
* This is clear with an example where each sequence has multiple time steps with one observation (feature) at each time step.
* We can use the sizes in the shape attribution on the array to specify the number of samples (rows) and columns (time steps) and fix the number of features at 1.

### Reference: Basics of Linear Algebra for Machine Learning - Discover the Mathematical Language of Data in Python