# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import pandas as pd

def load_data(PATH):
    data = pd.read_csv( PATH , sep = ',')
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
