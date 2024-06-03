import streamlit as st
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import pandas as pd
import os
import subprocess
import shutil
import time

import my_functions

st.set_page_config(
    page_title="Compression Demo",
    page_icon="📊",
    initial_sidebar_state='expanded'
)


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
st.markdown('*3. Click the "compress ..." button. (FYI, that buttons also clears the results data from previous attempts.)*')
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
        decomp_methods.append(['bzip2 -d'])
with col3:
    three_check = st.checkbox('Xz')
    if three_check:
        methods.append('xz') 
        decomp_methods.append('unxz')
#Best
with col1:
    one_check = st.checkbox('Gzip Best')
    if one_check:
        methods.append(['gzip --best'])  
        decomp_methods.append('gunzip')
with col2:
    two_check = st.checkbox('Bzip2 Best')
    if two_check:
        methods.append(['bzip2 --best'])       
        decomp_methods.append(['bzip2 -d'])
with col3:
    three_check = st.checkbox('Xz Best')
    if three_check:
        methods.append(['xz --best']) 
        decomp_methods.append('unxz')
#Fast
with col1:
    one_check = st.checkbox('Gzip Fast')
    if one_check:
        methods.append(['gzip --fast'])  
        decomp_methods.append('gunzip')
with col2:
    two_check = st.checkbox('Bzip2 Fast')
    if two_check:
        methods.append(['bzip2 --fast'])       
        decomp_methods.append(['bzip2 -d'])
with col3:
    three_check = st.checkbox('Xz Fast')
    if three_check:
        methods.append(['xz --fast']) 
        decomp_methods.append('unxz')


st.divider()
        

class FileManager:
    def __init__(self):
    
        self.data_dir = '/mount/src/compressionsequel/work_space/data_dir'
        self.compressed_dir = '/mount/src/compressionsequel/work_space/compressed_dir'
        self.decompressed_dir = '/mount/src/compressionsequel/work_space/decompressed_dir'
        self.results_dir = '/mount/src/compressionsequel/work_space/results_dir'
        self.uploaded_dir = '/mount/src/compressionsequel/work_space/uploaded_dir'        
        self.sample_files1 = '/mount/src/compressionsequel/pages'        
        self.sample_files2 = '/mount/src/compressionsequel/images'
    
    def save_file(self,uploaded_files):
        for uploaded_file in uploaded_files:
            file_name = uploaded_file.name.replace(" ", "").replace("(", "").replace(")", "")
            with open(os.path.join(self.uploaded_dir, file_name), "wb") as f:
                f.write(uploaded_file.getbuffer())
        return
        
    def sample_files(self):
        files_to_copy = os.listdir(self.sample_files1)
        for file_name in files_to_copy:
            source_path = os.path.join(self.sample_files1, file_name)
            destination_path = os.path.join(self.uploaded_dir, file_name)
            shutil.copy(source_path, destination_path) 
        files_to_copy = os.listdir(self.sample_files2)
        for file_name in files_to_copy:
            source_path = os.path.join(self.sample_files2, file_name)
            destination_path = os.path.join(self.uploaded_dir, file_name)
            shutil.copy(source_path, destination_path) 
        return
        
    def copy_files_from_to(self,files_from,files_to):
        files_to_copy = os.listdir(files_from)
        for file_name in files_to_copy:
            source_path = os.path.join(files_from, file_name)
            destination_path = os.path.join(files_to, file_name)
            shutil.copy(source_path, destination_path)
        return
        
        
    
    def move_all_files_from_to(self,files_from,files_to):
        files_to_move = os.listdir(files_from)
        for file_name in files_to_move:
            source_path = os.path.join(files_from, file_name)
            shutil.move(source_path, files_to)
        return
        
    def remove_file(self,path_with_file_name):
        if os.path.isfile(path_with_file_name):
            os.remove(path_with_file_name)
        return   
        
    def remove_all_files(self,Dir_Path):
        for file_name in os.listdir(Dir_Path):
            path_with_file_name = os.path.join(Dir_Path, file_name)
            os.remove(path_with_file_name)
        return
        
    def get_list_files_in_dir(self,Dir_Path):
        File_List = os.listdir(Dir_Path)
        return File_List
    
    def path_with_file_name_update(self,path_with_file_name):
        self.remove_file(path_with_file_name)
        file_name = self.get_list_files_in_dir(self.compressed_dir)
        new_path_with_file_name = os.path.join(self.compressed_dir,file_name[0])
        return new_path_with_file_name
  
    def clear_work_space(self):
        for file_name in os.listdir(self.data_dir):
            path_with_file_name = os.path.join(self.data_dir, file_name)
            os.remove(path_with_file_name)
        for file_name in os.listdir(self.compressed_dir):
            path_with_file_name = os.path.join(self.compressed_dir, file_name)
            os.remove(path_with_file_name)
        for file_name in os.listdir(self.decompressed_dir):
            path_with_file_name = os.path.join(self.decompressed_dir, file_name)
            os.remove(path_with_file_name)
        for file_name in os.listdir(self.results_dir):
            path_with_file_name = os.path.join(self.results_dir, file_name)
            os.remove(path_with_file_name)
        for file_name in os.listdir(self.uploaded_dir):
            path_with_file_name = os.path.join(self.uploaded_dir, file_name)
            os.remove(path_with_file_name)
        return      

  
        
        
class Compresor:
    
    Counter = 0
    
    def __init__(self, methods, decomp_methods):
                
        self.files_list = [] #1
        self.comp_method = [] #2
        self.file_size = [] #3
        self.comp_time = [] #4
        self.file_size_after_comp = [] #5
        self.decomp_time = [] #6
        self.file_size_after_decomp = [] #7
        self.check_if_diff = [] #8
        self.current_comp_method = methods[Compresor.Counter]
        self.current_decomp_method = decomp_methods[Compresor.Counter]
        Compresor.Counter += 1
        
    def get_file_size(self,path_with_file_name): #3, 5, 7
        File_Size = os.path.getsize(path_with_file_name)
        return File_Size
    
    def compress_decompress(self,method,File_Path): #4, 6
        start_time = time.time()
        os.system(f'{method} {File_Path}')
        end_time = time.time()
        result_time = end_time - start_time        
        return result_time
    
    def compare(self,file_after,file_before): #8
        result_temp = subprocess.run([f"diff -s {file_after} {file_before} | awk '{{print $6}}'"], shell=True, capture_output=True, text=True)
        self.check_if_diff.append(result_temp)
        return
    
    def add_file_name(self,file_name): #1
        self.files_list.append(file_name)
        return
    
    def add_method(self): #2
        self.comp_method.append(self.current_comp_method)
        return
            


    
    
    
def compression_function():   

    data = pd.DataFrame({
        'method': [] ,
        'filename': [] ,
        'sizeBefore': [] ,
        'compressionTime': [],
        'compressedFileSize': [],
        'decompressionTime': [],
        'sizeAfterDecompression': [],
        'different': []})
        
    mover = FileManager()     
    
    for file_name in os.listdir(mover.uploaded_dir):
        path_with_og_file = os.path.join(mover.uploaded_dir, file_name)
        path_with_file_name = os.path.join(mover.compressed_dir, file_name)
        shutil.copy(path_with_og_file, path_with_file_name)  
        for method in methods:
            tester = Compresor(methods, decomp_methods) 
            tester.add_file_name(file_name) #1
            tester.add_method() #2
            tester.file_size.append(tester.get_file_size(path_with_file_name)) #3
            tester.comp_time.append(tester.compress_decompress(tester.current_comp_method,path_with_file_name)) #4     
            path_with_file_name = mover.path_with_file_name_update(path_with_file_name) #update
            tester.file_size_after_comp.append(tester.get_file_size(path_with_file_name))#5
            tester.decomp_time.append(tester.compress_decompress(tester.current_decomp_method,path_with_file_name)) #6
            path_with_file_name = mover.path_with_file_name_update(path_with_file_name) #update
            tester.file_size_after_decomp.append(tester.get_file_size(path_with_file_name)) #7
            tester.compare(path_with_file_name,path_with_og_file) #8
            
            data2 = pd.DataFrame({
            'method': tester.comp_method,
            'filename': tester.files_list,
            'sizeBefore': tester.file_size,
            'compressionTime': tester.comp_time,
            'compressedFileSize': tester.file_size_after_comp,
            'decompressionTime': tester.decomp_time,
            'sizeAfterDecompression': tester.file_size_after_decomp,
            'different': tester.check_if_diff})
            
            data = pd.concat([data, data2], ignore_index=True)
            
            
    data['compressionFactor'] = 100 - (100 * data['compressedFileSize'] / data['sizeBefore'])
    data.to_csv('/mount/src/compressionsequel/work_space/results_dir/result.csv', index=False)  
    return
 



        
        
        
mover = FileManager()   
        
comp_button = st.button('Compress your files')
if comp_button:   
    mover.clear_work_space()
    if uploaded_files or Fake_Files:
        if methods != []:
            if Fake_Files:
                mover.sample_files()
            else:
                mover.save_file(uploaded_files) 
            compression_function()
        else:
            st.warning('No methods have been selected', icon="⚠️")
    else:
        st.warning('No files have been uploaded or selected', icon="⚠️")
        
    


st.divider()

if os.path.isfile('/mount/src/compressionsequel/work_space/results_dir/result.csv'):      
    data = pd.read_csv('/mount/src/compressionsequel/work_space/results_dir/result.csv')
    unique_methods = list(set(data['method']))
    averageTime = data['compressionTime'].mean()
    for method in unique_methods:
        mask = data['method'] == method
        meanCompressionFactor.append(data['compressionFactor'][mask].mean())
        meanCompressionTime.append(data['compressionTime'][mask].mean())
        meanDecompressionTime.append(data['decompressionTime'][mask].mean())




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
        st.bar_chart(pd.DataFrame({'Method': unique_methods, 'Compression Factor': meanCompressionFactor}), x='Method', y='Compression Factor')
        st.bar_chart(pd.DataFrame({'Method': unique_methods, 'Compression Time (s)': meanCompressionTime}), x='Method', y='Compression Time (s)')
        st.bar_chart(pd.DataFrame({'Method': unique_methods, 'Decompression Time (s)': meanDecompressionTime}), x='Method', y='Decompression Time (s)')
    else:
        st.warning('No results', icon="⚠️")
if page2:
    if os.path.isfile(result_path_check):
        st.title('Data Frame')
        #st.dataframe(my_functions.result_data_frame(unique_methods,meanCompressionFactor,meanCompressionTime,meanDecompressionTime))
        st.dataframe(data)
    else:
        st.warning('No results', icon="⚠️")
if page3:
    if os.path.isfile(result_path_check):
        st.title('OG Graph ')
        st.pyplot(my_functions.Graph_with_dots(data))
    else:
        st.warning('No results', icon="⚠️")




       
#PATH = '/mount/src/compressionsequel/work_space/results_dir/result.csv'
#if st.button("Download File"):
    #st.markdown(f'<a href="{PATH}" download="results.csv">download</a>', unsafe_allow_html=True)
