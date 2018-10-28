# Problem: https://www.hackerrank.com/challenges/py-check-strict-superset/problem
# Score: 10


a = set(input().split())
print(all(a > set(input().split()) for _ in range(int(input()))))
