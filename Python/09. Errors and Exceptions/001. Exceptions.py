# Problem: https://www.hackerrank.com/challenges/exceptions/problem
# Score: 10


for _ in range(int(input())):
    a, b = input().split()
    try:
        print(int(a) // int(b))
    except BaseException as err:
        print("Error Code:", err)
