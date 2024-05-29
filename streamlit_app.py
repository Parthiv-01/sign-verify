import streamlit as st
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error, r2_score
import altair as alt
import time
import zipfile

# Page title
st.set_page_config(page_title='Signature Verify', page_icon='🤖')

st.title("Enter Sign")

input_method = st.radio("Select input method:", ("Upload from Drive", "Take a picture"))

# File uploader widget
if input_method == "Upload from Drive":
    uploaded_image = st.file_uploader("Upload an image", type=["jpg", "jpeg", "png"])
    if uploaded_image is not None:
        st.image(uploaded_image, caption="Uploaded Image", use_column_width=True)

# Camera input widget
elif input_method == "Take a picture":
    captured_image = st.camera_input("Take a picture")
    if captured_image is not None:
        st.image(captured_image, caption="Captured Image", use_column_width=True)
