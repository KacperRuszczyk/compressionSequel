# -*- coding: utf-8 -*-
import streamlit as st
import pandas as pd
import os
import subprocess

import my_functions

#streamlit boot PATH creation
if os.path.exists('/mount/src/compressionsequel/work_space') == False:
    os.mkdir('/mount/src/compressionsequel/work_space')
    os.mkdir('/mount/src/compressionsequel/work_space/data_dir')
    os.mkdir('/mount/src/compressionsequel/work_space/compressed_dir')
    os.mkdir('/mount/src/compressionsequel/work_space/decompressed_dir')
    os.mkdir('/mount/src/compressionsequel/work_space/results_dir')
    
    

uploaded_file = st.file_uploader("Upload your file here...", type=['csv'])

PATH = 'E:\Py\Data\wyniki1.csv'

col1, left, col2, right, col3 = st.columns([1,0.1,1,0.1,1])

metods = []
decopm_metodes = []


with col1:
    one_check = st.checkbox('Gzip')
    if one_check:
        metods.append('gzip')  
        decopm_metodes.append('gunzip')
with col2:
    two_check = st.checkbox('Bzip2')
    if two_check:
        metods.append('bzip2')       
        decopm_metodes.append(['bzip2','-d'])
with col3:
    three_check = st.checkbox('Xz')
    if three_check:
        metods.append('xz') 
        decopm_metodes.append('unxz')
with col1:
    four_check = st.checkbox('Gzip 2')
    if four_check:
        metods.append('Gzip 2')        
with col2:
    five_check = st.checkbox('L4 2')
    if five_check:
        metods.append('L4 2')        
with col3:
    six_check = st.checkbox('Xz 2')
    if six_check:
        metods.append('Xz 2')        



st.markdown(f''' :red[methods used:] :gray[{str(metods)}]''')

data = my_functions.loadData(uploaded_file)
averageTime = data['compressionTime'].mean()
unique_methods = list(set(data['method']))

meanCompressionFactor = []
meanCompressionTime = []
meanDecompressionTime = []

for method in unique_methods:
    mask = data['method'] == method
    meanCompressionFactor.append(data['compressionFactor'][mask].mean())
    meanCompressionTime.append(data['compressionTime'][mask].mean())
    meanDecompressionTime.append(data['decompressionTime'][mask].mean())




col1, left, col2, center, col3, right, col4 = st.columns([1, 0.1, 1, 0.1, 1, 0.1, 1])

with col1:
    page1 = st.button("Graphs")

with col2:
    page2 = st.button("Data")

with col3:
    page3 = st.button("One graph")
    
with col4:
    page4 = st.button("CPU inf")

if page1:
    st.title('Graphs')
    st.bar_chart(pd.DataFrame({'Method': unique_methods, 'Compression Factor': meanCompressionFactor}), x='Method', y='Compression Factor')
    st.bar_chart(pd.DataFrame({'Method': unique_methods, 'Compression Time (s)': meanCompressionTime}), x='Method', y='Compression Time (s)')
    st.bar_chart(pd.DataFrame({'Method': unique_methods, 'Decompression Time (s)': meanDecompressionTime}), x='Method', y='Decompression Time (s)')

if page2:
    st.title('Data Frame')
    st.dataframe(my_functions.result_data_frame(unique_methods,meanCompressionFactor,meanCompressionTime,meanDecompressionTime))

if page3:
    st.title('OG Graph ')
    st.pyplot(my_functions.Graph_with_dots(data))
    
if page4:
    st.title('CPU ')
    st.markdown(subprocess.run(['lscpu','-C','cpu'], shell=True, capture_output=True, text=True))
    
    
st.markdown(os.getcwd())

st.markdown('gzip, bzip2, xz, help')

st.markdown(os.listdir('/mount/src/compressionsequel/work_space'))

#st.markdown(os.path.getsize('/mount/src/compressionsequel/work_space/results_dir/results.csv'))
#subprocess.run(['bzip2', '/mount/src/compressionsequel/work_space/results_dir/results.csv'])
#st.markdown(os.listdir('/mount/src/compressionsequel/work_space/results_dir'))
#st.markdown(os.path.getsize('/mount/src/compressionsequel/work_space/results_dir/results.csv.bz2'))


st.markdown(os.path.exists( '/mount/src/compressionsequel/compressionPlot.py'))
X = '/mount/src/compressionsequel/compressionPlot.py'

result_temp=subprocess.run([f"ls -l {X} | awk '{{print $5}}'"], shell=True, capture_output=True, text=True)
st.markdown(result_temp)

file_size = result_temp.stdout.strip()

st.markdown(file_size)

#st.markdown(os.listdir('/mount/src/compressionsequel/work_space/compressed_dir'))
#subprocess.run(['bzip2', '/mount/src/compressionsequel/work_space/compressed_dir/compressionPlot.py'])
##subprocess.run(['rm', '/mount/src/compressionsequel/work_space/compressed_dir/compressionPlot.py'])
st.markdown(os.listdir('/mount/src/compressionsequel/work_space/compressed_dir'))

st.markdown(os.path.isfile('/mount/src/compressionsequel/work_space/compressed_dir/compressionPlot.py.bz2'))

st.markdown(subprocess.run(['bzip2','-d', '/mount/src/compressionsequel/work_space/compressed_dir/compressionPlot.py.bz2'], capture_output=True, text=True))

st.markdown(os.listdir('/mount/src/compressionsequel/work_space/compressed_dir'))