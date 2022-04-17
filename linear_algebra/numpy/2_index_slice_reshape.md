## Index, Slice and Reshape Numpy Arrays
* Machine learning data is represented as arrays. In Python, data is almost universially represented as NumPy arrays.
* If you are new to Python, you may be confused by some of the Pythonic ways of accessing data, such as negative indexing and array slicing.
* In this tutorial, you will discover how to manipulate and access your data correctly in Numpy arrays.

</br>

## 1. From List to Arrays
* In general, I recommend loading your data from file using Pandas or even NumPy functions.
* This section assumes you have loaded or generated your data by other means and it is now represented using Python lists.

</br>

## 1.1. One-Dimensional List to Array
* You may load your data or generate your data and have access to it as a list. You can convert a one-dimensional list of data to an array by calling the array() NumPy function.


</br>

## 1.2. Two-Dimensional List of Lists to Array
* It is more likely in machine learning that you will have two-dimensional data. That is a table of data where each row represents a new observation and each column a new feature.
* Perhaps you generated the data or loaded it using custom code and now you have a list of lists.
* Each list represents a new observation. You can convert your list of lists to a NumPy array the same way as above, by calling the array() function.

</br>

### [From list to arrays example](./list_to_arrays.py)

</br>

## 2. Array Indexing
* Once your data is represented using a NumPy array, you can access it using indexing.

</br>

## 2.1. One-Dimensional Indexing
* Generally, indexing works you would expect from your experience with other programming languages, like Java, C#, C++.
* For example, you can access elements using the bracket operator [] specifying the zero-offset index for the value to retrieve.
* One key difference is that you can use negative indexes to retrieve values offset from the end of the array.
* For example, the index -1 refers to the last item in the array.

</br>

## 2.2 Two-Dimensional Indexing
* Indexing two-dimensional data is simialar to indexing one-dimesional data, exept that a comma is used to seperate the index for each dimension.
* If we are interested in all items in the first row, we could leave the second dimension index empty

</br>

### [Array indexing example](./array_indexing.py)

</br>

## 3. Array Slicing
* Array slicing is one feature that causes problems for beginners to Python and NumPy arrays.
* Structures like lists and NumPy arrays can be sliced. This means that a subsequence of the structure can be indexed and NumPy arrays can be indexed and retrieved.
* __This is most useful in machine learning when specifying input variables and output variables, or splitting training row from testing rows.__
* Slicing is specified using the colon operator : with a _from_ and _to_ index before and after the column respectively.

</br>

## 3.1. One-Dimensional Slicing
* You can access all data in an array dimesion by specifying the slice ':' with no indexes.
* The first item of the array can be sliced by specifying a slice that starts at index 0 and ends at index 1.
* We can also use negative indexs in slices. For exmpale, we can slice the last two items in the list by the slice to the end of the dimension.

</br>

## 3.2. Two-Dimensional Slicing

### Split Input and Output Feature
* It is common to split yout loaded data into input varaiable($X$) and the output varaible($y$).
* We can do this by slicing all rows and all columns up to, but before the last column, then seperately indexing the last column.
* FOr the input features, we can select all row and all columns except the last one by specifying : for in the rows index, and :-1 in the columns index.

</br>

### Split Train and Test Rows
* It is common to split a loaded dataset into seperate train and test sets.
* This is a splitting of rows where some portion will be used to train the model and the remaining protion will be used to estimate the skill fo the trained model. 
* This would involve slicing all columns by specifying : in the second dimensional index.

</br>

### [Array slicing example](./array_slicing.py)

</br>

### Reference: Basics of Linear Algebra for Machine Learning - Discover the Mathematical Language of Data in Python