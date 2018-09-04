# Problem: https://www.hackerrank.com/challenges/apple-and-orange/problem
# Score: 10


s, t, a, b, m, n = map(int, input().split() + input().split() + input().split())
apple = list(map(int, input().split()))
orange = list(map(int, input().split()))
print(sum(s <= a + i <= t for i in apple))
print(sum(s <= b + i <= t for i in orange))
