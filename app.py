import streamlit as st
import numpy as np
import pickle

# Load model and encoder
model = pickle.load(open("laptop_model.pkl", "rb"))
le = pickle.load(open("label_encoder.pkl", "rb"))

st.set_page_config(page_title="Laptop Price Prediction", layout="centered")

st.title("💻 Laptop Price Prediction System")
st.write("Predict laptop price based on specifications")

# ---------------- INPUT FIELDS ---------------- #

company = st.selectbox("Company", ["Dell", "HP", "Lenovo", "Apple", "Asus"])
type_name = st.selectbox("Laptop Type", ["Ultrabook", "Notebook", "Gaming"])
inches = st.number_input("Screen Size (Inches)", min_value=10, max_value=20)
screen_res = st.selectbox("Screen Resolution", ["1920x1080", "1366x768"])
cpu = st.selectbox("CPU", ["Intel Core i5", "Intel Core i7", "AMD"])
ram = st.selectbox("RAM (GB)", [4, 8, 16, 32])
memory = st.selectbox("Memory (GB)", [256, 512, 1024])
gpu = st.selectbox("GPU", ["Intel", "Nvidia", "AMD"])
os = st.selectbox("Operating System", ["Windows", "Mac", "Linux"])
weight = st.number_input("Weight (kg)", min_value=1.0, max_value=5.0)

# ---------------- ENCODING ---------------- #

company = le.fit_transform([company])[0]
type_name = le.fit_transform([type_name])[0]
screen_res = le.fit_transform([screen_res])[0]
cpu = le.fit_transform([cpu])[0]
gpu = le.fit_transform([gpu])[0]
os = le.fit_transform([os])[0]

# ---------------- PREDICTION ---------------- #

if st.button("🔍 Predict Price"):
    input_data = np.array([[company, type_name, inches, screen_res,
                            cpu, ram, memory, gpu, os, weight]])

    prediction = model.predict(input_data)

    st.success(f"💰 Estimated Laptop Price: ₹ {int(prediction[0])}")
