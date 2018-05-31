# Problem: https://www.hackerrank.com/challenges/python-string-formatting/problem
# Score: 10


def print_formatted(number):
    width = len("{0:b}".format(number))
    for i in range(1, number + 1):
        print("{0:{width}d} {0:{width}o} {0:{width}X} {0:{width}b}".format(i, width=width))
