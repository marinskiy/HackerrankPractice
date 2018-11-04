# Problem: https://www.hackerrank.com/challenges/py-collections-deque/problem
# Score: 20


from collections import deque


d = deque()
for _ in range(int(input())):
    line = input().split()
    if line[0] == 'append':
        d.append(line[1])
    elif line[0] == 'pop':
        d.pop()
    elif line[0] == 'popleft':
        d.popleft()
    elif line[0] == 'appendleft':
        d.appendleft(line[1])
print(*d)
