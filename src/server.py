from typing import Union

from fastapi import FastAPI
import pickle

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/predict/")
def read_item():

    loaded_model = pickle.load(open('../pkl/model.pkl' , 'rb'))
    clf = pickle.load(open('../pkl/clf.pkl' , 'rb'))
    
    new_text = ["Medicine is a field of constant innovation and discovery, aimed at improving human health and well-being. From the development of life-saving vaccines to breakthroughs in surgical techniques, medical science has come a long way. In recent times, the world has witnessed an unprecedented global effort to combat diseases, with a spotlight on pandemics like COVID-19. Healthcare professionals, including doctors, nurses, and researchers, work tirelessly to provide the best care and find new treatments. Telemedicine has also gained prominence, allowing remote consultations and expanding access to healthcare. As the medical field continues to evolve, it offers hope for healthier lives and a brighter future."]
        
    encoded_new_text = loaded_model.encode(new_text)
    predicted_labels = clf.predict(encoded_new_text)
        
    return {"predict": predicted_labels[0]} 