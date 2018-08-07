# Problem:  https://www.hackerrank.com/challenges/itertools-product/problem
# Score: 10


from itertools import product


a = list(map(int, input().split()))
b = list(map(int, input().split()))
print(*list(product(a, b)))
