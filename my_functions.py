# -*- coding: utf-8 -*-
#Debug/my_functions
import streamlit as st
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import pandas as pd
import os
import subprocess
import shutil
import time

def kb_to_mb(size):
    size = size / 1024
    return size

def save_file(uploaded_file):
    with open(os.path.join('/mount/src/compressionsequel/work_space/uploaded_dir', uploaded_file.name), "wb") as f:
        f.write(uploaded_file.getbuffer())

def result_data_frame(unique_methods,meanCompressionFactor,meanCompressionTime,meanDecompressionTime):
    result = pd.DataFrame({
        'Method': unique_methods,
        'Compression Factor': meanCompressionFactor,
        'Compression Time (s)': meanCompressionTime,
        'Decompression Time (s)': meanDecompressionTime})
    return result

def Graph_with_dots(data):
    colors_dict = {
        "gzip": "yellow",
        "gzip -v9": "red",
        "gzip -v1": "blue",
        "pigz": "green",
        "bzip2": "purple",
        "pbzip2": "orange",
        "lz4": "pink",
        "lz4 -12": "gray",
        "lzip": "brown",
        "plzip": "olive",
        "plzip -9": "cyan",
        "xz": "magenta",
        "zstd": "teal",
        "zstd -19 -T0": "navy"}
    legend = [mpatches.Patch(color=color, label=label) for label, color in colors_dict.items()]
    colors = [colors_dict[m] for m in data['method']]
    fig = plt.figure(figsize=(12,10))
    plt.xticks(fontsize=14)
    plt.yticks(fontsize=14)
    plt.scatter(data['compressionTime'], data['compressionFactor'], c=colors, s=data['decompressionTime']*50, alpha = 0.5)
    plt.xlabel('Czas kompresji (s)', fontsize=17)
    plt.ylabel('Współczynnik kompresji (%)', fontsize=17)
    plt.title('Wykres czasu kompresji i współczynnika kompresji')
    plt.legend(handles=legend)
    return fig
    
def clear_work_space():
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
    return
    
def compression(metods, decomp_metodes):
    # Data harvesting arrays
    files_list = [] #1
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
    
    percent_complete = int(50/len(metods))
    percent_progress = percent_complete  
    progress_text = "Operation in progress. Please wait."
    my_bar = st.progress(0, text=progress_text)

    
    
    for i, metod in enumerate(metods):
        #copy files from uploaded_dir to data_dir
        
        progress_text = f" {metod} compression in progress. Please wait."
        my_bar.progress(percent_progress, text=progress_text)
        
        files_to_copy = os.listdir(uploaded_dir)
        
        for file_name in files_to_copy:
            source_path = os.path.join(uploaded_dir, file_name)
            destination_path = os.path.join(data_dir, file_name)
            shutil.copy(source_path, destination_path)
            
        for file_name in os.listdir(data_dir):
            path_with_file_name = os.path.join(data_dir, file_name)
            
            files_list.append(file_name) #1
            comp_metode.append(metod) #2
            file_size.append(os.path.getsize(path_with_file_name)) #3
            
            start_time = time.time()    
            if type(metod) == list:
                os.system(f'{metod[0]} {metod[1]} {path_with_file_name}')
            else:
                os.system(f'{metod} {path_with_file_name}')
            end_time = time.time()
            comp_time.append(end_time - start_time) #4
            
            if os.path.isfile(path_with_file_name):
                os.remove(path_with_file_name)
            
        
        #subprocess.run(['mv', f'{data_dir}/*', compressed_dir])
        files_to_move = os.listdir(data_dir)
        for file_name in files_to_move:
            source_path = os.path.join(data_dir, file_name)
            shutil.move(source_path, compressed_dir)
        
        progress_text = f" {metod} decompression in progress. Please wait."    
        percent_progress += percent_complete
        my_bar.progress(percent_progress, text=progress_text) 
        
        
        
        for file_name in os.listdir(compressed_dir):
            path_with_file_name = os.path.join(compressed_dir, file_name)
            
            file_size_after_comp.append(os.path.getsize(path_with_file_name)) #5
                
            start_time = time.time()    
            if type(decomp_metodes[i]) == list:
                os.system(f'{decomp_metodes[i][0]} {decomp_metodes[i][1]} {path_with_file_name}')
            else:
                os.system(f'{decomp_metodes[i]} {path_with_file_name}')
            end_time = time.time()
            decomp_time.append(end_time - start_time) #6
            

            if os.path.isfile(path_with_file_name):
                os.remove(path_with_file_name)
            
        #subprocess.run(['mv', f'{compressed_dir}/*', decompressed_dir])  
        files_to_move = os.listdir(compressed_dir)
        for file_name in files_to_move:
            source_path = os.path.join(compressed_dir, file_name)
            shutil.move(source_path, decompressed_dir)
        
        
        
        for file_name in os.listdir(decompressed_dir):
            file_after = os.path.join(decompressed_dir, file_name)
            file_before = os.path.join(data_dir, file_name)
            
            file_size_after_decomp.append(os.path.getsize(file_after)) #7
            
            result_temp = subprocess.run([f"diff -s {file_after} {file_before} | awk '{{print $6}}'"], shell=True, capture_output=True, text=True)
            result_temp2 = result_temp.stdout.strip()
            check_if_diff.append(result_temp2)  #8
            
            if os.path.isfile(file_after):
                os.remove(file_after)
               
        percent_progress += percent_complete          
         
          
        
        
    data = pd.DataFrame({
        'method': comp_metode,
        'filename': files_list,
        'sizeBefore': file_size,
        'compressionTime': comp_time,
        'compressedFileSize': file_size_after_comp,
        'decompressionTime': decomp_time,
        'sizeAfterDecompression': file_size_after_decomp,
        'different': check_if_diff})
        
    data['compressionFactor'] = 100 - (100 * data['compressedFileSize'] / data['sizeBefore'])
    data.to_csv('/mount/src/compressionsequel/work_space/results_dir/result.csv', index=False)  
    
    my_bar.empty()
    
    return 