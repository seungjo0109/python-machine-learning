from numpy import array
from numpy.linalg import norm

arr = array([1,2,3])
l2 = norm(arr)

print(f"arr: {arr}")
print(f"arr L2 norm: {l2}")