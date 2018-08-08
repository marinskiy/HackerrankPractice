# Problem: https://www.hackerrank.com/challenges/itertools-combinations-with-replacement/problem
# Score: 10


import itertools


s = input().split()
string, number = sorted(s[0]), int(s[1])
print(*list(map(''.join, itertools.combinations_with_replacement(string, number))), sep='\n')
