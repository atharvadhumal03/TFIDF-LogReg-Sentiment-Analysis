# TF-IDF + Logistic Regression | Sentiment Analysis on IMDB Movie Review Dataset

## 📊 Project Overview
### Introduction
This project implements a comprehensive sentiment analysis system for movie reviews using Natural Language Processing (NLP) and machine learning techniques. The system processes raw text from IMDB movie reviews and classifies them as either positive or negative sentiments with high accuracy. The solution includes a complete pipeline from data preprocessing to model deployment via an interactive web interface.

### Objectives
- Build an accurate sentiment classifier capable of understanding the emotional tone in movie reviews.
- Develop robust text preprocessing to handle messy real-world text data including HTML tags, special characters, and varied formatting
- Create a production-ready solution with modular code architecture separating preprocessing logic from model inference.
- Deploy an accessible web application allowing users to analyze movie reviews in real-time through an intuitive interface.
- Establish a scalable ML pipeline that can be easily maintained and updated with new data or models.

## 📈 Results Summary
- 89% accuracy achieved on 10,000 test reviews, demonstrating strong generalization capability.
- Balanced performance with F1-scores of 0.89 for both positive and negative classes, indicating no bias.
- Fast inference time - the lightweight Logistic Regression model provides instant predictions.
- Robust preprocessing successfully handles various text formats, special characters and HTML content.
User-friendly deployment via Streamlit enables non-technical users to leverage the ML model.

## 🌐 Deployment
The application is deployed on Streamlit Cloud and can be accessed at:
- **Live App:** https://atharvadhumal-tfidf-logreg-sentiment-analysis-66dulerouq.streamlit.app/
- **Status:** 🟢 Active

#### How to Use:
1. Visit the web app
2. Enter your movie review in the text box
3. Click 'Submit Review'
4. Confirm the review you have submitted and click 'Confirm and Predict.'
5. Get instant prediction (Positive/Negative)

## 🖼️ Screenshots
### Web Application Interface
![screenshots/project_GUI.png]
*Clean and intuitive user interface for sentiment analysis*

## ⚙️ Methodology
### Data Preprocessing Pipeline:
- HTML tag removal using BeautifulSoup
- Text normalization (lowercase conversion, special character removal)
- Tokenization with NLTK
- Stop word elimination
- Word lemmatization for root form extraction

### Feature Engineering:
- TF-IDF vectorization with 7,000 features
- Conversion of text to numerical representations

### Model Training:
- Logistic Regression classifier
- 80-20 train-test split
- Pipeline creation for seamless preprocessing and prediction

### Deployment Architecture:
- Modular design with separate preprocessing functions
- Pickle serialization for model persistence
- Streamlit web interface for user interaction

### 🛠️ Technologies Used
1. Python 3.x - Core programming language
2. Pandas & NumPy - Data manipulation and numerical operations
3. NLTK - Natural language processing tasks (tokenization, lemmatization)
4. BeautifulSoup4 - HTML parsing and cleaning
5. Scikit-learn - Machine learning algorithms and pipeline creation
6. Matplotlib - Data visualization and result analysis
7. Streamlit - Web application framework for deployment
8. Pickle - Model serialization and storage