# Problem: https://www.hackerrank.com/challenges/s10-the-central-limit-theorem-1/problem
# Score: 30


import math


def cdf(x, mean, std):
    return 1/2*(1+math.erf((x-mean) / std / 2**(1/2)))


mean = 49 * 205
std = 15 * 49**(1/2)

# Find the probability that sum <= 9800
print(round(cdf(9800, mean, std), 4))
