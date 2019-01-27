# Problem: https://www.hackerrank.com/challenges/construct-the-array/problem
# Score: 35


def count_array(n, k, x):
    dp = [[1], [1]]
    if x == 1:
        dp = [[1], [0]]
    else:
        dp = [[1], [1]]

    for x in range(n - 2):
        dp[0].append(dp[0][-1] * (k - 1) % (10 ** 9 + 7))
        dp[1].append((dp[0][-1] - dp[1][-1]) % (10 ** 9 + 7))
    return dp[1][-1]


n, k, x = map(int, input().split())
print(count_array(n, k, x))
