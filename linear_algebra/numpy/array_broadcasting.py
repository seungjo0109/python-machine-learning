from numpy import array

arr_1D = array([1, 2, 3])
arr_2D = array([[1, 2, 3],
                [1, 2, 3]])
arr2_1D = array([1, 2])

scalar = 2

print(f"arr_1D: {arr_1D}")
print(f"arr_2D: \n{arr_2D}")
print(f"scalar: {scalar}")
print(f"arr_1D + scalar: {arr_1D+scalar}")
print(f"arr_2D + scalar: \n{arr_2D+scalar}")
print(f"arr_1D + add_2D: \n{arr_1D+arr_2D}")
# print(f"broadcasting error case: {arr2_1D+arr_2D}")
