from numpy import array

data_1D = array([11, 22, 33, 44, 55])
data_2D = array([ [11, 22],
                  [33, 44],
                  [55, 66]])

data_reshape = data_1D.reshape((data_1D.shape[0], 1))
data_reshape_3D = data_2D.reshape((data_2D.shape[0], data_2D.shape[1], 1))

print(f"dat_1D shape: {data_1D.shape}")
print(f"dat_2D shape: {data_2D.shape}")
print(f"data_2D Rows: {data_2D.shape[0]}")
print(f"data_2D Cols: {data_2D.shape[1]}")
print(f"data_reshape shape: {data_reshape.shape}")
print(f"data_reshape_3D shape: {data_reshape_3D.shape}")