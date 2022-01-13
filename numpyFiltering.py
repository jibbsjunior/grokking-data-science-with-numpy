import numpy as np

#Filtering data
# x = np.array([[1, 2, 3], [4, 5, 6], [3, 1, 0]])
# # print(repr(x == 3))
# # print(repr(x > 0))
# # print(repr(x != 1))
# # print(repr(~(x != 1)))
# y = np.array([[1, 2, 4], [4, 2, np.nan], [3, np.nan, 1]])
# print(repr(np.isnan(y)))
# x = np.array([[1, 3, 2], [2, 1, 4], [2, 3, 4]])
# # print(repr(np.where(x == 3)))
# # print(repr(np.where([True, False, True])))
# np_filter = np.array([[True, False], [False, True]])
# positives = np.array([[1, 2], [3, 4]])
# negatives = np.array([[-2, -5], [-1, -8]])
# # print(repr(np.where(np_filter, positives, negatives)))
# np_filter = positives > 2
# # print(repr(np.where(np_filter, positives, negatives)))

# np_filter = negatives > 0
# # print(repr(np.where(np_filter, positives, negatives)))

# np_filter = np.array([[True, False], [False, True]])
# positives = np.array([[1, 2], [3, 4]])
# # print(repr(np.where(np_filter, positives, -1)))
# arr = np.array([[-2, -1, -3],
#                 [4, 5, -6],
#                 [3, 9, 1]])
# print(repr(arr > 0))
# print(np.any(arr > 0))
# print(np.all(arr > 0))

#Quiz
# 1. Each coding exercise in this chapter will be to complete a small function that takes in a 2-D NumPy matrix (data) as input. The first function to complete is get_positives.
# Set a tuple of x_ind, y_ind equal to the output of np.where, applied with the condition data > 0.
# Then return data[x_ind, y_ind].
def get_positives(data):
  # CODE HERE
  x_ind, y_ind = np.where(data > 0)
  print(repr(data[x_ind, y_ind]))
  return data[x_ind, y_ind]
  pass

#   2. Next, we'll complete the function replace_zeros. The function replaces each of the non-positive elements in data with 0. We first create an array of all 0's, with the same shape as data.
# Then we filter the data array and replace the non-positive elements with the corresponding element from zeros (which will be a 0).
def replace_zeros(data):
  # CODE HERE
  zeros = np.zeros_like(data)
  zero_replace = np.where(data > 0, data, zeros)
  return zero_replace
  pass

# 3. The next function, replace_neg_one, will replace the non-positive elements of data with -1. Rather than creating a separate array, we'll use broadcasting.
def replace_neg_one(data):
  # CODE HERE
  neg_one_replace = np.where(data > 0, data, -1)
  return neg_one_replace
  pass

#4. Our final function, coin_flip_filter will apply a filter using a boolean array as the condition. We'll first create a boolean coin flip array with the same shape as data.
def coin_flip_filter(data):
  # CODE HERE
  coin_flips = np.random.randint(2, size=(data.shape))
  bool_coin_flips = coin_flips.astype(np.bool)
  one_replace = np.where(bool_coin_flips, data, 1)
  return one_replace
  pass