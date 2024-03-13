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

st.subheader('Welcome to my app dedicated to showcasing the effectiveness and ineffectiveness in some cases  of lossless compression algorithms')

st.subheader('My platform aims to provide insights into the performance and efficiency of these renowned compression tools.')




