from numpy import array

data_1D = array([11, 22, 33, 44, 55])
data_2D = array([ [11,22,33],
                  [44,55,66],
                  [77,88,99]])
# seperate 2D data
X, y = data_2D[:, :-1], data_2D[:, -1]
# split train and test data
split = 2
train, test = data_2D[:split, :], data_2D[split:, :]

print(f"data_1D[:] = {data_1D[:]}")
print(f"data_1D[0:1] = {data_1D[0:1]}")
print(f"data_1D[-2:] = {data_1D[-2:]}\n")

print(f"data_2D[:] = {data_2D[:]}")
print(f"X = {X}")
print(f"y =  {y}")
print(f"train =  {train}")
print(f"test = {test} ")