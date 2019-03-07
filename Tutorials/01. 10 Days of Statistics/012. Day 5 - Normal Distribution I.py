# Problem: https://www.hackerrank.com/challenges/s10-normal-distribution-1/problem
# Score: 30


import math


def cdf(x, mean, std):
    return 1/2*(1+math.erf((x-mean) / std / 2**(1/2)))


mean = 20
std = 2

# Less than 19.5 hours
print(round(cdf(19.5, mean, std), 3))
# Between 20 and 22 hours?
print(round(cdf(22, mean, std) - cdf(20, mean, std), 3))
