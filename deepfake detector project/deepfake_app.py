#This Streamlit app lets you upload an image and predicts if it's a deepfake or real using a trained model. Upload a JPG or PNG image to see the result instantly.
# python -m streamlit run deepfake_app.py
import streamlit as st
import tensorflow as tf
from tensorflow.keras.preprocessing import image
import numpy as np
from PIL import Image
import time
import datetime

# Load model once at startup
@st.cache_resource
def load_model():
    return tf.keras.models.load_model('D:\codes\my-projects\deepfake detector project\MODELdeepfakedetector.h5')

model = load_model()
# Function to predict image
def predict_image(uploaded_image):
    img_original_size = uploaded_image.size
    img = uploaded_image.resize((128, 128))
    img = np.array(img) / 255.0
    if img.shape[-1] == 4:
        img = img[..., :3]
    img = np.expand_dims(img, axis=0)
    prediction = model.predict(img)[0][0]
    confidence = float(prediction) if prediction >= 0.5 else float(1 - prediction)
    label = "Real" if prediction >= 0.5 else "Fake"
    return label, confidence, img_original_size

st.title("🕵️‍♂️ Deepfake Image Detector")
st.write(
    """
    Upload an image. The model will predict whether it is ***Fake*** or ***Real***,
    and show the technical details of the inference.
    """
)

uploaded_file = st.file_uploader("Upload an image...", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    img = Image.open(uploaded_file).convert("RGB")
    st.image(img, caption='Uploaded Image', use_container_width=True)
    st.write("---")
    st.write("🔎 **Inference Results:**")

    start_time = time.time()
    result, Probability, orig_size = predict_image(img)
    processing_time = time.time() - start_time

    # Dashboard metrics
    col1, col2, col3 = st.columns(3)
    col1.metric("Prediction", result)
    col2.metric("Probability", f"{Probability:.2%}")
    col3.metric("Processing Time", f"{processing_time:.2f} s")