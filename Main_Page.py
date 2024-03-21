# -*- coding: utf-8 -*-
#Debug/compressionPlot
import streamlit as st
import pandas as pd
import os

import my_functions

def test():
    from streamlit.runtime.scriptrunner import get_script_run_ctx
    session_id = get_script_run_ctx().session_id
    return session_id


st.set_page_config(
    page_title="Compression",
    page_icon="👻",
    initial_sidebar_state='expanded'
)

#streamlit boot PATH creation
if os.path.exists('/mount/src/compressionsequel/work_space') == False:
    os.mkdir('/mount/src/compressionsequel/work_space')
    os.mkdir('/mount/src/compressionsequel/work_space/data_dir')
    os.mkdir('/mount/src/compressionsequel/work_space/compressed_dir')
    os.mkdir('/mount/src/compressionsequel/work_space/decompressed_dir')
    os.mkdir('/mount/src/compressionsequel/work_space/results_dir')
    os.mkdir('/mount/src/compressionsequel/work_space/uploaded_dir')
    
if os.path.exists('/mount/src/compressionsequel/user_check') == False:    
    os.mkdir('/mount/src/compressionsequel/user_check')

user_session = my_functions._get_session()
user_file_check = '/mount/src/compressionsequel/user_checkcheck.txt'
if os.path.isfile(user_file_check):
    st.markdown('path true')
    with open(user_file_check) as file:
        line = file.readline()
    if str(line) == str(user_session):
        pass
        st.markdown('pass')
    else:
        st.markdown('clear')
        os.remove(user_file_check)
        my_functions.clear_work_space()
        with open(user_file_check, "w") as file:
            file.write(str(user_session))
else:
    st.markdown('else create')
    with open(user_file_check, "w") as file:
        file.write(str(user_session))






session_id = test()

st.markdown(session_id)


