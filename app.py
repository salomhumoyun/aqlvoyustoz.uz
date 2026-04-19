import streamlit as st
import google.generativeai as genai

# Sahifa nomi
st.title("AqlVoy Yordamchi")

# API kalitni sozlash
api_key = "AIzaSyAregfoifufu0owMdi05ysRg2IXaaHpEk4"
genai.configure(api_key=api_key)

# Modelni ishga tushirish
model = genai.GenerativeModel('gemini-1.5-flash')

# Chat tarixini saqlash uchun
if "chat" not in st.session_state:
    st.session_state.chat = model.start_chat(history=[])

# Foydalanuvchi kiritadigan joy
user_input = st.text_input("Savolingizni yozing:")

# Javobni qaytarish
if user_input:
    response = st.session_state.chat.send_message(user_input)
    st.write("AqlVoy:", response.text)
