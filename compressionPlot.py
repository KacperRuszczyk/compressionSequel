# -*- coding: utf-8 -*-
import streamlit as st
import pandas as pd



data = pd.read_csv('E:\Py\Data\wyniki1.csv' , sep = ',')

data['CompressionFactor'] = 100 - (100 * data['compressedFileSize'] / data['sizeBefore'])
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
        'Decompression Time (s)': meanDecompressionTime
    })
    return result

st.title('Charts')
col1, left, col2, right, col3 = st.columns([1,0.1,1,0.1,1])

with col1:
    page1 = st.button("Look at a graph")

with col2:
    page2 = st.button("Look at an image")

with col3:
    page3 = st.button("The writing on the wall")

if page1:
    st.bar_chart(pd.DataFrame({'Method': unique_methods, 'Compression Factor': meanCompressionFactor}), x='Method', y='Compression Factor')
    st.bar_chart(pd.DataFrame({'Method': unique_methods, 'Compression Time (s)': meanCompressionTime}), x='Method', y='Compression Time (s)')
    st.bar_chart(pd.DataFrame({'Method': unique_methods, 'Decompression Time (s)': meanDecompressionTime}), x='Method', y='Decompression Time (s)')

if page2:
    st.dataframe(resultDataFrame())

print("testtest")

if page3:
    st.subheader("You won't be able to nest any other widgets after using the button!")
    st.subheader("The memory of a button click lasts only 1 script run")
