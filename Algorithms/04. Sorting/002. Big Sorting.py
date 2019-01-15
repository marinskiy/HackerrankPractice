# Problem: https://www.hackerrank.com/challenges/big-sorting/problem
# Score: 20


n = int(input())
arr = []
for i in range(n):
    arr.append(input())
arr.sort(key=int)
for _ in arr:
    print(_)
