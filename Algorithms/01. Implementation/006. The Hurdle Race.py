# This is the solution to https://www.hackerrank.com/challenges/the-hurdle-race/problem


n, k = map(int, input().split())
hurdles = list(map(int, input().split()))
numberOfPotions = max(0, max(hurdles) - k)
print(numberOfPotions)
