from sklearn.linear_model import LinearRegression

X = [[1000],[1500],[2000]]
y = [50,75,100]

model = LinearRegression()
model.fit(X,y)

print("Price:", model.predict([[1800]]))
