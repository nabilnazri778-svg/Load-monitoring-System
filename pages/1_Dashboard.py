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
