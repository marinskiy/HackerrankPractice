# Problem: https://www.hackerrank.com/challenges/two-arrays/problem
# Score: 40


n = int(input())
for _ in range(n):
    __, k = map(int, input().split())
    a = sorted(list(map(int, input().split())))
    b = sorted(list(map(int, input().split())), reverse=True)
    if all([a[i] + b[i] >= k for i in range(len(a))]):
        print('YES')
    else:
        print('NO')
