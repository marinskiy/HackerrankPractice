# Problem: https://www.hackerrank.com/challenges/battery/problem
# Score: 10


import pandas as pd
from sklearn.linear_model import LinearRegression


timeCharged = float(input())
data = pd.read_csv('trainingdata.txt', names=['charged', 'lasted'])
train = data[data['lasted'] < 8]
model = LinearRegression()
model.fit(train['charged'].values.reshape(-1, 1), train['lasted'].values.reshape(-1, 1))
ans = model.predict([[timeCharged]])
print(min(ans[0][0], 8))
