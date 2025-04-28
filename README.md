Data Preprocessing:
    You've cleaned the text data by removing non-alphabetic characters, converting text to lowercase, and stemming the words.
    The target labels are adjusted from 0 (negative) and 4 (positive) to 0 and 1.
    
Feature Extraction:
     You've used the TfidfVectorizer to convert the cleaned text data into numerical features.

Model Training:
     You trained a logistic regression model on the processed text data.

Model Evaluation:
     After training the model, you evaluate it on the test set, achieving an accuracy of approximately 77.8%.

Saving the Model:
     The trained model and vectorizer are saved using pickle for future use.

Streamlit Application:
     You set up a Streamlit app for live sentiment prediction.

