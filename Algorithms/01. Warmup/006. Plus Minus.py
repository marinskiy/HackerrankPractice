# Problem: https://www.hackerrank.com/challenges/plus-minus/problem
# Score: 10


n = int(input())
arr = list(map(int, input().split()))
print(round(len([x for x in arr if x > 0]) / n, 6))
print(round(len([x for x in arr if x < 0]) / n, 6))
print(round(len([x for x in arr if x == 0]) / n, 6))
