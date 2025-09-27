# 📊 Customer Feedback Analyzer

![Python](https://img.shields.io/badge/Python-3.8%2B-blue)
![Streamlit](https://img.shields.io/badge/Streamlit-App-orange)
![NLP](https://img.shields.io/badge/NLP-Project-green)
![License](https://img.shields.io/badge/License-MIT-lightgrey)
[![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/MAhsaanUllah/Customer-Feedback-Analyzer/blob/main/customer-feedback-analyzer.ipynb)
[![Hugging Face](https://img.shields.io/badge/🤗-Hugging%20Face-yellow)](https://huggingface.co/)

---

## 📌 Overview
This project applies **Natural Language Processing (NLP)** techniques to analyze customer reviews.  
It helps businesses uncover insights by:  
- Identifying main **topics** in customer feedback.  
- Summarizing them into **short, human-readable text**.  
- Performing **sentiment analysis** per topic.  
- Presenting results in an **interactive Streamlit dashboard**.  

🔑 Built using **BERTopic**, **BART**, **TextRank**, and **Hugging Face Transformers**.

---

## 🚀 Features
- **Topic Modeling** – Grouping similar reviews with BERTopic.  
- **Summarization** – Extractive (TextRank) & Abstractive (BART).  
- **Sentiment Analysis** – Positive, negative, neutral sentiment detection.  
- **Interactive Visualization** – Topic clusters, frequencies, and keywords.  
- **Streamlit App** – User-friendly interface for non-technical users.  

---

## 📂 Project Structure

project/
├── app.py # Streamlit app
├── requirements.txt # Dependencies
├── customer-feedback-analyzer.ipynb # Jupyter/Colab notebook
├── README.md # Project documentation
├── data/
│ ├── sample_reviews.csv # Sample dataset
│ └── customers_200_reviews.csv
└── images/ # Screenshots (to be added)


---

## 📊 Workflow
1. **Data Preprocessing** → Lowercasing, stopword removal, lemmatization.  
2. **Topic Modeling (BERTopic)** → Extract major topics & keywords.  
3. **Review Summarization** → Using TextRank + BART.  
4. **Sentiment Analysis** → Topic-wise sentiment insights.  
5. **Visualization** → BERTopic visual tools.  
6. **Streamlit App** → End-to-end interactive UI.  

---

## ⚙️ Installation
```bash
git clone https://github.com/MAhsaanUllah/Customer-Feedback-Analyzer.git
cd Customer-Feedback-Analyzer
pip install -r requirements.txt

▶️ Usage

Run the Streamlit app:

streamlit run app.py

📊 Dataset

Primary dataset: Amazon Fine Food Reviews.

Testing: data/sample_reviews.csv (included).

Sample rows:

I love the taste of this product! Great flavor and fresh.
The delivery was late and the packaging was damaged.
Worth the price. Very good value for money.
Terrible taste. I will never buy this again.
Fast delivery, excellent quality!

📜 License

This project is licensed under the MIT License.

🙌 Acknowledgments

BERTopic

Hugging Face Transformers

Streamlit

✨ Recruiter Note

This project demonstrates:

Practical NLP Applications → Topic modeling, summarization, and sentiment analysis.

End-to-End Workflow → From raw text preprocessing to a deployable Streamlit app.

Business Impact → Helps companies transform raw customer reviews into actionable insights.

🔗 Relevant for roles in Data Science, NLP Engineering, and AI/ML.
