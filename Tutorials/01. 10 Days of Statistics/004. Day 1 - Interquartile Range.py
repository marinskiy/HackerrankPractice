# Problem: https://www.hackerrank.com/challenges/s10-interquartile-range/problem
# Score: 30


def find_median(arr):
    if len(arr) % 2 == 1:
        return arr[len(arr) // 2]
    else:
        return (arr[len(arr) // 2] + arr[len(arr) // 2 - 1]) / 2


# create array
n = int(input())
values = list(map(int, input().split()))
freq = list(map(int, input().split()))
arr = []
for i in range(n):
    arr += [values[i]] * freq[i]
arr = sorted(arr)

# find iqr
iqr = float(find_median(arr[len(arr) // 2 + len(arr) % 2:]) - find_median(arr[:len(arr)//2]))
print(iqr)
