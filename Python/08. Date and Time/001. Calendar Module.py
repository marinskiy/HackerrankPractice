# Problem: https://www.hackerrank.com/challenges/calendar-module/problem
# Score: 10


import calendar


m, d, y = map(int, input().split())
print(calendar.day_name[calendar.weekday(y, m, d)].upper())
