# This is the solution to https://www.hackerrank.com/challenges/itertools-product/problem

from itertools import product
a = list(map(int, input().split()))
b = list(map(int, input().split()))
print(*list(product(a, b)))
