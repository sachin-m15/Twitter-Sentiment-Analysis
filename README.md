Data Preprocessing:<br>
    You've cleaned the text data by removing non-alphabetic characters, converting text to lowercase, and stemming the words.<br>
    The target labels are adjusted from 0 (negative) and 4 (positive) to 0 and 1.
    
Feature Extraction:<br>
     You've used the TfidfVectorizer to convert the cleaned text data into numerical features.<br>

Model Training:<br>
     You trained a logistic regression model on the processed text data.<br>

Model Evaluation:<br>
     After training the model, you evaluate it on the test set, achieving an accuracy of approximately 77.8%.<br>

Saving the Model:<br>
     The trained model and vectorizer are saved using pickle for future use.<br>

Streamlit Application:<br>
     You set up a Streamlit app for live sentiment prediction.<br>

