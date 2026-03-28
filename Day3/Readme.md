# NLP Day 3: Tokenization → Vectorization

## Example Output
```
[[0 0 1 1]
 [1 1 0 1]]
```

## Vocabulary
```
['fun', 'is', 'love', 'nlp']
```

Each column represents a word:

| fun | is | love | nlp |
|-----|----|------|-----|

---

## Understanding the Array

### Sentence 1: "I love NLP"
```
[0 0 1 1]
```
- fun → 0 (not present)
- is → 0 (not present)
- love → 1 (present)
- nlp → 1 (present)

---

### Sentence 2: "NLP is fun"
```
[1 1 0 1]
```
- fun → 1 (present)
- is → 1 (present)
- love → 0 (not present)
- nlp → 1 (present)

---

## Meaning of Values

- **0** → word is NOT present  
- **1** → word is present once  
- **>1** → word appears multiple times  

---

## Final Understanding

Each sentence is converted into a **numeric vector** based on word counts.

👉 This is called **Bag of Words (BoW)**  
👉 It helps machines understand text data
