from numpy import array

A = array([
    [1,2],
    [3,4],
    [5,6]
])

B = array([
    [1,2],
    [3,4]
])

C = A.dot(B)
D = A @ B

print(f"matrix A: {A}")
print(f"matrix A: {B}")
print(f"matrix A.dot(B): {C}")
print(f"matrix A @ B: {D}")