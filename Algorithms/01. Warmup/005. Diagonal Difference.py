# Problem: https://www.hackerrank.com/challenges/diagonal-difference/problem
# Score: 10


a = []
result = 0
for i in range(int(input())):
    a = list(map(int, input().split()))
    result += a[i] - a[- 1 - i]
print(abs(result))
