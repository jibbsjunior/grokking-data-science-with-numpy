import numpy as np
from numpy.ma.core import exp

arr = np.array([[1, 2], [3, 4]])
#add 1 to each element values
# print(repr(arr + 1))
# #subtract 1 from each element values
# arr -= 1
# print(repr(arr))
# #multiply each element values by 2
# arr *= 2
# print(repr(arr))
# #divide each element by 2
# print(repr(arr/2))
# #perform integer division (half) on each element
# print(repr(arr // 2))
# #square each element values
# print(repr(arr ** 2))
# #square root each element values
# print(repr(arr ** 0.5))

#convert fahrenheit to celsius with numpy
def fahrenheit_to_celsius(temp):
    return (5/9) * (temp - 32)

fahrenheits = np.array([0, 32, 12, -3, 15, 30])
celsius = fahrenheit_to_celsius(fahrenheits)
# print("celsius: {}".format(repr(celsius)))

#non-linear functions
# x = np.array([[1, 2], [3, 4]])
# #raised each x element to the power of e
# print(repr(np.exp(x)))
# #raised each x element to the power of 2
# print(repr(np.exp2(x)))

# y = np.array([[2, 3], [np.e, np.pi]])
# #Natural logarithm of y
# print(repr(np.log(y)))
# print(repr(np.power(2, x)))

#matrix multiplication
# x = np.array([[1, 2], [3, 4], [5, 6]])
# y = np.array([[2, 4, 5], [7, 8, 9]])
# z = np.array([1, 2, 3])
# m = np.array([3, 4, 5])
# print(repr(np.matmul(z, m)))
# print(repr(np.matmul(x, y)))
# print(repr(np.matmul(x, x)))

#Quiz
# 1. Set arr equal to np.array applied to a list of lists representing the first matrix.
# Then set arr2 equal to np.array applied to a list of lists representing the second matrix.
arr = np.array([[-0.5, 0.8, -0.1], [0.0, -1.2, 1.3]])
arr2 = np.array([[1.2, 3.1], [1.2, 0.3], [1.5, 2.2]])

# 2. Next we'll apply some arithmetic to arr. Specifically, we'll do multiplication, addition, and squaring.
# Set multiplied equal to arr multiplied by np.pi.
# Then set added equal to the result of adding arr and multiplied.
# Finally, set squared equal to added with each of its elements squared.
multiplied = arr * np.pi
added = arr + multiplied
squared = added ** 2
# print(repr(multiplied))
# print(repr(added))
# print(repr(squared))

# 3. Set exponential equal to np.exp applied to squared.
# Then set logged equal to np.log applied to arr2.
exponential = np.exp(squared)
logged = np.log(arr2)
# print(repr(exponential.shape))
# print(repr(logged.shape))
# 4. Note that exponential has shape (2, 3) and logged has shape (3, 2). So we can perform matrix multiplication both ways.
# Set matmul1 equal to np.matmul with first argument logged and second argument exponential. Note that matmul1 will have shape (3, 3).
# Then set matmul2 equal to np.matmul with first argument exponential and second argument logged. Note that matmul2 will have shape (2, 2).
matmul1 = np.matmul(logged, exponential)
matmul2 = np.matmul(exponential, logged)
print(repr(matmul1.shape))
print(repr(matmul2.shape))