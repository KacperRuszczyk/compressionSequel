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

st.title(':orange[Lossless Compression Algorithms]')

st.subheader('This app showcases the effectiveness of lossless compression algorithms.')

st.subheader("Here you'll be able to examine the performance and efficiency of multiple compression tools. See for yourself!")

st.subheader(':arrow_left: Just pick one of the sites on the left.')

left, mid, right = st.columns([1, 0.2, 1])

with left:
    st.subheader(':orange[Compression app]')
    st.markdown('Demo that can help you visualise how Bzip2, gzip, and xz are compressing different kinds of file types')
    st.markdown('Here you can also see how the compression script operates:')
with mid:
    st.subheader('and')

with right:
    st.subheader(':orange[Information about Algorithms]')
    st.markdown('Used in all the three compression programs.')




st.image('images/Script.png')
    


