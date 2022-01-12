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
# arr = np.array([[1, 2, 3],
#                 [4, 5, 6],
#                 [7, 8, 9]])
# print(repr(arr[:]))
# print(repr(arr[1:]))
# print(repr(arr[:, -1]))
# print(repr(arr[:, 1:]))
# print(repr(arr[0:1, 1:]))
# print(repr(arr[0, 1:]))

#Argmin and Argmax function
# arr = np.array([[-2, -1, -3],
#                 [4, 5, -6],
#                 [-3, 9, 1]])
# print(np.argmin(arr[0]))
# print(np.argmax(arr[2]))
# print(np.argmin(arr))

#Quiz
# 1. Each coding exercise in this chapter will be to complete a small function that takes in a 2-D NumPy matrix (data) as input. The first function to complete is direct_index.
# Set elem equal to the third element of the second row in data (remember that the first row is index 0). Then return elem.
def direct_index(data):
  # CODE HERE
  elem = data[1][2]
  return elem
  pass

# 2. The next function, slice_data, will return two slices from the input data.
# The first slice will contain all the rows, but will skip the first element in each row. The second slice will contain all the elements of the first three rows except the last two elements.
def slice_data(data):
  # CODE HERE
  slice1 = data[:, 1:]
  slice2 = data[0:3, :-2]
  return (slice1, slice2)
  pass

# 3. The final function, argmax_data, will find the index of each row's maximum element in data. Since there are only 2 dimensions in data, we can apply the operation along either axis 1 or -1.
def argmax_data(data):
  # CODE HERE
  argmax_neg1 = np.argmax(data, axis=1)
  return argmax_neg1
  pass
