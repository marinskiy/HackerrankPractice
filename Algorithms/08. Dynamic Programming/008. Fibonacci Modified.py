# Problem: https://www.hackerrank.com/challenges/fibonacci-modified/problem
# Score: 45


n1, n2, n = map(int, input().split())
sequence = [n1, n2]
if n <= 2:
    print(sequence[n-1])
else:
    for i in range(n-2):
        sequence.append(sequence[-2] + sequence[-1]**2)
    print(sequence[-1])
