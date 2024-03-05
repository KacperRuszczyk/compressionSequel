import streamlit as st

st.set_page_config(
    page_title="CPU info",
    page_icon="💽",
)

st.markdown(subprocess.run(['lscpu','-C','cpu'], shell=True, capture_output=True, text=True))