# Problem: https://www.hackerrank.com/challenges/mini-max-sum/problem
# Score: 10


arr = list(map(int, input().split()))
print(sum(arr) - max(arr), sum(arr) - min(arr))
