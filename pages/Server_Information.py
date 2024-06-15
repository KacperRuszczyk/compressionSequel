import streamlit as st
import os
import subprocess





st.set_page_config(
    page_title='Server information',
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
    'Size': F"{output_lines_disk[1].split()[1]} KB",
    'Used': F"{output_lines_disk[1].split()[2]} KB",
    'Available': F"{output_lines_disk[1].split()[3]} KB",
    'Use%': output_lines_disk[1].split()[4],
}


st.header("CPU Information",anchor=False)
for key, value in relevant_info.items():
    st.write(f"{key}: {value}")
    
st.header("Drive Capacity Information",anchor=False)
for key, value in relevant_info_disk.items():
    st.write(f"{key}: {value}")   
    
