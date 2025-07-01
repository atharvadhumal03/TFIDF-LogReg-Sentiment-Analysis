import re
from bs4 import BeautifulSoup
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
import nltk
nltk.download('punkt_tab', quiet=True)
nltk.download('stopwords', quiet=True)
nltk.download('wordnet', quiet=True)

def text_preprocessing(text):

    #parsing html tags
    text = BeautifulSoup(text, 'lxml').get_text()
    
    #lowercasing
    text = text.lower()

    #handling punctuations and special characters
    text = re.sub(r'[^a-zA-Z\s]', '', text)

    #returning preprocessed text
    return text

def tokenize(text):
    
    #tokenization
    tokens = word_tokenize(text)

    #returning tokens
    return tokens

def stop_words_removal(tokens):
    stop_words = stopwords.words("english")
    new_tokens = []
    for word in tokens:
        if word.lower() not in stop_words:
            new_tokens.append(word)
    
    return new_tokens
def lemmatizer(word):
    lemmatizer = WordNetLemmatizer()
    lemmatized = []
    for x in word:
        result = lemmatizer.lemmatize(x)
        lemmatized.append(result)
    return lemmatized

def final_text(tokens):
    return " ".join(tokens)

def full_text_preprocessing(text):

    if isinstance(text, list):
        processed_list = []
        for t in text:
            processed_item = full_text_preprocessing(t)
            processed_list.append(processed_item[0])  #extract the from the returned list as recursion output gives final_doc = [[]].
        return processed_list


    #removing hmtl tags (if present), punctions, special chars and numbers
    text = text_preprocessing(text)
    
    #tokenize
    tokens = tokenize(text)

    #remvoing stop words
    cleaned_tokens = stop_words_removal(tokens)

    #lemmatization
    lemmatized = lemmatizer(cleaned_tokens)

    #joining tokens into a single doc for vectorization
    final_doc = final_text(lemmatized)
    
    return [final_doc]