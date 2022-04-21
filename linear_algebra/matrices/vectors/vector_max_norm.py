from math import inf
from numpy import array
from numpy.linalg import norm

arr = array([1,2,3])
maxnorm = norm(arr, inf)

print(f"arr: {arr}")
print(f"arr max norm: {maxnorm}")