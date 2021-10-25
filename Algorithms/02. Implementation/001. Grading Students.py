# Problem: https://www.hackerrank.com/challenges/grading/problem
# Score: 10


for _ in range(int(input())):
    grade = int(input())
    grade = grade - grade%5 + 5 if grade%5 > 2 and grade >= 38 else grade
   
print(grade)
