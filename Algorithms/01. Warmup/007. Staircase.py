# Problem: https://www.hackerrank.com/challenges/staircase/problem
# Score: 10


def staircase(a):
    for i in range(1, a + 1):
        print((a - i) * ' ' + i * "#")


n = int(input())
staircase(n)
