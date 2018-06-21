# Problem: https://www.hackerrank.com/challenges/compare-the-triplets/problem
# Score: 10


a = list(map(int, input().split()))
b = list(map(int, input().split()))
aliceScore = sum([(1 if a[i] > b[i] else 0) for i in range(3)])
bobScore = sum([(1 if a[i] < b[i] else 0) for i in range(3)])
print(aliceScore, bobScore)
