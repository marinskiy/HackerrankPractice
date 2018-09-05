# Problem: https://www.hackerrank.com/challenges/kangaroo/problem
# Score: 10


def kangaroo(x1, v1, x2, v2):
    return 'YES' if (v1 > v2) and (x2 - x1) % (v2 - v1) == 0 else 'NO'


x1, v1, x2, v2 = map(int, input().split())
print(kangaroo(x1, v1, x2, v2))
