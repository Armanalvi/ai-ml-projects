
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

data = np.array([[1,0,1],[1,1,0],[0,1,1]])

print(cosine_similarity(data))
