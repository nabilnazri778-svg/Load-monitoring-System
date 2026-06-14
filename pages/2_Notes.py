import streamlit as st

st.title("📚 Learning Notes")

topic = st.selectbox(
    "Choose Topic",
    [
        "Beban Mati",
        "Beban Hidup",
        "Daya Tegangan",
        "Daya Mampatan",
        "Faktor Keselamatan"
    ]
)

if topic == "Beban Mati":
    st.header("Beban Mati")
    st.write("""
    Beban mati ialah beban kekal yang berasal
    daripada berat struktur bangunan sendiri.
    """)

elif topic == "Beban Hidup":
    st.header("Beban Hidup")
    st.write("""
    Beban hidup ialah beban yang berubah
    mengikut penggunaan bangunan.
    """)
