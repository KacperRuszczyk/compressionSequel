# -*- coding: utf-8 -*-
#Debug/compressionPlot
import streamlit as st
import pandas as pd
import os



import my_functions


#streamlit boot PATH creation
if os.path.exists('/mount/src/compressionsequel/work_space') == False:
    os.mkdir('/mount/src/compressionsequel/work_space')
    os.mkdir('/mount/src/compressionsequel/work_space/data_dir')
    os.mkdir('/mount/src/compressionsequel/work_space/compressed_dir')
    os.mkdir('/mount/src/compressionsequel/work_space/decompressed_dir')
    os.mkdir('/mount/src/compressionsequel/work_space/results_dir')
    os.mkdir('/mount/src/compressionsequel/work_space/uploaded_dir')

st.set_page_config(
    page_title="Compression",
    page_icon="👻",
    initial_sidebar_state='expanded'
)

st.sidebar.success("Select page above.")

st.title(':red[Efficiency of Lossless Compression Algorithms]')

st.subheader('Welcome to my app dedicated to showcasing the effectiveness and ineffectiveness of lossless compression algorithms.')

st.subheader('My platform aims to provide insights into the performance and efficiency of renowned compression tools such as Bzip2, gzip, and xz.')

st.subheader('Here You can find things such as:')

left, mid, right = st.columns([1, 0.2, 1])

with left:
    st.subheader(':red[Compression app]')
    st.markdown('That can help you visualise how Bzip2, gzip, and xz are compressing different kinds of file types')
    st.markdown('Here you can also see how the compression script operates:')
with mid:
    st.subheader('and')

with right:
    st.subheader(':red[Information about Algorithms]')
    st.markdown('Used in all the three compression programs')
left, right = st.columns([1, 1])



page1 = st.button("Script")


if page1:
    st.image('images/Skrypt.png')
    



switch_page_button = st.button('compression demo')
if switch_page_button:
    my_functions.switch_page("compression demo")