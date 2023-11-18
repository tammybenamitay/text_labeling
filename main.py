from typing import Union

from fastapi import FastAPI
import pickle
import utils_fastapi

app = FastAPI()

encoding_model = pickle.load(open('./pkl/model.pkl' , 'rb'))
regression = pickle.load(open('./pkl/clf.pkl' , 'rb'))

vectorizer = pickle.load(open('./pkl/vectorizer.pkl' , 'rb'))
kmeans = pickle.load(open('./pkl/kmeans.pkl' , 'rb'))
cluster_to_label = pickle.load(open('./pkl/cluster_to_label.pkl', 'rb'))

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.post("/text_to_label/")
async def create_item(new_text):

    return predict_by_regression(new_text),  predict_by_clustering(new_text)

@app.post("/generate_with_openai/")
async def create_item(subject):

    new_text = utils_fastapi.generate_text_with_openai(subject)
    return predict_by_regression(new_text),  predict_by_clustering(new_text), new_text

def predict_by_regression(new_text):
    
    encoded_new_text = encoding_model.encode([new_text])
    predicted_labels = regression.predict(encoded_new_text)
    return "label by regression : "+ predicted_labels[0]

def predict_by_clustering(new_text):
    
    encoded_new_text = vectorizer.transform([new_text])
    predicted_labels = kmeans.predict(encoded_new_text)
    print([new_text])
    print(predicted_labels)
    
    return "label by clustering : "+cluster_to_label.get(predicted_labels[0])