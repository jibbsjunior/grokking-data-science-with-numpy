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
print(np.inf > 100000)

arr = np.array([np.inf, 5])
print(repr(arr))

arr = np.array([-np.inf, 2])
print(repr(arr))

np.array([np.inf, 3], dtype=np.float32)
# np.array([np.inf, 2], dtype=np.int32) #uncommenting this line will break the code