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
# colors = ['Red', 'Blue', 'Green']
# print(np.random.choice(colors))
# print(repr(np.random.choice(colors, size=2)))
# print(repr(np.random.choice(colors, size=(2,2))))
# print(repr(np.random.choice(colors, size=(2, 2), p=[0.8, 0.19, 0.01])))

#Quiz
# 1. Set random1 equal to np.random.randint with 5 as the only argument.
# Then set random_arr equal to np.random.randint with 3 as the first argument, 10 as the high keyword argument, and (3, 5) as the size keyword argument.
random1 = np.random.randint(5)
random_arr = np.random.randint(3, high=10, size=(3, 5))

# 2. The next two arrays will be drawn randomly from distributions. The first will contain 5 numbers drawn uniformly from the range [-2.5, 1.5].
# Set random_uniform equal to np.random.uniform with the low and high keyword arguments set to -2.5 and 1.5, respectively. The size keyword argument should be set to 5.
random_uniform = np.random.uniform(low=-2.5, high=1.5, size=5)

# 3. The second array will contain 50 numbers drawn from a normal distribution with mean 2.0 and standard deviation 3.5.
# Set random_norm equal to np.random.normal with the loc and scale keyword arguments set to 2.0 and 3.5, respectively. The size keyword argument should be set to (10, 5).
random_norm = np.random.normal(loc=2.0, scale=3.5, size=(10, 5))

# 4. We'll now create our own distribution of strings and randomly select from it. The values for our distribution will be 'a', 'b', 'c', 'd'.
# To choose a value, we'll use a probability distribution of [0.5, 0.1, 0.2, 0.2], i.e. 'a' will have probability 0.5 of being chosen, 'b' will have a probability of 0.1, etc.
choices = ['a', 'b', 'c', 'd']
choice = np.random.choice(choices, p=[0.5, 0.1, 0.2, 0.2])

# 5. The last random operation we perform will be an in-place shuffle of a NumPy array.
# Set arr equal to a NumPy array containing the integers from 1 to 5, inclusive.
arr = np.array([1, 2, 3, 4, 5])
np.random.shuffle(arr)