
from sklearn.linear_model import Lasso

model = Lasso()
model.fit([[1],[2],[3]], [1,2,3])

print(model.predict([[4]]))
