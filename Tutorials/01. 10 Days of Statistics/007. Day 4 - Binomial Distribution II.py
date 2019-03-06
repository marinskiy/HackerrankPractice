# Problem: https://www.hackerrank.com/challenges/s10-binomial-distribution-2/problem
# Score: 30


import math


p = 0.12
ans1 = 0
for i in range(0, 3):
    ans1 += math.factorial(10)/math.factorial(i)/math.factorial(10-i) * p**i * (1-p)**(10-i)
    if i == 1:
        ans2 = 1 - ans1

print(round(ans1, 3))
print(round(ans2, 3))
