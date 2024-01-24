# -*- coding: utf-8 -*-
import os
import time

# cmop / decomp
methods = ['Gzip', 'L4', 'Xz', 'Gzip 2', 'L4 2', 'Xz 2']
decopm_metodes = ['Gzip', 'L4', 'Xz', 'Gzip 2', 'L4 2', 'Xz 2']

# Data variables
files = [] #1
comp_metode = [] #2
file_size = [] #3
comp_time = [] #4
file_size_after_comp = [] #5
decomp_time = [] #6
file_size_after_decomp = [] #7
check_if_diff = [] #8


# Paths
data_dir = '0'
compressed_dir = '0'
decompressed_dir = '0'
results_dir = '0'

i = 0



for method in methods:
    for file_name in os.listdir(data_dir):
        path_with_file_name = os.path.join(data_dir, file_name)
        
        files.append(file_name) #1
        comp_metode.append(method) #2
        file_size.append(os.system("ls -l $path_with_file_name | awk '{print $5}'")) #3
        
        start_time = time.time()    
        os.system("$method $path_with_file_name")
        end_time = time.time()
        comp_time.append(end_time - start_time) #4
        
        os.system("rm $path_with_file_name")
        
    
    os.system("mv $data_dir/* $compressed_dir")
    i = 0
    
    for file_name in os.listdir(compressed_dir):
        path_with_file_name = os.path.join(compressed_dir, file_name)
        
        file_size_after_comp.append(os.system("ls -l $path_with_file_name | awk '{print $5}'")) #5
        
        start_time = time.time()    
        os.system("${decopm_metodes[$i]} $path_with_file_name")
        end_time = time.time()
        decomp_time.append(end_time - start_time) #6
        
        file_size_after_decomp.append(os.system("ls -l $path_with_file_name | awk '{print $5}'")) #7
        
        os.system("rm $path_with_file_name")
        i =+ 1
        
    os.system("mv $compressed_dir/* $decompressed_dir")
    i = 0
    
    for file_name in os.listdir(decompressed_dir):
        path_with_file_name = os.path.join(decompressed_dir, file_name)
        check_if_diff.append(os.system("diff -s $decompressed_dir/$file_name $data_dir/$file_name  | awk '{print $6}'"))
    
    
    
start_time = time.time()    
#
end_time = time.time()
how_long = end_time - start_time

