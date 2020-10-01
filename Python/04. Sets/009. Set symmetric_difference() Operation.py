# Problem: https://www.hackerrank.com/challenges/py-set-symmetric-difference-operation/problem
# Score: 10


_, english = input(), set(input().split())
_, french = input(), set(input().split())
print(len(english.symmetric_difference(french)))
