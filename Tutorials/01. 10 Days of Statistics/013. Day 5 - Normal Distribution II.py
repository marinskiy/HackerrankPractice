# Problem: https://www.hackerrank.com/challenges/s10-normal-distribution-2/problem
# Score: 30


import math


def cdf(x, mean, std):
    return 1/2*(1+math.erf((x-mean) / std / 2**(1/2)))


mean = 70
std = 10

# Scored higher than 80
print(round((1 - cdf(80, mean, std))*100, 2))
# Passed the test (i.e., have a grade >= 60)?
print(round((1 - cdf(60, mean, std))*100, 2))
# Failed the test (i.e., have a grade < 60)?
print(round(cdf(60, mean, std)*100, 2))
