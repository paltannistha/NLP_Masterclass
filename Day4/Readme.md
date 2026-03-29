# TF-IDF in NLP

## What is TF-IDF?
TF-IDF (Term Frequency - Inverse Document Frequency) is a technique used in Natural Language Processing (NLP) to find how important a word is in a document compared to a collection of documents.

---

## 1. Term Frequency (TF)
TF measures how often a word appears in a document.

TF = (Number of times word appears) / (Total words in document)

---

## 2. Inverse Document Frequency (IDF)
IDF measures how unique or rare a word is across all documents.

IDF = log(Total documents / Documents containing the word)

---

## 3. TF-IDF Formula
TF-IDF = TF × IDF

---

## Key Idea
- High TF → word is frequent in the document  
- High IDF → word is rare across documents  
- High TF-IDF → important word

---

## Example
Documents:
1. I love AI  
2. AI is powerful  
3. I love coding  

- "coding" → high TF, high IDF → important  
- "AI" → high TF, low IDF → less important  

---

## Why use TF-IDF?
- Converts text into numbers  
- Helps in text classification, search, and keyword extraction  

---

## One-line Summary
TF-IDF highlights important words by combining frequency and uniqueness.