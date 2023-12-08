import streamlit as st 
import pickle as pkl
import numpy as np

class_list ={'0': 'Male', '1': 'Female','2'}
st.title('Sentiment analysis from Vietnamese names')

#image = Image.open('.png')
#st.image(image)

input_ec = open('ec_vinames.pkl','rb')
encoder = pkl.load(input_ec)

input_md = open('lrc_vinames.pkl','rb')
model = pkl.load(input_md)

st.header('write a name')
txt = st.text_area('','')

if txt != '':
  if st.button('Predict'):
    feature_vector = encoder.transform([txt])
    label = str((model.predict(feature_vector))[0])
    
    st.header('Result')
    st.text(class_list[lable])
    
