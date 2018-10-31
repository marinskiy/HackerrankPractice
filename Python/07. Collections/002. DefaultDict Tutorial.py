# Problem: https://www.hackerrank.com/challenges/defaultdict-tutorial/problem
# Score: 20


from collections import defaultdict


n, m = map(int, input().split())
d = defaultdict(list)
for i in range(1, n + 1):
    d[input()].append(str(i))
for i in range(m):
    print(' '.join(d[input()]) or -1)
