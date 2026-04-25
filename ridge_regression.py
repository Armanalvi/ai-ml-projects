
from sklearn.linear_model import Ridge

model = Ridge()
model.fit([[1],[2],[3]], [1,2,3])

print(model.predict([[4]]))
