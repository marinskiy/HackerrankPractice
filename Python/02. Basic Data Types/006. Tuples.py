# Problem: https://www.hackerrank.com/challenges/python-tuples/problem
# Score: 10


n = int(input())
print(hash(tuple(map(int, input().split()))))
