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
# print(np.concatenate([arr, x]))
# print(np.concatenate([arr, x], axis=1))

#Quiz
# 1. The first function to complete is get_sums, which returns the overall sum and column sums of data.
def get_sums(data):
  # CODE HERE
  total_sum = np.sum(data)
  col_sum = np.sum(data, axis=0)

  return total_sum, col_sum
  pass

# 2. The next function to complete is get_cumsum, which returns the cumulative sums for each row of data.
def get_cumsum(data):
  # CODE HERE
  row_cumsum = np.cumsum(data, axis=1)

  return row_cumsum
  pass

# 3. The final function, concat_arrays, takes in two 2-D NumPy arrays as input. It returns the column-wise and row-wise concatenations of the input arrays.
def concat_arrays(data1, data2):
  # CODE HERE
  col_concat = np.concatenate([data1, data2])
  row_concat = np.concatenate([data1, data2], axis=1)

  return col_concat, row_concat
  pass

