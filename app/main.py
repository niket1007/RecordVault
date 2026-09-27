import streamlit as st
from Common import constants

if(st.session_state.get("is_user_logged_in", False)):
    if st.session_state.get("role") == constants.ADMINROLE:
        pg = st.navigation(
                [
                    st.Page("Pages/Admin/Home.py", title="Home")
                ]
            )
    elif st.session_state.get("role") == constants.USERROLE:
        pg = st.navigation(
            [
                st.Page(
                    "Pages/User/Home.py", title="Home"),
                st.Page(
                    "Pages/User/Policy/Insert.py", title="Policy - Add"),
                st.Page(
                    "Pages/User/Policy/Fetch_Delete_Update.py", title="Policy - Get, Update, Delete")
            ]
        )
else:
    pg = st.navigation(
        [
            st.Page("Pages/Login.py", title="Login")
        ]
    )

pg.run()