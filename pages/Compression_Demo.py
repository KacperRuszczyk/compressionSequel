import streamlit as st
import pandas as pd
import os

from Classes.Master import Master
from Classes.FileManager import FileManager
from Classes.PathManager import PathManager
from Classes.DataHolder import DataHolder
from Classes.Grapher import Grapher


st.set_page_config(
    page_title="Compression Demo",
    page_icon="📊",
    initial_sidebar_state='expanded'
)
file_manager = FileManager()
data_holder = DataHolder()
path_manager = PathManager()
grapher = Grapher()
master = Master()
methods = []
decomp_methods = []

st.title(':orange[Compression Demo]', anchor=False)
st.markdown(
    "*1. Upload some files (I would recommend uploading one file extension type, but I'm not going to tell you how to live your life).*")
st.markdown("*2. Choose the compression options that you would like to test.*")
st.markdown(
    '*3. Click the "compress ..." button. (FYI, that buttons also clears the results data from previous attempt.)*')
st.markdown('*4. Wait until the process is done and view the results.*')
st.divider()

col1, left, col2 = st.columns([1, 0.1, 1])

with col1:
    uploaded_files = st.file_uploader("Upload your files here...", accept_multiple_files=True)
with col2:
    fake_files_check = st.checkbox('Use Sample Files')
    if fake_files_check:
        Fake_Files = True
    else:
        Fake_Files = False

col1, left, col2, right, col3 = st.columns([1, 0.1, 1, 0.1, 1])
# Regular
with col1:
    one_check = st.checkbox('Gzip')
    if one_check:
        methods.append('gzip')
        decomp_methods.append('gunzip')
with col2:
    two_check = st.checkbox('Bzip2')
    if two_check:
        methods.append('bzip2')
        decomp_methods.append('bzip2 -d')
with col3:
    three_check = st.checkbox('Xz')
    if three_check:
        methods.append('xz')
        decomp_methods.append('unxz')
# Best
with col1:
    one_check = st.checkbox('Gzip Best')
    if one_check:
        methods.append('gzip --best')
        decomp_methods.append('gunzip')
with col2:
    two_check = st.checkbox('Bzip2 Best')
    if two_check:
        methods.append('bzip2 --best')
        decomp_methods.append('bzip2 -d')
with col3:
    three_check = st.checkbox('Xz Best')
    if three_check:
        methods.append('xz --best')
        decomp_methods.append('unxz')
# Fast
with col1:
    one_check = st.checkbox('Gzip Fast')
    if one_check:
        methods.append('gzip --fast')
        decomp_methods.append('gunzip')
with col2:
    two_check = st.checkbox('Bzip2 Fast')
    if two_check:
        methods.append('bzip2 --fast')
        decomp_methods.append('bzip2 -d')
with col3:
    three_check = st.checkbox('Xz Fast')
    if three_check:
        methods.append('xz --fast')
        decomp_methods.append('unxz')

st.divider()

comp_button = st.button('Compress your files')
if comp_button:
    file_manager.clear_work_space()
    if uploaded_files or Fake_Files:
        if methods != []:
            if Fake_Files:
                file_manager.sample_files()
            else:
                file_manager.save_file(uploaded_files)
            master.compression_function(methods, decomp_methods)
        else:
            st.warning('No methods have been selected', icon="⚠️")
    else:
        st.warning('No files have been uploaded or selected', icon="⚠️")

st.divider()

if os.path.isfile(path_manager.result_path_check):
    data_holder.create_graph_data(path_manager.result_path_check)
    data = pd.read_csv(path_manager.result_path_check)

col1, left, col2, right, col3 = st.columns([1, 0.1, 1, 0.1, 1])

with col1:
    page1 = st.button("Graphs")

with col2:
    page2 = st.button("Data")

with col3:
    page3 = st.button("One graph")

if page1:
    if os.path.isfile(path_manager.result_path_check):
        st.title('Graphs')
        st.bar_chart(
            pd.DataFrame({'Method': data_holder.unique_methods, 'Compression Factor': data_holder.meanCompressionFactor}),
            x='Method', y='Compression Factor')
        st.bar_chart(
            pd.DataFrame({'Method': data_holder.unique_methods, 'Compression Time (s)': data_holder.meanCompressionTime}),
            x='Method', y='Compression Time (s)')
        st.bar_chart(
            pd.DataFrame(
                {'Method': data_holder.unique_methods, 'Decompression Time (s)': data_holder.meanDecompressionTime}),
            x='Method', y='Decompression Time (s)')
    else:
        st.warning('No results', icon="⚠️")
if page2:
    if os.path.isfile(path_manager.result_path_check):
        st.title('Data Frame')
        st.dataframe(data)
    else:
        st.warning('No results', icon="⚠️")
if page3:
    if os.path.isfile(path_manager.result_path_check):
        st.title('OG Graph ')
        st.pyplot(grapher.og_graph(data))
    else:
        st.warning('No results', icon="⚠️")
