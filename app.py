import streamlit as st

st.set_page_config(
page_title="IoT Structural Learning & Load Monitoring System",
page_icon="🏗️",
layout="wide"
)

if "role" not in st.session_state:
st.session_state.role = None

st.title("🏗️📚 IoT Structural Learning & Load Monitoring System")

if st.session_state.role is None:

```
st.subheader("Login")

username = st.text_input("Username")
password = st.text_input("Password", type="password")

if st.button("Login"):

    if username == "admin" and password == "admin123":
        st.session_state.role = "admin"
        st.rerun()

    elif username == "student" and password == "student123":
        st.session_state.role = "student"
        st.rerun()

    else:
        st.error("Invalid Username or Password")
```

else:

```
st.success(f"Logged in as: {st.session_state.role}")

if st.button("Logout"):
    st.session_state.role = None
    st.rerun()

st.info("Use the sidebar to navigate through the system.")
```
