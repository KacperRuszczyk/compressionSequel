# -*- coding: utf-8 -*-
#Debug/compressionScript
import os
import time
import subprocess


def compression(metods, decomp_metodes):
    # Data harvesting arrays
    Files_list = [] #1
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
    i = 0



    for metod in metods:
        #copy files from uploaded_dir to data_dir
        files_to_copy = os.listdir(uploaded_dir)
        for file_name in files_to_copy:
            source_path = os.path.join(uploaded_dir, file_name)
            destination_path = os.path.join(data_dir, file_name)
            shutil.copy(source_path, destination_path)
            
        for file_name in os.listdir(data_dir):
            path_with_file_name = os.path.join(data_dir, file_name)
            
            Files_list.append(file_name) #1
            comp_metode.append(metod) #2
            result_temp = subprocess.run([f"ls -l {path_with_file_name} | awk '{{print $5}}'"], shell=True, capture_output=True, text=True)
            result_temp2 = result_temp.stdout.strip()
            file_size.append(result_temp2) #3
            
            start_time = time.time()    
            subprocess.run([metod, path_with_file_name])
            end_time = time.time()
            comp_time.append(end_time - start_time) #4
            
            os.remove(path_with_file_name)
            
        
        #subprocess.run(['mv', f'{data_dir}/*', compressed_dir])
        files_to_move = os.listdir(data_dir)
        for file_name in files_to_move:
            source_path = os.path.join(data_dir, file_name)
            shutil.move(source_path, compressed_dir)
        
        for file_name in os.listdir(compressed_dir):
            path_with_file_name = os.path.join(compressed_dir, file_name)
            
            result_temp = subprocess.run([f"ls -l {path_with_file_name} | awk '{{print $5}}'"], shell=True, capture_output=True, text=True)
            result_temp2 = result_temp.stdout.strip()
            file_size_after_comp.append(result_temp2) #5
                
            start_time = time.time()    
            if decomp_metodes == list:
                subprocess.run([decomp_metodes[i][0],decomp_metodes[i][1], path_with_file_name], shell=True)
            else:
                subprocess.run([decomp_metodes[i], path_with_file_name], shell=True)
            end_time = time.time()
            decomp_time.append(end_time - start_time) #6
            
            
            result_temp = subprocess.run([f"ls -l {path_with_file_name} | awk '{{print $5}}'"], shell=True, capture_output=True, text=True)
            result_temp2 = result_temp.stdout.strip()
            file_size_after_decomp.append(result_temp2) #7
            
            os.remove(path_with_file_name)
            
        #subprocess.run(['mv', f'{compressed_dir}/*', decompressed_dir])  
        files_to_move = os.listdir(compressed_dir)
        for file_name in files_to_move:
            source_path = os.path.join(compressed_dir, file_name)
            shutil.move(source_path, decompressed_dir)
        i += 1
        
        for file_name in os.listdir(decompressed_dir):
            file_after = os.path.join(compressed_dir, file_name)
            file_before = os.path.join(data_dir, file_name)
            result_temp = subprocess.run([f"diff -s {file_after} {file_before} | awk '{{print $6}}'"], shell=True, capture_output=True, text=True)
            result_temp2 = result_temp.stdout.strip()
            check_if_diff.append(result_temp2)  #8

    return(Files_list)
    
    