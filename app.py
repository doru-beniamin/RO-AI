import streamlit as st
from transformers import pipeline

# Title of the app
st.title('Financial Sentiment Analysis')

# Load FinBERT model
model_name = "ProsusAI/finbert"
finbert_sentiment_pipeline = pipeline('sentiment-analysis', model=model_name)

# Text input
text_to_analyze = st.text_area("Enter the phrase to analyze:", height=150)

# Analyze button
if st.button('Analyze'):
    if text_to_analyze:
        # Perform analysis
        result = finbert_sentiment_pipeline(text_to_analyze)
        
        # Display results
        st.write(result)
    else:
        st.write("Please enter a phrase to analyze.")