# Problem: https://www.hackerrank.com/challenges/cats-and-a-mouse/problem
# Score: 15


def catAndMouse(catA, catB, mouseC):
    distanceA = abs(catA - mouseC)
    distanceB = abs(catB - mouseC)
    if distanceA > distanceB:
        print('Cat B')
    elif distanceA == distanceB:
        print('Mouse C')
    else:
        print('Cat A')


n = int(input())
for i in range(n):
    catA, catB, mouseC = map(int, input().split())
    catAndMouse(catA, catB, mouseC)
