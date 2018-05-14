# Problem: https://www.hackerrank.com/challenges/write-a-function/problem
# Score: 10


def is_leap(y):
    return y % 4 == 0 and (y % 100 != 0 or y % 400 == 0)
