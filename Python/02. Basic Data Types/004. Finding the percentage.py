# Problem: https://www.hackerrank.com/challenges/finding-the-percentage/problem
# Score: 10


def readScores(listOfStudents):
    line = list(input().split())
    avScore = sum(map(float, line[1:])) / 3
    name = line[0]
    listOfStudents[name] = avScore


n = int(input())
listOfStudents = dict()
for i in range(n):
    readScores(listOfStudents)
print('%.2f' % listOfStudents[input()])
