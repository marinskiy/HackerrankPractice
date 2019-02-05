# Problem: https://www.hackerrank.com/challenges/marcs-cakewalk/problem
# Score: 15


_ = input()
calories = list(map(int, input().split()))
calories = sorted(calories, reverse=True)
ans = 0
for index, cupcake in enumerate(calories):
    ans += 2**index*cupcake
print(ans)
