# Problem: https://www.hackerrank.com/challenges/py-if-else/problem
# Score: 10


def weird_or_not(n):
    if n % 2 == 1 or (6 <= n <= 20):
        print("Not Weird")
    else:
        print("Weird)
weird_or_not(n)
