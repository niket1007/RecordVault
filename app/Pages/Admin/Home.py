import streamlit as st
from Common import constants
from Database.mongodb import MongoDB
from Database.models import UserRegRecords

class AdminHomePage:
    def __init__(self):
        self.is_user_logged_in = (
            st.session_state["is_user_logged_in"]
            and st.session_state["role"] == constants.ADMINROLE
        )
        self.mongodb = MongoDB()

    def load_ui(self):
        if not self.is_user_logged_in:
            st.error("User not logged in")
            st.stop()

        with st.form(
            key="admin_register_user",
            clear_on_submit=False,
            border=True,
            enter_to_submit=False,
        ):
            st.subheader("Register User", divider=True, text_alignment="right")

            email_id = st.text_input(
                label="Email Id",
                max_chars=100,
                type="email",
                icon=":material/alternate_email:",
            )

            password = st.text_input(
                label="Password",
                type="password",
                icon=":material/password:",
            )

            submitted = st.form_submit_button("Register")

            if submitted:
                if not email_id or not password:
                    st.error("Fill all the required fields")
                else:
                    try:
                        self.mongodb.register_user(
                            UserRegRecords(email_id=email_id, password=password))
                        st.success("Registered user successfuly", icon=":material/check:")
                    except Exception as e:
                        st.error(str(e))


ui = AdminHomePage()
ui.load_ui()
