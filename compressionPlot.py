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

methods_used = []

with col1:
    one_check = st.checkbox('Gzipp')
    if one_check:
        methods_used.append('Gzipp')        
with col2:
    two_check = st.checkbox('L4')
    if two_check:
        methods_used.append('L4')        
with col3:
    three_check = st.checkbox('Xz')
    if three_check:
        methods_used.append('Xz') 
with col1:
    four_check = st.checkbox('Gzip 2')
    if four_check:
        methods_used.append('Gzip 2')        
with col2:
    five_check = st.checkbox('L4 2')
    if five_check:
        methods_used.append('L4 2')        
with col3:
    six_check = st.checkbox('Xz 2')
    if six_check:
        methods_used.append('Xz 2')        



st.markdown(f''' :red[methods used:] :gray[{str(methods_used)}]''')

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




col1, left, col2, right, col3 = st.columns([1,0.1,1,0.1,1])

with col1:
    page1 = st.button("Graphs")

with col2:
    page2 = st.button("Data")

with col3:
    page3 = st.button("One graph")

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
    
    
st.markdown(os.getcwd())

st.markdown('gzip, bzip2, xz, help')

st.markdown(os.listdir('/mount/src/compressionsequel/work_space'))

#st.markdown(os.path.getsize('/mount/src/compressionsequel/work_space/results_dir/results.csv'))
#subprocess.run(['bzip2', '/mount/src/compressionsequel/work_space/results_dir/results.csv'])
#st.markdown(os.listdir('/mount/src/compressionsequel/work_space/results_dir'))
#st.markdown(os.path.getsize('/mount/src/compressionsequel/work_space/results_dir/results.csv.bz2'))


st.markdown(os.path.exists( '/mount/src/compressionsequel/compressionPlot.py'))
X = '/mount/src/compressionsequel/compressionPlot.py'
st.markdown(subprocess.run(['ls', '-l', X]))
