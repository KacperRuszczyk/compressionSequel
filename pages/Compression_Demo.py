import streamlit as st
import pandas as pd
import os

from Classes.Compresor import Compresor
from Classes.FileManager import FileManager
import my_functions

st.set_page_config(
    page_title="Compression Demo",
    page_icon="📊",
    initial_sidebar_state='expanded'
)
mover = FileManager()

result_path_check = '/mount/src/compressionsequel/work_space/results_dir/result.csv'
data = 0
unique_methods = 0
methods = []
decomp_methods = []
meanCompressionFactor = []
meanCompressionTime = []
meanDecompressionTime = []

st.title(':orange[Compression Demo]',anchor=False)
st.markdown("*1. Upload some files (I would recommend uploading one file extension type, but I'm not going to tell you how to live your life).*")
st.markdown("*2. Choose the compression options that you would like to test.*")
st.markdown('*3. Click the "compress ..." button. (FYI, that buttons also clears the results data from previous attempt.)*')
st.markdown('*4. Wait until the process is done and view the results.*')
st.divider()
 
col1, left, col2= st.columns([1,0.1,1])

with col1:
    uploaded_files = st.file_uploader("Upload your files here...", accept_multiple_files=True)
with col2:
    fake_files_check = st.checkbox('Use Sample Files')
    if fake_files_check:
        Fake_Files = True
    else:
        Fake_Files = False

col1, left, col2, right, col3 = st.columns([1,0.1,1,0.1,1])
#Regular
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
#Best
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
#Fast
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
    mover.clear_work_space()
    if uploaded_files or Fake_Files:
        if methods != []:
            if Fake_Files:
                mover.sample_files()
            else:
                mover.save_file(uploaded_files) 
            my_functions.compression_function(methods,decomp_methods)
        else:
            st.warning('No methods have been selected', icon="⚠️")
    else:
        st.warning('No files have been uploaded or selected', icon="⚠️")
        
    


st.divider()

if os.path.isfile(mover.result_path_check):
    tester = Compresor(methods, decomp_methods)
    tester.create_graph_data(result_path_check)




col1, left, col2, right, col3 = st.columns([1, 0.1, 1, 0.1, 1])

with col1:
    page1 = st.button("Graphs")

with col2:
    page2 = st.button("Data")

with col3:
    page3 = st.button("One graph")
    

if page1:
    if os.path.isfile(result_path_check):
        st.title('Graphs')
        st.bar_chart(pd.DataFrame({'Method': tester.unique_methods, 'Compression Factor': tester.meanCompressionFactor}), x='Method', y='Compression Factor')
        st.bar_chart(pd.DataFrame({'Method': tester.unique_methods, 'Compression Time (s)': tester.meanCompressionTime}), x='Method', y='Compression Time (s)')
        st.bar_chart(pd.DataFrame({'Method': tester.unique_methods, 'Decompression Time (s)': tester.meanDecompressionTime}), x='Method', y='Decompression Time (s)')
    else:
        st.warning('No results', icon="⚠️")
if page2:
    if os.path.isfile(result_path_check):
        st.title('Data Frame')
        st.dataframe(data)
    else:
        st.warning('No results', icon="⚠️")
if page3:
    if os.path.isfile(result_path_check):
        st.title('OG Graph ')
        st.pyplot(my_functions.Graph_with_dots(data))
    else:
        st.warning('No results', icon="⚠️")



