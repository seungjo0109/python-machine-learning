from numpy import array
from numpy import diag

M = array([
    [1, 2, 3],
    [1, 2, 3],
    [1, 2, 3]
])

print(f"M:\n {M}")
print(f"diag(M):\n {diag(M)}")
print(f"diag(diag(M)): \n {diag(diag(M))}")