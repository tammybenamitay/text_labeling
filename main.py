from typing import Union

from fastapi import FastAPI
import pickle

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.post("/text_to_label/")
async def create_item(new_text):

    loaded_model = pickle.load(open('pkl/model.pkl' , 'rb'))
    clf = pickle.load(open('pkl/clf.pkl' , 'rb'))
    
    encoded_new_text = loaded_model.encode([new_text])
    predicted_labels = clf.predict(encoded_new_text)

    return predicted_labels[0]