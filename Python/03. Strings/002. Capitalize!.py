# Problem:  https://www.hackerrank.com/challenges/capitalize/problem
# Score: 20


st = input()
print(' '.join(word.capitalize() for word in st.split(' ')))
