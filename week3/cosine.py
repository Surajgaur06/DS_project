from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

s1 = "data science is fun"
s2 = "science makes data useful"
vectorizer = CountVectorizer().fit([s1, s2])
vector = vectorizer.tranceform([s1, s2])

cos_sim = cousine_similarity(vectors[0], vectors[1])[0][0]
print("Cousin Similarity: ", cos.sim)