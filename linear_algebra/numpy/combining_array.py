from numpy import array
from numpy import vstack
from numpy import hstack

# create array
arr1 = array([1,2,3])
print(arr1)
arr2 = array([4,5,6])
print(arr2)

# vertical stack
arr3 = vstack((arr1, arr2))
print(f"arr3 = {arr3}")
print(f"arr4 shape = {arr3.shape}")

arr4 = hstack((arr1, arr2))
print(f"arr4 = {arr4}")
print(f"arr4 shape = {arr4.shape}")