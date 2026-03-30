# 📘 NLP Day 5: From TF-IDF to Embeddings

## 🔹 TF-IDF (Vectorization)
- Converts text into numbers based on **word importance**
- Output is a **sparse vector** (many 0s)
- Each value represents a **word**

### Example
"I love AI" → [0, 1, 0, 1]

---

## 🔹 Embeddings
- Converts text into **dense vectors** (decimal numbers)
- Captures **semantic meaning** of the sentence
- Output size is **fixed** (e.g., 384 values), not based on number of words

### Example
"I love AI" → [0.12, -0.45, 0.67, 0.23, ...]

---

## ⚡ Key Difference

| Feature | TF-IDF | Embeddings |
|--------|--------|-----------|
| Based on | Word frequency | Meaning |
| Vector type | Sparse | Dense |
| Size depends on | Vocabulary | Model (fixed) |

---

## 🧠 Important Concept

**Number of words ≠ number of output values in embeddings**

- "I love AI" (3 words) → 384 values  
- "AI is the future" (4 words) → 384 values  

✔ Because embeddings represent **meaning, not words**

---

## 🚀 Conclusion

- TF-IDF = **importance of words**  
- Embeddings = **meaning of sentences**  
- Embeddings are preferred in modern NLP