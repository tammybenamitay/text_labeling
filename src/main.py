from typing import Union

from fastapi import FastAPI
import pickle
import utils

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.post("/text_to_label/")
async def create_item(new_text):

    loaded_model = pickle.load(open('../pkl/model.pkl' , 'rb'))
    clf = pickle.load(open('../pkl/clf.pkl' , 'rb'))
    
    encoded_new_text = loaded_model.encode([new_text])
    predicted_labels = clf.predict(encoded_new_text)

    return predicted_labels[0]

@app.post("/generate_with_openai/")
async def create_item(subject):

    new_text = utils.generate_text_with_openai(subject)

    loaded_model = pickle.load(open('../pkl/model.pkl' , 'rb'))
    clf = pickle.load(open('../pkl/clf.pkl' , 'rb'))
    
    encoded_new_text = loaded_model.encode([new_text])
    predicted_labels = clf.predict(encoded_new_text)

    return new_text, predicted_labels[0]