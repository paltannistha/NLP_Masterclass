import nltk
nltk.download('punkt')
nltk.download('punkt_tab')

# Word Tokenization
from nltk.tokenize import word_tokenize

text = "NLP is powerful and interesting!"
tokens = word_tokenize(text)

print(tokens)

# Sentence Tokenization
from nltk.tokenize import sent_tokenize

text = "NLP is fun. It is widely used in AI."
sentences = sent_tokenize(text)

print(sentences)

# Custom Tokenization (Regex-based)
import re

text = "NLP is amazing! #AI @2026"
tokens = re.findall(r'\b\w+\b', text)

print(tokens)