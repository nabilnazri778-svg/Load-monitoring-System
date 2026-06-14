from streamlit_autorefresh import st_autorefresh
import streamlit as st
import requests

st.title("📡 Live Force Monitoring")

st_autorefresh(
    interval=3000,
    key="refresh"
)

BLYNK_TOKEN = "XGO8_1zRJ27b6VOPJNuV8NzsPgyymo5S"

try:

    force_url = f"https://blynk.cloud/external/api/get?token={BLYNK_TOKEN}&V0"
    status_url = f"https://blynk.cloud/external/api/get?token={BLYNK_TOKEN}&V1"

    force = requests.get(force_url).text
    status = requests.get(status_url).text

    st.metric(
        "Current Force",
        f"{force} N"
    )

    if status.upper() == "SAFE":

        st.success(
            f"Status: {status}"
        )

    else:

        st.error(
            f"Status: {status}"
        )

except Exception as e:

    st.error(
        f"Connection Error: {e}"
    )

st.caption(
    "Data received from ESP32 through Blynk Cloud"
)