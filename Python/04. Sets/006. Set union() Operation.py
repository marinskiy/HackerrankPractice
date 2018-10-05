# Problem: https://www.hackerrank.com/challenges/py-set-union/problem
# Score: 10


_, a = input(), set(input().split())
_, b = input(), set(input().split())
print(len(a.union(b)))
