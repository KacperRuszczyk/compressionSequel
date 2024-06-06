import os
import subprocess
import time
import pandas as pd
class Compresor:
    Counter = 0

    def __init__(self, methods, decomp_methods):
        self.files_list = []  # 1
        self.comp_method = []  # 2
        self.file_size = []  # 3
        self.comp_time = []  # 4
        self.file_size_after_comp = []  # 5
        self.decomp_time = []  # 6
        self.file_size_after_decomp = []  # 7
        self.check_if_diff = []  # 8
        self.meanCompressionFactor = []
        self.meanCompressionTime = []
        self.meanDecompressionTime = []
        self.unique_methods = []
        self.current_comp_method = methods[Compresor.Counter % len(methods) - 1]
        self.current_decomp_method = decomp_methods[Compresor.Counter % len(decomp_methods) - 1]
        Compresor.Counter += 1

    def get_file_size(self, path_with_file_name):  # 3, 5, 7
        File_Size = os.path.getsize(path_with_file_name)
        return File_Size

    def compress_decompress(self, method, File_Path):  # 4, 6
        start_time = time.time()
        os.system(f'{method} {File_Path}')
        end_time = time.time()
        result_time = end_time - start_time
        return result_time

    def compare(self, file_after, file_before):  # 8
        result_temp = subprocess.run(
            f"diff -s {file_after} {file_before}",
            shell=True,
            capture_output=True,
            text=True
        )
        if 'identical' in result_temp.stdout:
            self.check_if_diff.append(True)
        else:
            self.check_if_diff.append(False)
        return

    def add_file_name(self, file_name):  # 1
        self.files_list.append(file_name)
        return

    def add_method(self):  # 2
        self.comp_method.append(self.current_comp_method)
        return

    def create_graph_data(self,result_path_check):

        data = pd.read_csv(result_path_check)
        self.unique_methods = list(set(data['method']))
        averageTime = data['compressionTime'].mean()
        for method in self.unique_methods:
            mask = data['method'] == method
            self.meanCompressionFactor.append(data['compressionFactor'][mask].mean())
            self.meanCompressionTime.append(data['compressionTime'][mask].mean())
            self.meanDecompressionTime.append(data['decompressionTime'][mask].mean())

