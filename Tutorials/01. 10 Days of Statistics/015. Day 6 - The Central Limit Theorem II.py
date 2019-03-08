# Problem: https://www.hackerrank.com/challenges/s10-the-central-limit-theorem-2/problem
# Score: 30


import math


def cdf(x, mean, std):
    return 1/2*(1+math.erf((x-mean) / std / 2**(1/2)))


mean = 100 * 2.4
std = 2 * 100**(1/2)

# Find the probability that sum <= 250
print(round(cdf(250, mean, std), 4))
