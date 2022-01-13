import numpy as np

x = np.array([[1, 3, -2], 
              [-3, 5, 22], 
              [2, 4 -5]], dtype=object)
# print(repr(x.min(axis=0)))
# print(repr(x.max(axis=-1)))

#mean, median, variance
arr = np.array([[1, 3, 5], [4, 2, 1], [3, 2, 4]])

print(np.mean(arr))
print(np.var(arr))
print(np.median(arr))
print(repr(np.median(arr, axis=-1)))
