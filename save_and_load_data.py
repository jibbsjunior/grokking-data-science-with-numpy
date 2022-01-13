import numpy as np

#Save data
arr = np.array([[1, 3, 4], [1, 4, 5], [5, 9, 0]])
np.save('arr', arr)

#Load data
load_file = np.load('arr.npy')
print(repr(load_file))

# #Quiz
# 1. The coding exercise in this chapter will require you to complete the save_points function, which will save some randomly generated 2-D points in a file.
# You'll generate 100 (x, y) points from a uniform distribution in the range [-2.5, 2.5), then save the points to save_file.
def save_points(save_file):
  # CODE HERE
  points = np.random.uniform(low=-2.5, high=2.5, size=(100, 2))
  np.save(save_file, points)
  pass