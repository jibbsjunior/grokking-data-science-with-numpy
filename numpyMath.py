import numpy as np

arr = np.array([[1, 2], [3, 4]])
#add 1 to each element values
print(repr(arr + 1))
#subtract 1 from each element values
arr -= 1
print(repr(arr))
#multiply each element values by 2
arr *= 2
print(repr(arr))
#divide each element by 2
print(repr(arr/2))
#perform integer division (half) on each element
print(repr(arr // 2))
#square each element values
print(repr(arr ** 2))
#square root each element values
print(repr(arr ** 0.5))