
#------------------ copy from to
def copy_files_from_to(files_from,files_to):
    files_to_copy = os.listdir(files_from)
    for file_name in files_to_copy:
        source_path = os.path.join(files_from, file_name)
        destination_path = os.path.join(files_to, file_name)
        shutil.copy(source_path, destination_path)
    return



#------------------ move from to 
def move_files_from_to(files_from,files_to):
    files_to_move = os.listdir(files_from)
    for file_name in files_to_move:
        source_path = os.path.join(files_from, file_name)
        shutil.move(source_path, files_to)
    return
    
    
    
#------------------ remove     
def remove_file(path_with_file_name):
    if os.path.isfile(path_with_file_name):
        os.remove(path_with_file_name)
    return   



#------------------ comp/decomp
def comp_decomp(method,path_with_file_name):
    start_time = time.time()    
    if type(method) == list:
        os.system(f'{method[0]} {method[1]} {path_with_file_name}')
    else:
        os.system(f'{method} {path_with_file_name}')
    end_time = time.time()
    resoult_time = end_time - start_time
    return resoult_time



