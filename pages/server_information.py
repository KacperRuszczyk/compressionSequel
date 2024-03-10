import streamlit as st
import os
import subprocess

st.set_page_config(
    page_title='CPU info',
    page_icon='💽',
    initial_sidebar_state='expanded'
)

result_cpu = subprocess.run(['lscpu', '-C', 'cpu'], shell=True, capture_output=True, text=True)

result_memory = subprocess.run(['free', '-h'], shell=True, capture_output=True, text=True)

result_disk = subprocess.run(['df', '-h'], shell=True, capture_output=True, text=True)



output_lines_cpu  = result_cpu.stdout.split('\n')
relevant_info = {
    'Architecture': output_lines_cpu [0].split(': ')[1],
    'CPU(s)': output_lines_cpu [5].split(': ')[1],
    'Model name': output_lines_cpu [13].split(': ')[1],
    'CPU MHz': '2250',
}





for key, value in relevant_info.items():
    st.write(f"{key}: {value}")
    
    
    
st.markdown(result_memory)
st.markdown(result_disk)