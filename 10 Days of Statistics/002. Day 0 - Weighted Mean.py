# Problem: https://www.hackerrank.com/challenges/s10-weighted-mean/problem
# Score: 30


n = int(input())
arr = list(map(int, input().split()))
weights = list(map(int, input().split()))
print(round(sum([arr[x]*weights[x] for x in range(len(arr))]) / sum(weights), 1))
