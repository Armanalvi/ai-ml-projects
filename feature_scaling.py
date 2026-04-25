from sklearn.preprocessing import StandardScaler

X = [[1],[2],[3]]
scaler = StandardScaler()

print(scaler.fit_transform(X))
