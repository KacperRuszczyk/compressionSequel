# jedna klasa
'''klasy pascal
funkcje snake
constanty pathy i takie tam Takie_Tam
'''

        
        
xz = 'unxz' , 'xz'       
bzip2 = 'bzip2 -d' , 'bzip2'
gzip = 'gunzip' , 'gzip' 



# Paths
data_dir = '/mount/src/compressionsequel/work_space/data_dir'
compressed_dir = '/mount/src/compressionsequel/work_space/compressed_dir'
decompressed_dir = '/mount/src/compressionsequel/work_space/decompressed_dir'
results_dir = '/mount/src/compressionsequel/work_space/results_dir'
uploaded_dir = '/mount/src/compressionsequel/work_space/uploaded_dir'        
      
sample_files1 = '/mount/src/compressionsequel/pages'        
sample_files2 = '/mount/src/compressionsequel/images'






class FileManager:
    def __init__(slef):
        
        self.files_list = [] #1
        self.comp_metode = [] #2
        self.file_size = [] #3
        self.comp_time = [] #4
        self.file_size_after_comp = [] #5
        self.decomp_time = [] #6
        self.file_size_after_decomp = [] #7
        self.check_if_diff = [] #8
        
    def save_file(self,uploaded_files,uploaded_dir):
        for uploaded_file in uploaded_files
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
        
    def remove_all_files(self,Dir_Path)
        for file_name in os.listdir(Dir_Path):
            path_with_file_name = os.path.join(Dir_Path, file_name)
            os.remove(path_with_file_name)
        return
        
    def compress_decompress(self,method,File_Path):
        start_time = time.time()
        os.system(f'{method} {File_Path}')
        end_time = time.time()
        resoult_time = end_time - start_time        
        return resoult_time
        
    def get_file_size(self,path_with_file_name):
        File_Size = os.path.getsize(path_with_file_name)
        return File_Size
        
    def get_list_files_in_dir(self,Dir_Path):
        File_List = os.listdir(Dir_Path)
        return File_List
        
        
        
mover = FileManager()   

if Fake_Files:
    mover.sample_files(uploaded_dir,sample_files1,sample_files2)
else:
    mover.save_file(uploaded_files,uploaded_dir)
    
for File_Name in os.listdir(Dir_Path):
    mover.copy_files_from_to()
    for method in methods:
        tester = FileManager()  
    