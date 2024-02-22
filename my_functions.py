# -*- coding: utf-8 -*-
#Debug/my_functions
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import pandas as pd
import os
import subprocess
import shutil
import time

def save_file(uploaded_file):
    with open(os.path.join('/mount/src/compressionsequel/work_space/uploaded_dir', uploaded_file.name), "wb") as f:
        f.write(uploaded_file.getbuffer())

def loadData(path):
    data = pd.read_csv( path , sep = ',')
    data['compressionFactor'] = 100 - (100 * data['compressedFileSize'] / data['sizeBefore'])
    return data

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


def compression(metods):

    Files_list = [] #1
    comp_metode = [] #2
    file_size = [] #3
    comp_time = [] #4
    
    data_dir = '/mount/src/compressionsequel/work_space/data_dir'
    compressed_dir = '/mount/src/compressionsequel/work_space/compressed_dir'
    decompressed_dir = '/mount/src/compressionsequel/work_space/decompressed_dir'
    results_dir = '/mount/src/compressionsequel/work_space/results_dir'
    uploaded_dir = '/mount/src/compressionsequel/work_space/uploaded_dir'
    
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
            
    return(Files_list)
    
def decompression(metods,decomp_metodes):
    i = 0
    file_size_after_comp = [] #5
    decomp_time = [] #6
    
    data_dir = '/mount/src/compressionsequel/work_space/data_dir'
    compressed_dir = '/mount/src/compressionsequel/work_space/compressed_dir'
    decompressed_dir = '/mount/src/compressionsequel/work_space/decompressed_dir'
    results_dir = '/mount/src/compressionsequel/work_space/results_dir'
    uploaded_dir = '/mount/src/compressionsequel/work_space/uploaded_dir'
    for metod in decomp_metodes:    
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
       
    return(file_size_after_comp)
    
def decompressionCheck(metods):
    file_size_after_decomp = [] #7
    check_if_diff = [] #8
    data_dir = '/mount/src/compressionsequel/work_space/data_dir'
    compressed_dir = '/mount/src/compressionsequel/work_space/compressed_dir'
    decompressed_dir = '/mount/src/compressionsequel/work_space/decompressed_dir'
    results_dir = '/mount/src/compressionsequel/work_space/results_dir'
    uploaded_dir = '/mount/src/compressionsequel/work_space/uploaded_dir'
    for metod in metods:
        for file_name in os.listdir(decompressed_dir):
                file_after = os.path.join(decompressed_dir, file_name)
                file_before = os.path.join(data_dir, file_name)
                
                file_size_after_decomp.append(os.path.getsize(file_after)) #7
                
                result_temp = subprocess.run([f"diff -s {file_after} {file_before} | awk '{{print $6}}'"], shell=True, capture_output=True, text=True)
                result_temp2 = result_temp.stdout.strip()
                check_if_diff.append(result_temp2)  #8
            
    return(file_size_after_decomp)

def moveToCompressedDir():
    data_dir = '/mount/src/compressionsequel/work_space/data_dir'
    compressed_dir = '/mount/src/compressionsequel/work_space/compressed_dir'
    decompressed_dir = '/mount/src/compressionsequel/work_space/decompressed_dir'
    results_dir = '/mount/src/compressionsequel/work_space/results_dir'
    uploaded_dir = '/mount/src/compressionsequel/work_space/uploaded_dir'
    files_to_move = os.listdir(data_dir)
    for file_name in files_to_move:
        source_path = os.path.join(data_dir, file_name)
        shutil.move(source_path, compressed_dir)
        
    return
    
def moveToDecompressedDir():
    
    data_dir = '/mount/src/compressionsequel/work_space/data_dir'
    compressed_dir = '/mount/src/compressionsequel/work_space/compressed_dir'
    decompressed_dir = '/mount/src/compressionsequel/work_space/decompressed_dir'
    results_dir = '/mount/src/compressionsequel/work_space/results_dir'
    uploaded_dir = '/mount/src/compressionsequel/work_space/uploaded_dir'
    files_to_move = os.listdir(compressed_dir)
    for file_name in files_to_move:
        source_path = os.path.join(compressed_dir, file_name)
        shutil.move(source_path, decompressed_dir)
        
    return