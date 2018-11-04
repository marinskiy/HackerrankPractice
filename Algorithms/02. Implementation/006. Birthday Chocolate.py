# Problem: https://www.hackerrank.com/challenges/the-birthday-bar/problem
# Score: 10


n, s = int(input().strip()), list(map(int, input().split()))
d, m = map(int, input().split())
print(sum([sum(s[i: i + m]) == d for i in range(len(s) - m + 1)]))
