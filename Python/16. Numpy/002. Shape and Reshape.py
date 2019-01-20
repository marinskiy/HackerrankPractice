# Problem: https://www.hackerrank.com/challenges/np-shape-reshape/problem
# Score: 20


import numpy as np


array = np.array(list(map(int, input().split())))
print(array.reshape(3, 3))
