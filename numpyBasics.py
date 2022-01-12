import numpy as np
from numpy.core.arrayprint import array_repr

# arange function
# arr = np.arange(5)
# print(repr(arr))

#linspace function
# arr = np.linspace(5, 11, num=5)
# print(repr(arr))
# arr = np.linspace(5, 11, num=4, endpoint=False)
# print(repr(arr))
# arr = np.linspace(5, 12, num=6, dtype=np.float32)
# print(repr(arr))

#reshape function
arr = np.arange(8)
reshaped_arr = np.reshape(arr, (2, 4))
print(repr(reshaped_arr.shape))