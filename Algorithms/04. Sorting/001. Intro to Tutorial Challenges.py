# Problem: https://www.hackerrank.com/challenges/tutorial-intro/problem
# Score: 30


v = int(input())
n = int(input())
arr = list(map(int, input().split()))
i = 0
while arr[i] != v:
    i += 1
print(i)
