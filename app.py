import streamlit as st
import pickle
import re
from sklearn.feature_extraction.text import TfidfVectorizer
from nltk.corpus import stopwords
import nltk
from ntscraper import Nitter

# Download stopwords once, using Streamlit's caching
@st.cache_resource
def load_stopwords():
    try:
        stop_words = stopwords.words('english')
    except LookupError:
        nltk.download('stopwords')
        stop_words = stopwords.words('english')
    return stop_words

# Load model and vectorizer once
@st.cache_resource
def load_model_and_vectorizer():
    with open("C:/Users/shrey/Desktop/code/projects/Twitter_sentiment_Analysis/mode.pkl", 'rb') as model_file:
        model = pickle.load(model_file)
    with open("C:/Users/shrey/Desktop/code/projects/Twitter_sentiment_Analysis/vectorizer.pkl", 'rb') as vectorizer_file:
        vectorizer = pickle.load(vectorizer_file)
    return model, vectorizer

# Define sentiment prediction function
def predict_sentiment(text, model, vectorizer, stop_words):
    text = re.sub('[^a-zA-Z]', ' ', text)
    text = text.lower()
    text = text.split()
    text = [word for word in text if word not in stop_words]
    text = ' '.join(text)
    text = [text]
    text = vectorizer.transform(text)
    sentiment = model.predict(text)
    return "Negative" if sentiment == 0 else "Positive"

# Initialize Nitter scraper
@st.cache_resource
def initialize_scraper():
    return Nitter(log_level=1)

# Function to create a stylish colored card
def create_card(tweet_text, sentiment):
    color = "linear-gradient(135deg, #4CAF50, #2E7D32);" if sentiment == "Positive" else "linear-gradient(135deg, #E53935, #B71C1C);"
    emoji = "😊" if sentiment == "Positive" else "😞"
    card_html = f"""
    <div style="
        background: {color};
        padding: 20px;
        border-radius: 20px;
        margin: 20px 0;
        box-shadow: 0 10px 20px rgba(0,0,0,0.2);
        transition: transform 0.3s ease;
    " onmouseover="this.style.transform='scale(1.03)'" onmouseout="this.style.transform='scale(1)'">
        <h4 style="color: white; margin-bottom: 10px;">{sentiment} Sentiment {emoji}</h4>
        <p style="color: white; font-size: 16px; line-height: 1.6;">{tweet_text}</p>
    </div>
    """
    return card_html

# Main app logic
def main():
    # Global page background and input styling
    st.markdown(""" 
    <style>
    .stApp {
        background: linear-gradient(to right, #e0eafc, #cfdef3);
        padding: 20px;
    }
    textarea, input[type="text"] {
        background: #ffffff !important;
        border: 2px solid #6a11cb !important;
        border-radius: 10px !important;
        padding: 10px !important;
        color: #333333 !important;
        font-size: 16px !important;
    }
    div.stButton > button {
        background: linear-gradient(135deg, #6a11cb, #2575fc);
        color: white;
        border: none;
        padding: 0.6em 2em;
        border-radius: 10px;
        font-size: 1rem;
        font-weight: bold;
        transition: background 0.3s ease;
        box-shadow: 0px 4px 12px rgba(0, 0, 0, 0.1);
    }
    div.stButton > button:hover {
        background: linear-gradient(135deg, #2575fc, #6a11cb);
        transform: scale(1.05);
    }
    .stSelectbox select {
        background: #ffffff !important;
        border: 2px solid #6a11cb !important;
        border-radius: 8px !important;
        padding: 10px !important;
        color: #333333 !important;
        font-size: 16px !important;
        box-shadow: 0 4px 6px rgba(0,0,0,0.1);
    }
    .stSelectbox label {
        font-size: 1.2rem !important;
        font-weight: bold !important;
        color: #6a11cb;
        margin-bottom: 10px;
    }
    /* Custom Style for 'Enter text to analyze sentiment' */
    .stTextArea label {
        font-size: 1.2rem !important;
        font-weight: bold !important;
        color: #6a11cb; /* Text color for label */
        margin-bottom: 12px !important;
    }
    .stTextArea textarea {
        background-color: #f1f8ff !important;
        border: 2px solid #6a11cb !important;
        border-radius: 10px !important;
        padding: 12px !important;
        font-size: 16px !important;
        color: #333333 !important;
        box-shadow: 0 4px 6px rgba(0,0,0,0.1) !important;
    }
    /* Custom style for the background of text input */
    .stTextArea textarea {
        background-color: #e0f7fa !important;  /* Light teal background */
    }
    </style>
    """, unsafe_allow_html=True)

    # Stylish heading
    st.markdown(""" 
    <h1 style="
        background: linear-gradient(135deg, #6a11cb, #2575fc);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        font-size: 3.5rem;
        font-weight: bold;
        text-align: center;
        margin-bottom: 40px;
    ">
        Twitter Sentiment Analysis 🚀
    </h1>
    """, unsafe_allow_html=True)

    # Load assets
    stop_words = load_stopwords()
    model, vectorizer = load_model_and_vectorizer()
    scraper = initialize_scraper()

    # Option select with styled selectbox
    option = st.selectbox("Choose an option", ["Input text", "Get tweets from user"])

    if option == "Input text":
        text_input = st.text_area("Enter text to analyze sentiment")
        if st.button("Analyze"):
            sentiment = predict_sentiment(text_input, model, vectorizer, stop_words)
            # Styled result card
            result_color = "linear-gradient(135deg, #4CAF50, #2E7D32);" if sentiment == "Positive" else "linear-gradient(135deg, #E53935, #B71C1C);"
            emoji = "✅" if sentiment == "Positive" else "❌"
            result_html = f"""
             <div style="
                 background: linear-gradient(135deg, #6a11cb, #2575fc);
                 padding: 30px;
                 border-radius: 20px;
                 margin: 25px 0;
                 box-shadow: 0 10px 25px rgba(169, 169, 169, 0.5);
                 text-align: center;
                 transition: transform 0.3s ease;
             " onmouseover="this.style.transform='scale(1.05)'" onmouseout="this.style.transform='scale(1)'">
               <h2 style="color: white; font-size: 2rem;">{sentiment} {emoji}</h2>
            </div>
            """
            st.markdown(result_html, unsafe_allow_html=True)

    elif option == "Get tweets from user":
        username = st.text_input("Enter Twitter username")
        if st.button("Fetch Tweets"):
            tweets_data = scraper.get_tweets(username, mode='user', number=5)
            if 'tweets' in tweets_data:
                for tweet in tweets_data['tweets']:
                    tweet_text = tweet['text']
                    sentiment = predict_sentiment(tweet_text, model, vectorizer, stop_words)
                    card_html = create_card(tweet_text, sentiment)
                    st.markdown(card_html, unsafe_allow_html=True)
            else:
                st.write("No tweets found or an error occurred.")

if __name__ == "__main__":
    main()
