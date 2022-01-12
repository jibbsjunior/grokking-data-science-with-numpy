import numpy as np
from numpy.core.arrayprint import array_repr
from numpy.core.fromnumeric import reshape

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
# arr = np.arange(8)
# reshaped_arr = np.reshape(arr, (2, 4))
# # print(repr(reshaped_arr.shape))

# arr2 = np.arange(10)
# reshaped_arr2 = np.reshape(arr2, (-1, 2, 5))
# # print(repr(reshaped_arr2.shape))

# #Flatten array
# arr3 = np.arange(12)
# reshaped_arr3 = np.reshape(arr3, (2, 6))
# flatten_arr = arr3.flatten()
# print(repr(arr3))
# print("Array shape: {}".format(reshaped_arr3.shape))
# print("Flatten array: {}".format(flatten_arr))
# print("Array after flatten: {}".format(flatten_arr.shape))

#Transpose an array
# arr = np.arange(8)
# arr = np.reshape(arr, (2, 4))
# transposed = np.transpose(arr)
# print(repr(transposed.shape))

#Transpose with the axes argument type
# arr = np.arange(24)
# arr = np.reshape(arr, (3, 4, 2))
# transposed = np.transpose(arr, axes=(2, 1, 0))
# print(repr(transposed))

#np.zeros and np.ones function
# arr = np.zeros(8)
# arr1 = np.ones((8, 2))
# arr2 = np.ones((4, 2), dtype=np.int32)
# print(repr(arr))
# print(repr(arr1))
# print(repr(arr2))

#np.zeros_like and np.ones_like function
# arr = np.array([[1, 2], [3, 4]])
# print(repr(np.zeros_like(arr)))

# arr1 = np.array([[5, 6], [8, 9]])
# print(repr(np.ones_like(arr1, dtype=np.float32)))

# Quiz
#1. Our initial array will just be all the integers from 0 to 11, inclusive. We'll also reshape it so it has three dimensions.
arr = np.arange(12)
reshaped = np.reshape(arr, (2, 3, 2))
print(repr(reshaped))

#2. Next we want to get a flattened version of the reshaped array (the flattened version is equivalent to arr), as well as a transposed version. For the transposed version of reshaped, we use a permutation of (1, 2, 0).
flattened = reshaped.flatten()
transposed = np.transpose(reshaped, axes=(1,2,0))
print(repr(transposed))

# 3. We'll create an array of 5 elements, all of which are 0. We'll also create an array with the same shape as transposed, but containing only 1 as the elements.
zeros_arr = np.zeros(5)
ones_arr = np.ones_like(transposed)
print(repr(ones_arr))

# 4. The final array will contain 101 evenly spaced numbers between -3.5 and 1.5, inclusive. Since they are evenly spaced, the difference between adjacent numbers is 0.05.
points = np.linspace(-3.5, 1.5, num=101)
print(repr(points))