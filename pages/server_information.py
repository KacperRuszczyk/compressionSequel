import streamlit as st
import os
import subprocess

st.set_page_config(
    page_title="CPU info",
    page_icon="💽",
    initial_sidebar_state='expanded'
)

result = subprocess.run(['lscpu', '-C', 'cpu'], shell=True, capture_output=True, text=True)

output_lines = result.stdout.split('\n')
relevant_info = {
    "Architecture": output_lines[0].split(': ')[1],
    "CPU(s)": output_lines[5].split(': ')[1],
    "Model name": output_lines[13].split(': ')[1],
    "CPU MHz": output_lines[14].split(': ')[1],
}

for key, value in relevant_info.items():
    st.write(f"{key}: {value}")