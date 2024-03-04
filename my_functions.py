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