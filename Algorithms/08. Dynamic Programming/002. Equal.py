# Problem: https://www.hackerrank.com/challenges/equal/problem
# Score: 30

# the idea here is that we can go not just to minimum element in array,
# but also to min+1 and min+2
target = [0, 1, 2]


def solution(arr):
    min_arr = min(arr)
    results = [0] * len(target) # array for results with each target
    for item in arr:
        for i in target:
            gap = item - min_arr + i
            results[i] += gap // 5 + (gap%5) // 2 + (gap%5)%2
    return min(results)


for t in range(int(input())):
    input()
    items = list(map(int, input().split()))
    print(solution(items))
