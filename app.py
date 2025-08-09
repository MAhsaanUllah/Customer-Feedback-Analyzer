import streamlit as st
import pandas as pd
from bertopic import BERTopic
from transformers import pipeline

st.set_page_config(page_title="Customer Review Analyzer", layout="wide")

st.title("🧠 Customer Review Analyzer")
st.markdown("Analyze customer feedback with Topic Modeling, Summarization, and Sentiment Analysis.")

# 📂 Upload CSV
uploaded_file = st.file_uploader("Upload a CSV file with a 'review' column", type=["csv"])

if uploaded_file:
    df = pd.read_csv(uploaded_file)
    st.write(f"✅ Loaded {len(df)} reviews")
    
    # Topic Modeling
    st.subheader("📌 Topic Modeling")
    topic_model = BERTopic()
    topics, probs = topic_model.fit_transform(df['review'])
    
    topic_info = topic_model.get_topic_info()
    st.dataframe(topic_info)
    
    # Summarization
    st.subheader("📝 Review Summarization")
    summarizer = pipeline("summarization", model="facebook/bart-large-cnn")
    example_summary = summarizer(" ".join(df['review'].head(3)), max_length=50, min_length=10, do_sample=False)
    st.write(example_summary[0]['summary_text'])
    
    # Visualization
    st.subheader("📊 Topic Visualizations")
    st.plotly_chart(topic_model.visualize_topics(), use_container_width=True)
    st.plotly_chart(topic_model.visualize_barchart(), use_container_width=True)
    st.plotly_chart(topic_model.visualize_term_rank(), use_container_width=True)

else:
    st.info("Please upload a CSV file to start.")
