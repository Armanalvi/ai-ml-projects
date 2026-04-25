
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB

texts = ["free money","hi friend","win prize","hello"]
labels = [1,0,1,0]

vec = CountVectorizer()
X = vec.fit_transform(texts)

model = MultinomialNB()
model.fit(X,labels)

print(model.predict(vec.transform(["free prize"])))
