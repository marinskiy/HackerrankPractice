# Problem: https://www.hackerrank.com/challenges/s10-the-central-limit-theorem-3/problem
# Score: 30


# inputs
mean = 500
std = 80
n = 100
z = 1.96

# characteristics of sample
mean = mean
std = std / n**(1/2)

# Find the 95% interval
print(round(mean - std * z, 2))
print(round(mean + std * z, 2))
