import numpy as np

x = np.array([[1, 3, -2], 
              [-3, 5, 22], 
              [2, 4 -5]], dtype=object)
# print(repr(x.min(axis=0)))
# print(repr(x.max(axis=-1)))

#mean, median, variance
arr = np.array([[1, 3, 5], [4, 2, 1], [3, 2, 4]])

# print(np.mean(arr))
# print(np.var(arr))
# print(np.median(arr))
# print(repr(np.median(arr, axis=-1)))

#Quiz
# 1. Each coding exercise in this chapter will be to complete a small function that takes in a 2-D NumPy matrix (data) as input. The first function to complete is get_min_max, which returns the overall minimum and maximum element in data.
def get_min_max(data):
  # CODE HERE
  overall_min = data.min()
  overall_max = data.max()

  return overall_min, overall_max
  pass

# 2. Next, we'll complete col_min, which returns the minimums across each column of data.
def col_min(data):
  # CODE HERE
  min0 = data.min(axis=0)

  return min0
  pass

# 3. The final function to complete is basic_stats, which returns the mean, median, and variance of data.
def basic_stats(data):
  # CODE HERE
  mean = np.mean(data)
  median = np.median(data)
  var = np.var(data)

  return mean, median, var
  pass