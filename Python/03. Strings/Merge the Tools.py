def merge_the_tools(string, k):
    # your code goes here
    n=int(len(string)/k)
    for i in range(n):
        s=""
        for j in string[i*k:(i+1)*k]:
            if j in s:
                continue
            else:
                s+=j
        print(s)
