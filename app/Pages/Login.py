import streamlit as st
from Common import constants


class LoginPage:
    def __init__(self):
        self.admin_config = st.secrets.get("ADMIN")

    def login_user(self, email_id: str, password: str):
        ip_address = st.context.ip_address
        st.write({
            "IP Address": ip_address,
            "email_id": email_id,
            "password": password
        })

        st.session_state["is_user_logged_in"] = True
        st.session_state["role"] = constants.USERROLE


    def load_ui(self):
        st.title(
            "Welcome to Record Vault",
            text_alignment="right",
            icon=":material/shield_locked:",
        )

        with st.form(
                key="Login", border=False, 
                clear_on_submit=False, enter_to_submit=False):
            
            email_id = st.text_input(
                label="Email Id",
                max_chars=100,
                type="email",
                autocomplete=None,
                icon=":material/alternate_email:")

            password = st.text_input(
                label="Password", type="password", icon=":material/password:")

            submitted = st.form_submit_button(label="Login")

            if submitted:
                if not email_id or not password:
                    st.error("Fill all the required fields")
                else:                    
                    if (email_id == self.admin_config.get("EMAIL", "") and 
                    password == self.admin_config.get("PASSWORD", "")):
                        st.session_state["is_user_logged_in"] = True
                        st.session_state["role"] = constants.ADMINROLE
                    else:
                        self.login_user(email_id, password)
        
                    st.rerun()



ui = LoginPage()
ui.load_ui()
