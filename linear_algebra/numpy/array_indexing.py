from numpy import array

# define array
data = array([11, 22, 33, 44, 55])
data_2D = array([[11, 22],
                 [33, 44],
                 [55, 66]])

print(f"data : {data}")
print(f"data[0]: {data[0]}")
print(f"data[4]: {data[4]}")
print(f"data[-1]: {data[-1]}")
print(f"data[-5]: {data[-5]}\n")

print(f"data_2D: {data_2D}")
print(f"data_2D[0,0]: {data_2D[0,0]}")
print(f"data_2D[0,]: {data_2D[0,]}")

