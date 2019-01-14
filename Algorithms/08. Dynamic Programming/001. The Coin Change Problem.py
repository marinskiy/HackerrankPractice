# Problem: https://www.hackerrank.com/challenges/coin-change/problem
# Score: 60


n, m = map(int, input().split())
coins = list(map(int, input().split()))
ans = [1] + [0] * n
for i in range(m):
    for j in range(coins[i], n + 1):
        ans[j] += ans[j - coins[i]]
print(ans[-1])
