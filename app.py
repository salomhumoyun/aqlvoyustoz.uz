st.title("AqlVoy Yordamchi")

# API kalitingiz
api_key = "AIzaSyAregfoifufu0owMdi05ysRg2IXaaHpEk4" 

genai.configure(api_key=api_key)

# Modelni sozlash
model = genai.GenerativeModel('gemini-1.5-flash')

# Chat tarixini saqlash uchun
if "chat" not in st.session_state:
    st.session_state.chat = model.start_chat(history=[])

# Foydalanuvchi inputi
user_input = st.text_input("Savolingizni yozing:")

if st.button("Yuborish"):
    if user_input:
        try:
            # Chat tarixiga savolni yuborish
            response = st.session_state.chat.send_message(user_input)
            st.write("AqlVoy:", response.text)
        except Exception as e:
            st.error(f"Xatolik yuz berdi: {e}")
