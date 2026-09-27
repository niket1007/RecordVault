import streamlit as st


class UserHomePage:
    def load_ui(self):
        st.title("Hi User!", text_alignment="right", icon=":material/person:")

        ip_address = st.context.ip_address
        st.write(
            {
                "IP Address": ip_address,
            }
        )


ui = UserHomePage()
ui.load_ui()
