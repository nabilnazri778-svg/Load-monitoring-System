import streamlit as st

st.title("📝 Quiz")

answer = st.radio(
    "Apakah beban yang datang daripada berat struktur sendiri?",
    [
        "Beban Mati",
        "Beban Hidup",
        "Beban Angin",
        "Beban Gempa"
    ]
)

if st.button("Submit"):

    if answer == "Beban Mati":
        st.success("Correct!")
    else:
        st.error("Wrong Answer")
