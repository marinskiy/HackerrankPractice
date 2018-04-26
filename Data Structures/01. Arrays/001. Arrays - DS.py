# This is the solution to https://www.hackerrank.com/challenges/arrays-ds/problem


def reverseArray(arr):
    result = arr[::-1]
    return result


arrСount = int(input())
arr = list(map(int, input().rstrip().split()))
result = reverseArray(arr)
print(*result)
