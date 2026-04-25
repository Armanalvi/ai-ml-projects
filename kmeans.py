from sklearn.cluster import KMeans

X = [[1],[2],[10],[11]]

model = KMeans(n_clusters=2)
model.fit(X)

print(model.labels_)
