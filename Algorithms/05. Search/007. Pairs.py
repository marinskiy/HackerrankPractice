# Problem: https://www.hackerrank.com/challenges/pairs/problem
# Score: 50


# use two-pointers approach on a sorted array
n, value = map(int, input().split())
points = sorted(list(map(int, input().split())))

ans = 0
i = 0
j = 1

while j < n:
    if points[j] - points[i] == value:
        ans += 1
        j += 1
    elif points[j] - points[i] > value:
        i += 1
    elif points[j] - points[i] < value:
        j += 1

print(ans)
