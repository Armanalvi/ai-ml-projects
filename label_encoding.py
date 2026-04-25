from sklearn.preprocessing import LabelEncoder

data = ["low","medium","high"]
le = LabelEncoder()

print(le.fit_transform(data))
