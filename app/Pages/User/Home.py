import streamlit as st


class UserHomePage():
    def load_ui(self):
        st.title("Hi User!", text_alignment="right", icon=":material/person:")

ui = UserHomePage()
ui.load_ui()