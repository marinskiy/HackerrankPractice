# Problem: https://www.hackerrank.com/challenges/s10-binomial-distribution-1/problem
# Score: 30


import math


p = 1.09/(1+1.09)
ans = 0
for i in range(3):
    ans += math.factorial(6) / math.factorial(i) / math.factorial(6-i) * p**i * (1-p)**(6-i)
print(round(1-ans, 3))
