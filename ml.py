import numpy as np


# arr1 = np.array([-2, 4, 5])
# print(arr1)

#Create 2D matrix
# arr = np.array([[1, 2, 4], [3, 4, 5]], dtype=np.float32)
# print(repr(arr))

# arr = np.array([1, 2.3, 5])
# print(repr(arr))

#Copy method
# a = np.array([4, 2])
# b = np.array([3, 6])
# c = a
# print("Array a: {}".format(repr(a)))
# c[0] = 8
# print("Array a after modifying c: {}".format(repr(a)))

# d = b.copy()
# d[0] = 9
# print("Array b after modifying d: {}".format(repr(b)))

#Casting method
# arr = np.array([4, 2])
# print(arr.dtype)

# arr = arr.astype(np.float32)
# print(arr.dtype)

#NAN method
# arr = np.array([np.nan, 1, 3])
# print(repr(arr))

# arr = np.array([np.nan, 'bba'])
# print(repr(arr))

# np.array([np.nan, 1, 2], dtype=np.float32)
# np.array([np.nan, 3, 2], dtype=np.int32) #uncommenting this line will break the code

#Infinity method
# print(np.inf > 100000)

# arr = np.array([np.inf, 5])
# print(repr(arr))

# arr = np.array([-np.inf, 2])
# print(repr(arr))

# np.array([np.inf, 3], dtype=np.float32)
# np.array([np.inf, 2], dtype=np.int32) #uncommenting this line will break the code

#Quiz
#1. The first array we'll create comes straight from a list of integers and np.nan. The list contains np.nan as the first element, and the integers from 2 to 5, inclusive, as the next four elements. Set arr equal to np.array applied to the specified list.
# arr = np.array([np.nan, 2, 3, 4, 5])
# print(repr(arr))

#2. We now want to copy the array so we can change the first element to 10. This way we don't modify the original array. Set arr2 equal to arr.copy(), then set the first element of arr2 equal to 10.
# arr = np.array([np.nan, 2, 3, 4, 5])
# arr2 = arr.copy()
# arr2[0] = 10
# print(repr(arr2))

#3. The next two arrays will use floating point numbers. The first array will be upcast to floating point numbers, while we manually cast the second array using np.float32.
# For manual casting, we use an array's inherent astype function, which takes in the new type as an argument and returns the casted array.
# Set float_arr equal to np.array applied to a list with elements 1, 5.4, and 3, in that order.
# Set float_arr2 equal to arr2.astype, with argument np.float32.
# arr = np.array([[1, 2, 3], [4, 5, 6]])
# float_arr2 = arr.astype(np.float32)
# print(repr(float_arr2))