#Summation
import numpy as np
from numpy.core.fromnumeric import cumsum

arr = np.array([[2, 3, 5], [1, 4, 3], [4, 7, 5]])

# print(np.sum(arr))
# print(repr(np.sum(arr, axis=0)))
# print(repr(np.sum(arr, axis=1)))

# cumsum
x = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

# print(np.cumsum(x))
# print(np.cumsum(x, axis=0))
# print(np.cumsum(x, axis=1))

#concatenation
print(np.concatenate([arr, x]))
print(np.concatenate([arr, x], axis=1))