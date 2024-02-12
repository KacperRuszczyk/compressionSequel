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
    
    
PATH = '/mount/src/compressionsequel/work_space/results_dir/results.csv'
if st.button("Download File"):
    st.markdown(f'<a href="{PATH}" download="results.csv">download</a>', unsafe_allow_html=True)
uploaded_files = st.file_uploader("Upload your files here...", accept_multiple_files=True)
st.markdown(os.listdir('/mount/src/compressionsequel/work_space'))
st.markdown(os.listdir('/mount/src/compressionsequel/work_space/data_dir'))
st.markdown(os.listdir('/mount/src/compressionsequel/work_space/compressed_dir'))
st.markdown(os.listdir('/mount/src/compressionsequel/work_space/decompressed_dir'))
st.markdown(os.listdir('/mount/src/compressionsequel/work_space/results_dir'))
#subprocess.run(['rm', '/mount/src/compressionsequel/work_space/results_dir/results.csv'])
#st.markdown(os.listdir('/mount/src/compressionsequel/work_space/results_dir'))
st.markdown(os.listdir('/mount/src/compressionsequel/work_space/uploaded_dir'))




if uploaded_files:
    for uploaded_file in uploaded_files:
        my_functions.save_file(uploaded_file)





    col1, left, col2, right, col3 = st.columns([1,0.1,1,0.1,1])

    metods = []
    decomp_metodes = []
    button_check = True

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
    
    
    if os.path.exists('/mount/src/compressionsequel/work_space/results_dir/results.csv'):
    
        data = my_functions.loadData('/mount/src/compressionsequel/work_space/results_dir/results.csv')
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
            
            
   
        
    
    else:
        st.warning("Processing data...")
else:
    st.warning("Please upload one or more files to proceed.")  


    
        
#st.markdown(os.getcwd())

#st.markdown('gzip, bzip2, xz, help')



#st.markdown(os.path.getsize('/mount/src/compressionsequel/work_space/results_dir/results.csv'))
#subprocess.run(['bzip2', '/mount/src/compressionsequel/work_space/results_dir/results.csv'])
#st.markdown(os.listdir('/mount/src/compressionsequel/work_space/results_dir'))
#st.markdown(os.path.getsize('/mount/src/compressionsequel/work_space/results_dir/results.csv.bz2'))


#st.markdown(os.path.exists( '/mount/src/compressionsequel/compressionPlot.py'))
#X = '/mount/src/compressionsequel/compressionPlot.py'

#result_temp=subprocess.run([f"ls -l {X} | awk '{{print $5}}'"], shell=True, capture_output=True, text=True)
#st.markdown(result_temp)

#file_size = result_temp.stdout.strip()

#st.markdown(file_size)

#st.markdown(os.listdir('/mount/src/compressionsequel/work_space/compressed_dir'))
#subprocess.run(['bzip2', '/mount/src/compressionsequel/work_space/compressed_dir/compressionPlot.py'])
##subprocess.run(['rm', '/mount/src/compressionsequel/work_space/compressed_dir/compressionPlot.py'])
#st.markdown(os.listdir('/mount/src/compressionsequel/work_space/compressed_dir'))
#st.markdown(os.path.isfile('/mount/src/compressionsequel/work_space/compressed_dir/compressionPlot.py.bz2'))
#st.markdown(subprocess.run(['bzip2','-d', '/mount/src/compressionsequel/work_space/compressed_dir/compressionPlot.py.bz2'], capture_output=True, text=True))
#st.markdown(os.listdir('/mount/src/compressionsequel/work_space/compressed_dir'))
