from numpy import array
from numpy.linalg import inv

Q = array([
    [1, 0],
    [0, -1]
])

V = inv(Q)

print(f"Q: \n{Q}")
print(f"V: \n{V}")
print(f"Q.T: \n{Q.T}")
print(f"Q.dot(Q.T): \n{Q.dot(Q.T)}")
