from numpy import array

A = array([
    [1,2],
    [3,4],
    [5,6]
])
v = array([0.5, 0.5])

print(f"matrix A: {A}")
print(f"vector v: {v}")
print(f"A.dot(v): {A.dot(v)}")