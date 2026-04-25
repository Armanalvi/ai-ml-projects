from sklearn.linear_model import LinearRegression

X = [[1,2],[2,3],[3,4]]
y = [5,7,9]

model = LinearRegression()
model.fit(X,y)

print(model.predict([[4,5]]))
