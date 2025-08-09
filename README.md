# 📊 Customer Feedback Analyzer

![Python](https://img.shields.io/badge/Python-3.8%2B-blue)
![Streamlit](https://img.shields.io/badge/Streamlit-App-orange)
![NLP](https://img.shields.io/badge/NLP-Project-green)
![License](https://img.shields.io/badge/License-MIT-lightgrey)

---

## 📌 Overview
This project uses **Natural Language Processing (NLP)** to:
- Identify main **topics** in customer reviews.
- Summarize them into **short, human-readable text**.
- Analyze **sentiment** for each topic.
- Display results in an **interactive Streamlit dashboard**.

📊 Built using **BERTopic**, **BART**, and **TextRank**.

---

## 🚀 Features
- **Topic Modeling** – Groups similar reviews together.
- **Summarization** – Extractive (TextRank) & Abstractive (BART).
- **Sentiment Analysis** – Understand mood for each topic.
- **Interactive Visualization** – Topic clusters, frequency, and keywords.
- **Streamlit UI** – Simple interface for end users.

---

## 📂 Project Structure

📂 project/
├── app.py # Streamlit app
├── requirements.txt # Dependencies
├── project.ipynb # Jupyter/Colab notebook
├── README.md # Project documentation
├── data/
│ └── sample_reviews.csv # Small sample dataset for testing
└── images/
└── (screenshots later)



---

## 📊 Workflow

### **Phase 1 – Project Setup & Introduction**
Define project goals, applications, dataset, and tech stack.

### **Phase 2 – Text Preprocessing**
Clean reviews: lowercase, remove stopwords, lemmatize, remove duplicates.

### **Phase 3 – Topic Modeling (BERTopic)**
Extract main topics from reviews and list top keywords.

### **Phase 4 – Review Summarization**
Summarize reviews with **TextRank** and **BART**.

### **Phase 5 – Topic-wise Sentiment & Summarization**
Combine topics with summaries and sentiment analysis.

### **Phase 6 – Topic Interpretability**
Visualize topics with BERTopic’s tools.

### **Phase 7 – Streamlit App**
Interactive UI for exploring topics and summaries.

---

## 📦 Installation
```bash
git clone https://github.com/your-username/your-repo-name.git
cd your-repo-name
pip install -r requirements.txt


▶️ Usage
Run the Streamlit app:

streamlit run app.py

📊 Dataset
We use the Amazon Fine Food Reviews dataset.
For testing, a sample dataset (data/sample_reviews.csv) is provided.


📜 License
This project is licensed under the MIT License.

⭐ Acknowledgments
BERTopic

Hugging Face Transformers

Streamlit



---

## **2 ️⃣ Sample Data File**
Create a file: `data/sample_reviews.csv`
```csv
review
I love the taste of this product! Great flavor and fresh.
The delivery was late and the packaging was damaged.
Worth the price. Very good value for money.
Terrible taste. I will never buy this again.
Fast delivery, excellent quality!


