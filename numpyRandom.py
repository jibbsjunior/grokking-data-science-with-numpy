import numpy as np

# print(np.random.randint(5))
# print(np.random.randint(5, high=6))
# print(np.random.randint(5, high=7, size=(2, 2)))

#Utility function
# np.random.seed(1)
# print(np.random.randint(10))
# random_arr = np.random.randint(4, high=100, size=(2, 2))
# print(random_arr)

# #new seed
# np.random.seed(4)
# print(np.random.randint(23))
# random_arr = np.random.randint(3, high=100, size=(2, 2))
# print(random_arr)

#np.random.shuffle function
vec = np.array([1, 2, 3, 4, 5])
np.random.shuffle(vec)
print(vec)
matrix = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
np.random.shuffle(matrix)
print(matrix)