import numpy as np

#Array Accessing
# arr = np.array([1, 2, 3, 4, 5])
# print(arr[0])
# print(arr[4])

# arr = np.array([[6, 3], [0, 2]])
# # Subarray
# print(repr(arr[0]))

#array slicing
# arr = np.array([1, 2, 3, 4, 5])
# print(repr(arr[:]))
# print(repr(arr[1:]))
# print(repr(arr[2:4]))
# print(repr(arr[:-1]))
# print(repr(arr[-2:]))

#Slicing a 2-D numpy array
arr = np.array([[1, 2, 3],
                [4, 5, 6],
                [7, 8, 9]])
print(repr(arr[:]))
print(repr(arr[1:]))
print(repr(arr[:, -1]))
print(repr(arr[:, 1:]))
print(repr(arr[0:1, 1:]))
print(repr(arr[0, 1:]))