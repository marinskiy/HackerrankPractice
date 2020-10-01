n = int(input())

a = n % 2

if a > 0 :
    print("Weird")
else:
    if 2 <= n <=5:
        print("Not Weird")
    elif 6 <= n <=20:
        print("Weird")
    elif n > 20:
        print("Not Weird")
