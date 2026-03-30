# Sample text data
texts = ["I love AI", "AI is the future", "I enjoy learning NLP"]

# -----------------------------
# 1. TF-IDF Vectorization
# -----------------------------
from sklearn.feature_extraction.text import TfidfVectorizer

tfidf = TfidfVectorizer()
tfidf_vectors = tfidf.fit_transform(texts)

print("TF-IDF Vectors:\n", tfidf_vectors.toarray())

# -----------------------------
# 2. Embeddings (Sentence Level)
# -----------------------------
from sentence_transformers import SentenceTransformer

model = SentenceTransformer('all-MiniLM-L6-v2')
embeddings = model.encode(texts)

print("\nEmbeddings:\n", embeddings)