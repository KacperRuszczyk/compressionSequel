# jedna klasa
'''klasy pascal
funkcje snake
constanty pathy i takie tam Takie_Tam
'''

        
        
xz = 'unxz' , 'xz'       
bzip2 = 'bzip2 -d' , 'bzip2'
gzip = 'gunzip' , 'gzip' 



class FileManager:
    def __init__(self):
    
        self.data_dir = '/mount/src/compressionsequel/work_space/data_dir'
        self.compressed_dir = '/mount/src/compressionsequel/work_space/compressed_dir'
        self.decompressed_dir = '/mount/src/compressionsequel/work_space/decompressed_dir'
        self.results_dir = '/mount/src/compressionsequel/work_space/results_dir'
        self.uploaded_dir = '/mount/src/compressionsequel/work_space/uploaded_dir'        
        self.sample_files1 = '/mount/src/compressionsequel/pages'        
        self.sample_files2 = '/mount/src/compressionsequel/images'
    
    def save_file(self,uploaded_files,uploaded_dir):
        for uploaded_file in uploaded_files:
            file_name = uploaded_file.name.replace(" ", "").replace("(", "").replace(")", "")
            with open(os.path.join(uploaded_dir, file_name), "wb") as f:
                f.write(uploaded_file.getbuffer())
        return
        
    def sample_files(self,uploaded_dir,sample_files1,sample_files2):
        files_to_copy = os.listdir(sample_files1)
        for file_name in files_to_copy:
            source_path = os.path.join(sample_files1, file_name)
            destination_path = os.path.join(uploaded_dir, file_name)
            shutil.copy(source_path, destination_path) 
        files_to_copy = os.listdir(sample_files2)
        for file_name in files_to_copy:
            source_path = os.path.join(sample_files2, file_name)
            destination_path = os.path.join(uploaded_dir, file_name)
            shutil.copy(source_path, destination_path) 
        return
        
    def copy_files_from_to(self,files_from,files_to):
        files_to_copy = os.listdir(files_from)
        for file_name in files_to_copy:
            source_path = os.path.join(files_from, file_name)
            destination_path = os.path.join(files_to, file_name)
            shutil.copy(source_path, destination_path)
        return
        
        
    def move_one_file_from_to(self,file_from,file_to):
        source_path = os.path.join(file_from, file_name)
        shutil.move(source_path, file_to)
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
        FileManager.remove_file(path_with_file_name)
        file_name = FileManager.get_list_files_in_dir(self.compressed_dir)
        new_path_with_file_name = os.path.join(self.compressed_dir,file_name)
        return new_path_with_file_name
        
        
        
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
        resoult_time = end_time - start_time        
        return resoult_time
    
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
            
def clear_work_space():
    data_dir = '/mount/src/compressionsequel/work_space/data_dir'
    compressed_dir = '/mount/src/compressionsequel/work_space/compressed_dir'
    decompressed_dir = '/mount/src/compressionsequel/work_space/decompressed_dir'
    results_dir = '/mount/src/compressionsequel/work_space/results_dir'
    uploaded_dir = '/mount/src/compressionsequel/work_space/uploaded_dir'
    for file_name in os.listdir(data_dir):
        path_with_file_name = os.path.join(data_dir, file_name)
        os.remove(path_with_file_name)
    for file_name in os.listdir(compressed_dir):
        path_with_file_name = os.path.join(compressed_dir, file_name)
        os.remove(path_with_file_name)
    for file_name in os.listdir(decompressed_dir):
        path_with_file_name = os.path.join(decompressed_dir, file_name)
        os.remove(path_with_file_name)
    for file_name in os.listdir(results_dir):
        path_with_file_name = os.path.join(results_dir, file_name)
        os.remove(path_with_file_name)
    for file_name in os.listdir(uploaded_dir):
        path_with_file_name = os.path.join(uploaded_dir, file_name)
        os.remove(path_with_file_name)
    return       
        
        
        
mover = FileManager()   
   
clear_work_space()
if uploaded_files or Fale_files:
    if methods != []:
        if Fake_Files:
            mover.sample_files(uploaded_dir,sample_files1,sample_files2)
        else:
            mover.save_file(uploaded_files,uploaded_dir) 
        compression_function()
    else:
        st.warning('No methods have been selected', icon="⚠️")
else:
    st.warning('No files have been uploaded or selected', icon="⚠️")
    
    
    
    
    
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
            tester = FileManager(methods, decomp_methods) 
            tester.add_file_name(file_name) #1
            tester.add_method() #2
            tester.file_size.append(tester.get_file_size(path_with_file_name)) #3
            tester.comp_time.append(tester.compress_decompress(tester.current_comp_method,path_with_file_name) #4     
            path_with_file_name = mover.path_with_file_name_update(path_with_file_name) #update
            tester.file_size_after_comp.append(tester.get_file_size(path_with_file_name))#5
            tester.comp_time.append(tester.compress_decompress(tester.current_decomp_method,path_with_file_name) #6
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