from sklearn.feature_extraction.text import CountVectorizer

# Sample text
text = ["I love NLP", "NLP is fun"]

# Step 1 + 2: Tokenization + Vectorization
vectorizer = CountVectorizer()
X = vectorizer.fit_transform(text)

# Vocabulary (words mapped to numbers)
print(vectorizer.get_feature_names_out())

# Vectorized form
print(X.toarray())