from numpy import array

# create 1-D array
# list of data
data_1D = [11, 22, 33, 44, 55]
# array of data
data_1D = array(data_1D)

# create 2-D array
data_2D = [[11, 22],
           [33, 44],
           [55, 66]]
# array of data
data_2D = array(data_2D)

print(data_1D)
print(type(data_1D))

print(data_2D)
print(type(data_2D))