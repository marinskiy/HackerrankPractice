def pickingNumbers(arr):
    result = 0
    for i in range(len(arr)):
        maxCount = max(arr.count(arr[i]) + arr.count(arr[i] + 1), arr.count(arr[i]) + arr.count(arr[i] - 1))
        if maxCount > result:
            result = maxCount
    return result


n = int(input().strip())
arr = list(map(int, input().strip().split(' ')))
result = pickingNumbers(arr)
print(result)
