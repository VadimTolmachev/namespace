import numpy as np
from random import randint

list1_int = []
list2_int = []
for i in range(10):
    list1_int.append(randint(1,10))
    list2_int.append(randint(1, 10))

arr = np.array([list1_int, list2_int])

print(arr)
print(arr.ndim)
print(arr.shape)
print('---')
for i in arr:
    print('***')
    for y in i:
        print(y)