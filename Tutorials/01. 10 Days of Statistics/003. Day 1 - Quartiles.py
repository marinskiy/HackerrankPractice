# Problem: https://www.hackerrank.com/challenges/s10-quartiles/problem
# Score: 30


def find_median(arr):
    if len(arr) % 2 == 1:
        return arr[len(arr) // 2]
    else:
        return (arr[len(arr) // 2] + arr[len(arr) // 2 - 1]) // 2


n = input()
arr = sorted(list(map(int, input().split())))
print(find_median(arr[:len(arr)//2]))
print(find_median(arr))
print(find_median(arr[len(arr) // 2 + len(arr) % 2:]))
