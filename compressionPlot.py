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


with col3:
    conf_button = st.button('upload to data dir')
    if conf_button:       
        if uploaded_files:
            for uploaded_file in uploaded_files:
                my_functions.save_file(uploaded_file)       
        
        
        
st.markdown('data_dir')     
st.markdown(os.listdir('/mount/src/compressionsequel/work_space/data_dir'))
st.markdown('compressed_dir') 
st.markdown(os.listdir('/mount/src/compressionsequel/work_space/compressed_dir'))
st.markdown('decompressed_dir') 
st.markdown(os.listdir('/mount/src/compressionsequel/work_space/decompressed_dir'))
st.markdown('data_dir') 
st.markdown(os.listdir('/mount/src/compressionsequel/work_space/uploaded_dir'))
st.markdown('uploaded_dir') 
st.markdown(os.listdir('/mount/src/compressionsequel/work_space/results_dir'))

col1, left, col2, right, col3 = st.columns([1,0.1,1,0.1,1])

with col1:
    comp_button = st.button('compress')
    if comp_button:
        my_functions.compression(metods)
        
with col2:
    decomp_button = st.button('decompress')
    if decomp_button:        
        my_functions.decompression(decomp_metodes)
 
with col3:
    check_button = st.button('check')
    if check_button:  
        my_functions.decompressionCheck(metods)
 
col1, left, col2, right, col3 = st.columns([1,0.1,1,0.1,1])

with col1:
    move_button = st.button('move1')
    if move_button:
        moveToCompressedDir()
        
with col2:
    move2_button = st.button('move2')
    if move2_button:
        moveToDecompressedDir()
        
with col3:
    ref_button = st.button('ref')
    if ref_button:       
        pass
        
        
def compression(metods, decomp_metodes):
    # Data harvesting arrays
    Files_list = [] #1
    comp_metode = [] #2
    file_size = [] #3
    comp_time = [] #4
    file_size_after_comp = [] #5
    decomp_time = [] #6
    file_size_after_decomp = [] #7
    check_if_diff = [] #8


    # Paths
    data_dir = '/mount/src/compressionsequel/work_space/data_dir'
    compressed_dir = '/mount/src/compressionsequel/work_space/compressed_dir'
    decompressed_dir = '/mount/src/compressionsequel/work_space/decompressed_dir'
    results_dir = '/mount/src/compressionsequel/work_space/results_dir'
    uploaded_dir = '/mount/src/compressionsequel/work_space/uploaded_dir'
    i = 0



    for metod in metods:
        #copy files from uploaded_dir to data_dir
        files_to_copy = os.listdir(uploaded_dir)
        for file_name in files_to_copy:
            source_path = os.path.join(uploaded_dir, file_name)
            destination_path = os.path.join(data_dir, file_name)
            shutil.copy(source_path, destination_path)
            
        for file_name in os.listdir(data_dir):
            path_with_file_name = os.path.join(data_dir, file_name)
            
            Files_list.append(file_name) #1
            comp_metode.append(metod) #2
            file_size.append(os.path.getsize(path_with_file_name)) #3
            
            start_time = time.time()    
            subprocess.run([metod, path_with_file_name])
            end_time = time.time()
            comp_time.append(end_time - start_time) #4
            if os.path.isfile(path_with_file_name):
                os.remove(path_with_file_name)
            
        
        #subprocess.run(['mv', f'{data_dir}/*', compressed_dir])
        files_to_move = os.listdir(data_dir)
        for file_name in files_to_move:
            source_path = os.path.join(data_dir, file_name)
            shutil.move(source_path, compressed_dir)
        
        for file_name in os.listdir(compressed_dir):
            path_with_file_name = os.path.join(compressed_dir, file_name)
            
            file_size_after_comp.append(os.path.getsize(path_with_file_name)) #5
                
            #start_time = time.time()    
            #if decomp_metodes == list:
                #subprocess.run([decomp_metodes[i][0],decomp_metodes[i][1], path_with_file_name], shell=True)
            #else:
                #subprocess.run([decomp_metodes[i], path_with_file_name], shell=True)
            #end_time = time.time()
            #decomp_time.append(end_time - start_time) #6
            

            #if os.path.isfile(path_with_file_name):
                #os.remove(path_with_file_name)
            
        #subprocess.run(['mv', f'{compressed_dir}/*', decompressed_dir])  
        files_to_move = os.listdir(compressed_dir)
        for file_name in files_to_move:
            source_path = os.path.join(compressed_dir, file_name)
            shutil.move(source_path, decompressed_dir)
        i += 1
        
        for file_name in os.listdir(decompressed_dir):
            file_after = os.path.join(decompressed_dir, file_name)
            file_before = os.path.join(data_dir, file_name)
            
            file_size_after_decomp.append(os.path.getsize(file_after)) #7
            
            #result_temp = subprocess.run([f"diff -s {file_after} {file_before} | awk '{{print $6}}'"], shell=True, capture_output=True, text=True)
            #result_temp2 = result_temp.stdout.strip()
            #check_if_diff.append(result_temp2)  #8

    return(Files_list)





    