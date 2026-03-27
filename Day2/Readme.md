# 📘 Tokenization (NLP)

## 💡 What is Tokenization?
Tokenization is the process of **splitting text into smaller units (tokens)**.

👉 Example:  
"I love NLP" → ["I", "love", "NLP"]

---

## 🚀 Why?
- Computers can’t understand raw text  
- Converts text into processable form  
- First step in NLP  

---

## 🔹 Example (Python)
```python
from nltk.tokenize import word_tokenize

text = "NLP is interesting!"
print(word_tokenize(text))