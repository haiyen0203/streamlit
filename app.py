import streamlit as st
import pickle
import requests
from io import BytesIO

# Link trực tiếp đến raw file model.pkl trên GitHub
github_model_url = "https://raw.githubusercontent.com/haiyen0203/streamlit/main/hy.pkl"

# Tải mô hình từ GitHub
response = requests.get(github_model_url)

if response.status_code == 200:
    # Đọc mô hình từ dữ liệu nhận được
    model = pickle.load(BytesIO(response.content))

    st.title('Sentiment analysis')

    message = st.text_input('Enter a message')
    submit = st.button("Predict")

    if submit:
        prediction = model.predict([message])
        st.write(prediction)
else:
    st.error(f"Failed to download the model. Please check the GitHub URL: {github_model_url}")
