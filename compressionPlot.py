# -*- coding: utf-8 -*-
#compressionPlot
import streamlit as st
import pandas as pd
import os
import subprocess

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
if uploaded_files:
    for uploaded_file in uploaded_files:
        my_functions.save_file(uploaded_file)
       
    col1, left, col2, right, col3 = st.columns([1,0.1,1,0.1,1])

    metods = []
    decomp_metodes = []
   

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
    
    with col2:
        compress_button = st.button('Compress The Files')
        if compress_button:    
            compressionScript.compression(metods, decomp_metodes)
            st.markdown(os.listdir('/mount/src/compressionsequel/work_space'))
            st.markdown(os.listdir('/mount/src/compressionsequel/work_space/data_dir'))
            st.markdown(os.listdir('/mount/src/compressionsequel/work_space/compressed_dir'))
            st.markdown(os.listdir('/mount/src/compressionsequel/work_space/decompressed_dir'))
            st.markdown(os.listdir('/mount/src/compressionsequel/work_space/results_dir'))
            st.markdown(os.listdir('/mount/src/compressionsequel/work_space/uploaded_dir'))
            st.markdown(Files)
            