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
# print(repr(reshaped_arr.shape))

arr2 = np.arange(10)
reshaped_arr2 = np.reshape(arr2, (-1, 2, 5))
# print(repr(reshaped_arr2.shape))

#Flatten array
arr3 = np.arange(12)
reshaped_arr3 = np.reshape(arr3, (2, 6))
flatten_arr = arr3.flatten()
print(repr(arr3))
print("Array shape: {}".format(reshaped_arr3.shape))
print("Flatten array: {}".format(flatten_arr))
print("Array after flatten: {}".format(flatten_arr.shape))