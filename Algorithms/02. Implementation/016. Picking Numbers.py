# Problem: https://www.hackerrank.com/challenges/picking-numbers
# Score: 20


def pickingNumbers(arr):
    result = 0
    checked = set()
    for i in range(len(arr)):
        if i not in checked:
            maxCount = max(arr.count(arr[i]) + arr.count(arr[i] + 1), arr.count(arr[i]) + arr.count(arr[i] - 1))
            if maxCount > result:
                result = maxCount
            checked.add(i)
    return result


n = int(input().strip())
arr = list(map(int, input().strip().split(' ')))
result = pickingNumbers(arr)
print(result)
