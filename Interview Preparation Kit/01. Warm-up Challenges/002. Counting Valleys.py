# Problem: https://www.hackerrank.com/challenges/counting-valleys/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=warmup
# Score: 15


def counting_valleys(n, s):
    current_level = 0
    count = 0
    for i in range(n):
        if s[i] == 'U':
            current_level += 1
        elif s[i] == 'D':
            current_level -= 1
            if current_level == -1:
                count += 1
    return count


n = int(input().strip())
s = input().strip()
result = counting_valleys(n, s)
print(result)
