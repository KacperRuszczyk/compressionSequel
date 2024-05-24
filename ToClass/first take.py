# jedna klasa
'''klasy pascal
funkcje snake
constanty pathy i takie tam Takie_Tam
'''
class gzip:
    def __init__(self,file_path):
        self.file_path = file_path
        
    def compress(self,modifier=None):
        start_time = time.time()
        if self.modifier == None:
            os.system(f'gzip {self.file_path}')
        else:
            os.system(f'gzip {self.modifier} {self.file_path}')
        end_time = time.time()
        resoult_time = end_time - start_time        
        return resoult_time
        
    def decompress(self):
        start_time = time.time()
        os.system(f'gunzip {self.file_path}')
        end_time = time.time()
        resoult_time = end_time - start_time       
        return resoult_time
        
class bzip2:
    def __init__(self,file_path):
        self.file_path = file_path
        
    def compress(self,modifier=None):
        start_time = time.time()
        if self.modifier == None:
            os.system(f'bzip2 {self.file_path}')
        else:
            os.system(f'bzip2 {self.modifier} {self.file_path}')
        end_time = time.time()
        resoult_time = end_time - start_time        
        return resoult_time
        
    def decompress(self):
        start_time = time.time()
        os.system(f'bzip2 -d {self.file_path}')
        end_time = time.time()
        resoult_time = end_time - start_time       
        return resoult_time
      

class xz:
    def __init__(self,file_path):
        self.file_path = file_path
        
    def compress(self,modifier=None):
        start_time = time.time()
        if self.modifier == None:
            os.system(f'xz {self.file_path}')
        else:
            os.system(f'xz {self.modifier} {self.file_path}')
        end_time = time.time()
        resoult_time = end_time - start_time        
        return resoult_time
        
    def decompress(self):
        start_time = time.time()
        os.system(f'unxz {self.file_path}')
        end_time = time.time()
        resoult_time = end_time - start_time       
        return resoult_time
            
        
        
        
xz = 'unxz' , 'xz'       
bzip2 = 'bzip2 -d' , 'bzip2'
gzip = 'gunzip' , 'gzip' 

files_list = [] #1
comp_metode = [] #2
file_size = [] #3
comp_time = [] #4
file_size_after_comp = [] #5
decomp_time = [] #6
file_size_after_decomp = [] #7
check_if_diff = [] #8

# Paths
data_dir = '/mount/src/compressionsequel/work_space/data_dir'
compressed_dir = '/mount/src/compressionsequel/work_space/compressed_dir'
decompressed_dir = '/mount/src/compressionsequel/work_space/decompressed_dir'
results_dir = '/mount/src/compressionsequel/work_space/results_dir'
uploaded_dir = '/mount/src/compressionsequel/work_space/uploaded_dir'        
        
        
class Compression:
    def __init__(self,File_Path):
        self.File_Path = File_Path
        
    def compress_decompress(self,method):
        start_time = time.time()
        os.system(f'{self.method} {self.File_Path}')
        end_time = time.time()
        resoult_time = end_time - start_time        
        return resoult_time
        
    
    
class FileManager:
    def __init__(slef,File_Path):
        self.File_Path = File_Path
            
    def copy_files_from_to(self,files_from,files_to):
        files_to_copy = os.listdir(self.files_from)
        for file_name in files_to_copy:
            source_path = os.path.join(self.files_from, file_name)
            destination_path = os.path.join(self.files_to, file_name)
            shutil.copy(source_path, destination_path)
        return
        
    def move_one_file_from_to(self,file_from,file_to):
            source_path = os.path.join(self.file_from, file_name)
            shutil.move(source_path, self.file_to)
        return
    
    def move_all_files_from_to(self,files_from,files_to):
        files_to_move = os.listdir(self.files_from)
        for file_name in files_to_move:
            source_path = os.path.join(self.files_from, file_name)
            shutil.move(source_path, self.files_to)
        return
        
    def remove_file(self,path_with_file_name):
        if os.path.isfile(self.path_with_file_name):
            os.remove(self.path_with_file_name)
        return   
        
    def remove_all_files(self,Dir_Path)
        for file_name in os.listdir(self.Dir_Path):
            path_with_file_name = os.path.join(self.Dir_Path, file_name)
            os.remove(path_with_file_name)
        return
        
    def compress_decompress(self,method):
        start_time = time.time()
        os.system(f'{self.method} {self.File_Path}')
        end_time = time.time()
        resoult_time = end_time - start_time        
        return resoult_time
        
    def get_file_size(self,path_with_file_name):
        File_Size = os.path.getsize(path_with_file_name)
        return File_Size
        
    def get_list_files_in_dir(self,Dir_Path):
        File_List = os.listdir(self.Dir_Path)
        return File_List