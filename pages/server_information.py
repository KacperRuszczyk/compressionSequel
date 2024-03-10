import streamlit as st
import os
import subprocess

st.set_page_config(
    page_title='CPU info',
    page_icon='💽',
    initial_sidebar_state='expanded'
)

result_cpu = subprocess.run(['lscpu', '-C', 'cpu'], shell=True, capture_output=True, text=True)

result_disk = subprocess.run(['df', '-h'], shell=True, capture_output=True, text=True)



output_lines_cpu  = result_cpu.stdout.split('\n')
relevant_info = {
    'Model name': output_lines_cpu [13].split(': ')[1],
    'Architecture': output_lines_cpu [0].split(': ')[1],    
    'CPU MHz': '2250',
}

output_lines_disk = result_disk.stdout.split('\n')
relevant_info_disk = {
    'Filesystem': output_lines_disk[1].split()[0],
    'Size': output_lines_disk[1].split()[1],
    'Used': output_lines_disk[1].split()[2],
    'Available': output_lines_disk[1].split()[3],
    'Use%': output_lines_disk[1].split()[4],
    'Mounted on': output_lines_disk[1].split()[5],
}


st.header("CPU Information")
for key, value in relevant_info.items():
    st.write(f"{key}: {value}")
    
st.header("Drive Capacity Information")
for key, value in relevant_info_disk.items():
    st.write(f"{key}: {value}")   
    
