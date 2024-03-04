# -*- coding: utf-8 -*-
#Debug/compressionPlot
import streamlit as st
import pandas as pd
import os

import my_functions


data = 0
unique_methods = 0
metods = []
decomp_metodes = []
meanCompressionFactor = []
meanCompressionTime = []
meanDecompressionTime = []

#streamlit boot PATH creation
if os.path.exists('/mount/src/compressionsequel/work_space') == False:
    os.mkdir('/mount/src/compressionsequel/work_space')
    os.mkdir('/mount/src/compressionsequel/work_space/data_dir')
    os.mkdir('/mount/src/compressionsequel/work_space/compressed_dir')
    os.mkdir('/mount/src/compressionsequel/work_space/decompressed_dir')
    os.mkdir('/mount/src/compressionsequel/work_space/results_dir')
    os.mkdir('/mount/src/compressionsequel/work_space/uploaded_dir')

uploaded_files = st.file_uploader("Upload your files here...", accept_multiple_files=True)


col1, left, col2, right, col3 = st.columns([1,0.1,1,0.1,1])

with col1:
    one_check = st.checkbox('Gzip')
    if one_check:
        metods.append('gzip')  
        decomp_metodes.append('gunzip')
with col2:
    two_check = st.checkbox('Bzip2')
    if two_check:
        metods.append('bzip2')       
        decomp_metodes.append(['bzip2','-d'])
with col3:
    three_check = st.checkbox('Xz')
    if three_check:
        metods.append('xz') 
        decomp_metodes.append('unxz')
        

col1, left, col2, right, col3 = st.columns([1,0.1,1,0.1,1])


with col2:
    comp_button = st.button('compress')
    if comp_button:
        my_functions.clear_work_space()
        if uploaded_files:
            for uploaded_file in uploaded_files:
                my_functions.save_file(uploaded_file)
            my_functions.compression(metods, decomp_metodes)


if os.path.isfile('/mount/src/compressionsequel/work_space/results_dir/result.csv'):      
    data = pd.read_csv('/mount/src/compressionsequel/work_space/results_dir/result.csv')
    unique_methods = list(set(data['method']))
    averageTime = data['compressionTime'].mean()
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
    #st.dataframe(my_functions.result_data_frame(unique_methods,meanCompressionFactor,meanCompressionTime,meanDecompressionTime))
    st.dataframe(data)
if page3:
    st.title('OG Graph ')
    st.pyplot(my_functions.Graph_with_dots(data))
    
if page4:
    st.title('CPU ')
    st.markdown(subprocess.run(['lscpu','-C','cpu'], shell=True, capture_output=True, text=True))
    
    

    





    

col1, left, col2, right, col3 = st.columns([1,0.1,1,0.1,1])


with col2:
    ref_button = st.button('ref')
    if ref_button:       
        pass
        
       



       
PATH = '/mount/src/compressionsequel/work_space/results_dir/result.csv'
if st.button("Download File"):
    st.markdown(f'<a href="{PATH}" download="results.csv">download</a>', unsafe_allow_html=True)