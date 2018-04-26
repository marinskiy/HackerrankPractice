# This is the solution to https://www.hackerrank.com/challenges/capitalize/problem


st = input()
print(' '.join(word.capitalize() for word in st.split(' ')))
