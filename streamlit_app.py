import streamlit as st
import numpy as np
import cv2
from PIL import Image
import tensorflow as tf

st.title("Signature Verification")

# Option to upload an image or take a picture
input_method = st.radio("Select input method:", ("Upload from Drive", "Take a picture"))

if input_method == "Upload from Drive":
    uploaded_image = st.file_uploader("Upload an image", type=["jpg", "jpeg", "png"])
    if uploaded_image is not None:
        uploaded_image = Image.open(uploaded_image)
        st.image(uploaded_image, caption="Uploaded Image", use_column_width=True)
        uploaded_image = np.array(uploaded_image)
else:
    captured_image = st.camera_input("Take a picture")
    if captured_image is not None:
        captured_image = Image.open(captured_image)
        st.image(captured_image, caption="Captured Image", use_column_width=True)
        uploaded_image = np.array(captured_image)

# Load the saved signature image (assume it's stored as saved_signature.png)
saved_signature = cv2.imread('saved_signature.png')
saved_signature = cv2.cvtColor(saved_signature, cv2.COLOR_BGR2RGB) # Convert to RGB

if uploaded_image is not None:
    # Verify the signature
    similarity_score = verify_signature(uploaded_image, saved_signature)
    st.write(f"Similarity Score: {similarity_score:.2f}")
    
    # Determine if the signatures match (assume a threshold of 0.5 for similarity)
    if similarity_score > 0.5:
        st.success("The signatures match!")
    else:
        st.error("The signatures do not match.")
