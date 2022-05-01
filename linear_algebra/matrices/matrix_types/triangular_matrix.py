from numpy import array
from numpy import tril
from numpy import triu

M = array([
    [1, 2, 3],
    [1, 2, 3],
    [1, 2, 3]
])

print(f"M:\n {M}")
print(f"tril(M):\n {tril(M)}")
print(f"triu(M):\n {triu(M)}")