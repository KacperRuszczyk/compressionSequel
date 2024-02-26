# -*- coding: utf-8 -*-
#Debug/compressionPlot
import streamlit as st
import pandas as pd
import os
import subprocess
import shutil
import time

import my_functions
import compressionScript

#streamlit boot PATH creation
if os.path.exists('/mount/src/compressionsequel/work_space') == False:
    os.mkdir('/mount/src/compressionsequel/work_space')
    os.mkdir('/mount/src/compressionsequel/work_space/data_dir')
    os.mkdir('/mount/src/compressionsequel/work_space/compressed_dir')
    os.mkdir('/mount/src/compressionsequel/work_space/decompressed_dir')
    os.mkdir('/mount/src/compressionsequel/work_space/results_dir')
    os.mkdir('/mount/src/compressionsequel/work_space/uploaded_dir')

uploaded_files = st.file_uploader("Upload your files here...", accept_multiple_files=True)


metods = []
decomp_metodes = []

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
        
st.markdown(f''' :red[methods used:] :gray[{str(metods)}]''')




col1, left, col2, right, col3 = st.columns([1,0.1,1,0.1,1])

with col1:
    clear_button = st.button('clear directorys')
    if clear_button:
        data_dir = '/mount/src/compressionsequel/work_space/data_dir'
        compressed_dir = '/mount/src/compressionsequel/work_space/compressed_dir'
        decompressed_dir = '/mount/src/compressionsequel/work_space/decompressed_dir'
        results_dir = '/mount/src/compressionsequel/work_space/results_dir'
        uploaded_dir = '/mount/src/compressionsequel/work_space/uploaded_dir'
        for file_name in os.listdir(data_dir):
            path_with_file_name = os.path.join(data_dir, file_name)
            os.remove(path_with_file_name)
        for file_name in os.listdir(compressed_dir):
            path_with_file_name = os.path.join(compressed_dir, file_name)
            os.remove(path_with_file_name)
        for file_name in os.listdir(decompressed_dir):
            path_with_file_name = os.path.join(decompressed_dir, file_name)
            os.remove(path_with_file_name)
        for file_name in os.listdir(results_dir):
            path_with_file_name = os.path.join(results_dir, file_name)
            os.remove(path_with_file_name)
        for file_name in os.listdir(uploaded_dir):
            path_with_file_name = os.path.join(uploaded_dir, file_name)
            os.remove(path_with_file_name)

with col2:
    test_button = st.button('test decomp')
    if test_button:
        metod = ['bzip2','-d']
        path_with_file_name = '/mount/src/compressionsequel/work_space/compressed_dir/compressionPlot.py.bz2'
        os.system(f'{metod[0]} {metod[1]} {path_with_file_name}')




with col3:
    conf_button = st.button('upload to data dir')
    if conf_button:       
        if uploaded_files:
            for uploaded_file in uploaded_files:
                my_functions.save_file(uploaded_file)     
            compressionScript.compression(metods, decomp_metodes)
        
st.markdown('uploaded_dir') 
st.markdown(os.listdir('/mount/src/compressionsequel/work_space/uploaded_dir'))             
st.markdown('data_dir')     
st.markdown(os.listdir('/mount/src/compressionsequel/work_space/data_dir'))
st.markdown('compressed_dir') 
st.markdown(os.listdir('/mount/src/compressionsequel/work_space/compressed_dir'))
st.markdown('decompressed_dir') 
st.markdown(os.listdir('/mount/src/compressionsequel/work_space/decompressed_dir'))
st.markdown('results_dir') 
st.markdown(os.listdir('/mount/src/compressionsequel/work_space/results_dir'))

col1, left, col2, right, col3 = st.columns([1,0.1,1,0.1,1])

with col1:
    comp_button = st.button('compress')
    if comp_button:
        my_functions.compression(metods)
        
with col2:
    decomp_button = st.button('decompress')
    if decomp_button:        
        my_functions.decompression(metods,decomp_metodes)
 
with col3:
    check_button = st.button('check')
    if check_button:  
        my_functions.decompressionCheck(metods)
 
col1, left, col2, right, col3 = st.columns([1,0.1,1,0.1,1])

with col1:
    move_button = st.button('move1')
    if move_button:
        my_functions.moveToCompressedDir()
        
with col2:
    move2_button = st.button('move2')
    if move2_button:
        my_functions.moveToDecompressedDir()
        
with col3:
    ref_button = st.button('ref')
    if ref_button:       
        pass
        
        
PATH = '/mount/src/compressionsequel/work_space/results_dir/results.csv'
if st.button("Download File"):
    st.markdown(f'<a href="{PATH}" download="results.csv">download</a>', unsafe_allow_html=True)