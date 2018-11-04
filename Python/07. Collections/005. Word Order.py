# Problem: https://www.hackerrank.com/challenges/word-order/problem
# Score: 50


from collections import OrderedDict


ordered_dict = OrderedDict()
for _ in range(int(input())):
    word = input()
    ordered_dict[word] = ordered_dict.get(word, 0) + 1
print(len(ordered_dict))
print(*ordered_dict.values())
