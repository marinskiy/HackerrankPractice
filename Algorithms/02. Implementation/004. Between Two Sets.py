# Problem: https://www.hackerrank.com/challenges/between-two-sets/problem
# Score: 10


n, m = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
count = 0
for i in range(max(a), min(b)+1):
    if all(i % x == 0 for x in a) and all(x % i == 0 for x in b):
        count += 1
print(count)
