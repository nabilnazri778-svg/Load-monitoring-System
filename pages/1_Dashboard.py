<<<<<<< HEAD
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
=======
import streamlit as st
import random
import pandas as pd

st.title("📊 Dashboard")

force = round(random.uniform(0, 25), 2)

st.metric("Current Force (N)", force)

if force > 20:
    st.error("OVERLOAD")
else:
    st.success("SAFE")

chart_data = pd.DataFrame({
    "Force": [random.uniform(0,25) for _ in range(20)]
})

st.line_chart(chart_data)
>>>>>>> 560a7b9ecbd9845f259431c99c596a61f73df7ac
