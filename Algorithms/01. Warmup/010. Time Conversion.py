# Problem: https://www.hackerrank.com/challenges/time-conversion/problem
# Score: 15


import time
print(time.strftime('%H:%M:%S', time.strptime(input(), '%I:%M:%S%p')))
