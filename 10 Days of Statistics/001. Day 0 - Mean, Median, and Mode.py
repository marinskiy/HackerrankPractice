# Problem: https://www.hackerrank.com/challenges/s10-basic-statistics/problem
# Score: 30


import numpy as np
from scipy import stats


n = int(input())
arr = list(map(int, input().split()))
print(np.mean(arr))
print(np.median(arr))
print(stats.mode(arr)[0][0])
