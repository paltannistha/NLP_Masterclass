from sklearn.feature_extraction.text import TfidfVectorizer

# Sample text data
documents = [
    "I love machine learning",
    "Machine learning is fun",
    "I love coding"
]

# Create TF-IDF object
vectorizer = TfidfVectorizer()

# Convert text to TF-IDF matrix
tfidf_matrix = vectorizer.fit_transform(documents)

# Get feature (word) names
feature_names = vectorizer.get_feature_names_out()

# Print results
print("Feature Names:", feature_names)
print("\nTF-IDF Matrix:\n", tfidf_matrix.toarray())