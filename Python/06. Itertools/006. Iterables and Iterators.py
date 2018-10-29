# Problem: https://www.hackerrank.com/challenges/iterables-and-iterators/problem
# Score: 40


n, number, k = int(input()), input().split().count('a'), int(input())
not_a = 1
for i in range(k):
    not_a = not_a * (n - number - i) / (n - i)
print(1-not_a)
