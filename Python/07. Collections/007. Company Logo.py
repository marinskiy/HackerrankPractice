# Problem: https://www.hackerrank.com/challenges/py-collections-deque/problem
# Score: 30


from collections import Counter, OrderedDict


class OrderedCounter(Counter, OrderedDict):
    pass


letters = OrderedCounter(sorted(input())).most_common(3)
[print(*letter) for letter in letters]
