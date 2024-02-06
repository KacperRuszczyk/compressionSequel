# -*- coding: utf-8 -*-
import os
import time
import subprocess
# cmop / decomp
metods = ['Gzip', 'L4', 'Xz', 'Gzip 2', 'L4 2', 'Xz 2']
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
data_dir = '/mount/src/compressionsequel/work_space/data_dir'
compressed_dir = '/mount/src/compressionsequel/work_space/compressed_dir'
decompressed_dir = '/mount/src/compressionsequel/work_space/decompressed_dir'
results_dir = '/mount/src/compressionsequel/work_space/results_dir'

i = 0



for metod in metods:
    for file_name in os.listdir(data_dir):
        path_with_file_name = os.path.join(data_dir, file_name)
        
        files.append(file_name) #1
        comp_metode.append(metod) #2
        result_temp = subprocess.run([f"ls -l {path_with_file_name} | awk '{{print $5}}'"], shell=True, capture_output=True, text=True)
        result_temp2 = result_temp.stdout.strip()
        file_size.append(result_temp2) #3
        
        start_time = time.time()    
        subprocess.run([metod, path_with_file_name])
        end_time = time.time()
        comp_time.append(end_time - start_time) #4
        
        subprocess.run(['rm', path_with_file_name])
        
    
    subprocess.run(['mv', f'{data_dir}/*', compressed_dir])
    
    
    for file_name in os.listdir(compressed_dir):
        path_with_file_name = os.path.join(compressed_dir, file_name)
        
        file_size_after_comp.append(subprocess.run(["ls -l $path_with_file_name | awk '{print $5}'"])) #5
        
        start_time = time.time()    
        subprocess.run(["${decopm_metodes[$i]} $path_with_file_name"])
        end_time = time.time()
        decomp_time.append(end_time - start_time) #6
        
        file_size_after_decomp.append(subprocess.run(["ls -l $path_with_file_name | awk '{print $5}'"])) #7
        
        subprocess.run(["rm $path_with_file_name"])
        
        
    subprocess.run(["mv $compressed_dir/* $decompressed_dir"])
    i =+ 1
    
    for file_name in os.listdir(decompressed_dir):
        path_with_file_name = os.path.join(decompressed_dir, file_name)
        check_if_diff.append(subprocess.run(["diff -s $decompressed_dir/$file_name $data_dir/$file_name  | awk '{print $6}'"]))
    
    
    
start_time = time.time()    
#
end_time = time.time()
how_long = end_time - start_time



results = os.path.join(results_dir, 'results.csv')

with open(results, 'a') as file:
    file.write("method;filename;size_before;compression_time;size_after_compression;decompression_time;size_after_decompression;are_identical\n")

    for i in range(len(cmethods)):    
        file.write(f"{comp_metode[i]};{files[i]};{file_size[i]};{comp_time[i]};{file_size_after_comp[i]};{decomp_time[i]};{file_size_after_decomp[i]};{check_if_diff[i]}\n")