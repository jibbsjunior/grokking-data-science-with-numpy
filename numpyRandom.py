import numpy as np
from numpy.core.fromnumeric import size

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
# vec = np.array([1, 2, 3, 4, 5])
# np.random.shuffle(vec)
# print(vec)
# matrix = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
# np.random.shuffle(matrix)
# print(matrix)

#Distributions
# print(np.random.uniform())
# print(np.random.uniform(low=1.5, high=2.2))
# print(repr(np.random.uniform(size=3)))
# print(repr(np.random.uniform(low=1.2, high=2.1, size=(2,2))))
# print(np.random.normal())
# print(np.random.normal(loc=1.5, scale=2.2))
# print(repr(np.random.normal(loc=1.4, scale=2.4, size=(2,2))))
colors = ['Red', 'Blue', 'Green']
print(np.random.choice(colors))
print(repr(np.random.choice(colors, size=2)))
print(repr(np.random.choice(colors, size=(2,2))))
print(repr(np.random.choice(colors, size=(2, 2), p=[0.8, 0.19, 0.01])))