import streamlit as st
import pickle
import utils_fastapi
import re


encoding_model = pickle.load(open('./pkl/model.pkl' , 'rb'))
regression = pickle.load(open('./pkl/clf.pkl' , 'rb'))

vectorizer = pickle.load(open('./pkl/vectorizer.pkl' , 'rb'))
kmeans = pickle.load(open('./pkl/kmeans.pkl' , 'rb'))
cluster_to_label = pickle.load(open('./pkl/cluster_to_label.pkl', 'rb'))

def predict_by_regression(new_text):
    
    encoded_new_text = encoding_model.encode([new_text])
    predicted_labels = regression.predict(encoded_new_text)
    return predicted_labels[0]

def predict_by_clustering(new_text):
    
    encoded_new_text = vectorizer.transform([new_text])
    predicted_labels = kmeans.predict(encoded_new_text)
    print([new_text])
    print(predicted_labels)
    
    return cluster_to_label.get(predicted_labels[0])


def main():
    st.title("Article labeling - insert your text")

    input_text = st.text_area("Enter text here", "")        
    if st.button("Label me with your text"):

        regression_label = predict_by_regression(input_text)
        st.text("Label by regression:" + regression_label)

        clustering_label = predict_by_clustering(input_text)
        st.text("Label by clustering:" +  ', '.join(map(str, clustering_label)))

    st.title("Article labeling - generate by openai")
    
    selected_label = st.selectbox("Generate you text using openai! chose one of the following subjects:", ["sport", "food", "space"])
    if st.button("Label me with openai generate text"):

        input_text = utils_fastapi.generate_text_with_openai(selected_label)
        
        regression_label = predict_by_regression(input_text)
        st.text("Label by regression:" + regression_label)

        clustering_label = predict_by_clustering(input_text)
        st.text("Label by clustering:" +  ', '.join(map(str, clustering_label)))
        
        st.markdown("The generated text:" + input_text)



if __name__ == "__main__":
    main()



