# Problem: https://www.hackerrank.com/challenges/birthday-cake-candles/problem
# Score: 10


n = int(input())
ar = list(map(int, input().split()))
print(ar.count(max(ar)))
