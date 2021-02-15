import streamlit as st
import numpy as np
import os
import cv2

# training_dataset = "training_data_2021-02-15-1"

st.sidebar.title("GTAV dataset")
training_dataset = st.sidebar.input("training_data_2021-02-15-1")

@st.cache(show_spinner=False)
def load_image():
    training_data = np.load("training_data/"+training_dataset+"-balanced.npy",allow_pickle=True)
    return training_data

data = load_image()
id = st.sidebar.slider("Frame",0,len(data)-1,0)
st.sidebar.markdown("## Recorded input:")
st.sidebar.write(data[id][1]) 

st.image(data[id][0],width=600)
