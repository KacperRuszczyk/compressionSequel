# -*- coding: utf-8 -*-
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches


path = 'E:\Py\Data\wyniki1.csv'

def loadData(path):
    data = pd.read_csv( path , sep = ',')
    data['CompressionFactor'] = 100 - (100 * data['compressedFileSize'] / data['sizeBefore'])
    return data

data = loadData(path)

averageTime = data['compressionTime'].mean()
unique_methods = list(set(data['method']))

meanCompressionFactor = []
meanCompressionTime = []
meanDecompressionTime = []

for method in unique_methods:
    mask = data['method'] == method
    meanCompressionFactor.append(data['CompressionFactor'][mask].mean())
    meanCompressionTime.append(data['compressionTime'][mask].mean())
    meanDecompressionTime.append(data['decompressionTime'][mask].mean())

def resultDataFrame():
    result = pd.DataFrame({
        'Method': unique_methods,
        'Compression Factor': meanCompressionFactor,
        'Compression Time (s)': meanCompressionTime,
        'Decompression Time (s)': meanDecompressionTime})
    return result

def secGraph(data):
    
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
    plt.scatter(data['compressionTime'], data['CompressionFactor'], c=colors, s=data['decompressionTime']*50, alpha = 0.5)
    plt.xlabel('Czas kompresji (s)', fontsize=17)
    plt.ylabel('Współczynnik kompresji (%)', fontsize=17)
    plt.title('Wykres czasu kompresji i współczynnika kompresji')
    plt.legend(handles=legend)
    return fig


col1, left, col2, right, col3 = st.columns([1,0.1,1,0.1,1])

with col1:
    page1 = st.button("Look at a graphs")

with col2:
    page2 = st.button("Look at the data")

with col3:
    page3 = st.button("Look at this graph")

if page1:
    st.title('Graphs')
    st.bar_chart(pd.DataFrame({'Method': unique_methods, 'Compression Factor': meanCompressionFactor}), x='Method', y='Compression Factor')
    st.bar_chart(pd.DataFrame({'Method': unique_methods, 'Compression Time (s)': meanCompressionTime}), x='Method', y='Compression Time (s)')
    st.bar_chart(pd.DataFrame({'Method': unique_methods, 'Decompression Time (s)': meanDecompressionTime}), x='Method', y='Decompression Time (s)')

if page2:
    st.title('Data Frame')
    st.dataframe(resultDataFrame())

if page3:
    st.title('OG Graph ')
    st.pyplot(secGraph(data))