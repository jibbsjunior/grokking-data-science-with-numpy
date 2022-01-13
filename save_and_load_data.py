import numpy as np

#Save data
arr = np.array([[1, 3, 4], [1, 4, 5], [5, 9, 0]])
np.save('arr', arr)

#Load data
load_file = np.load('arr.npy')
print(repr(load_file))