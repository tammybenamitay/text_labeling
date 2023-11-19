import os
import pickle
import openai
import config
import nltk
import utils
import numpy as np
import pandas as pd
from sentence_transformers import SentenceTransformer
from nltk.corpus import stopwords
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

stop_words = stopwords.words('english')
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report
#from gensim.summarization import summarize

prt = nltk.stem.PorterStemmer()
nltk.download('punkt')
#os.system('python -m pip install requirements.txt')

def printaa():
    print("This is a test function in utils.py")

def preprocess(document_path):
    with open(document_path, 'r', encoding='utf-8') as file:
        document = file.read()
        return document
        # tokens = nltk.word_tokenize(document)
        # tokens_pun_lower = [i.lower() for i in tokens if i.isalnum()]
        # tokens_stop = [i for i in tokens_pun_lower if i not in stop_words]
        # terms = [prt.stem(i) for i in tokens_stop]
        #return " ".join(terms)
    
def load_data(data_folder_path, word_count_num):
    data_list = []
    #summarize_data = []
    folder_names = []

    for folder_name in os.listdir(data_folder_path):
        folder_path = os.path.join(data_folder_path, folder_name)
        if os.path.isdir(folder_path):
            folder_names.extend([folder_name] * len(os.listdir(folder_path)))  
            for file_name in os.listdir(folder_path):
                file_path = folder_path+'/'+file_name
                file_data = preprocess(file_path)
                data_list.append(file_data)
                #summarize_data.append(summarize(file_data, word_count=word_count_num))

    df = pd.DataFrame({'label': folder_names, 'text': data_list})
    return df

def create_model_LogisticRegression(encoded_texts,max_iter_num , dfLabels, test_size_num):

    X_train, X_test, y_train, y_test = train_test_split(encoded_texts, dfLabels, test_size=test_size_num, random_state=42)

    clf = LogisticRegression(max_iter=max_iter_num)
    clf.fit(X_train, y_train)

    y_pred = clf.predict(X_test)
    accuracy = accuracy_score(y_test, y_pred)
    # report = classification_report(y_test, y_pred)

    # print(f"Accuracy: {accuracy}")
    # print("Classification Report:")
    # print(report)
    return (clf, y_pred) 


def generate_text_with_openai(subjectName):

    api_key = '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'

    request = 'generate an 150 words article on any random {subject} category'.format(subject=subjectName)

    # Configure GPT-3 parameters
    response = openai.Completion.create(
        engine="text-davinci-003",  # You can choose other engines like 'text-davinci-003'
        prompt=request,
        max_tokens=150,  # Adjust the desired length of the generated text
        api_key=api_key
    )

    # Extract the generated text from the response
    #print(response.choices)
    generated_text = response.choices[0].text
    return generated_text