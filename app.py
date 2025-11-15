import streamlit as st
from simulasi1 import render_frame

st.set_page_config(page_title="Simulasi Lensa Cembung", layout="wide")
st.title("🔍 Simulasi Lensa Cembung – Versi Web (Streamlit)")

placeholder = st.empty()

while True:
    img = render_frame()
    placeholder.image(img, channels="RGB")
