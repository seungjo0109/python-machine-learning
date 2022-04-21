from numpy import array
from numpy.linalg import norm

# define vector
arr = array([1, 2, 3])
l1 = norm(arr, 1)

print(f"arr: {arr}")
print(f"arr L1 norm: {l1}")