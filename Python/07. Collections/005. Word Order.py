# Problem: https://www.hackerrank.com/challenges/word-order/problem
# Score: 50


from collections import Counter, OrderedDict


class OrderedCounter(Counter, OrderedDict):
    pass


ordered_counter = OrderedCounter(input() for _ in range(int(input())))
print(len(ordered_counter))
print(*ordered_counter.values())
