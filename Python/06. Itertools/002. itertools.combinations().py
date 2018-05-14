# Problem:  https://www.hackerrank.com/challenges/itertools-combinations/problem
# Score: 10


import itertools


def printCombinations(string, number):
    string = sorted(string)
    for i in range(1, number + 1):
        combinationsList = list(itertools.combinations(string, i))
        for j in combinationsList:
            print(''.join(j))


s = input().split()
string, number = s[0], int(s[1])
printCombinations(string, number)
