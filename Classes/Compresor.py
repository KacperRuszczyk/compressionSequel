import os
import subprocess
import time
import pandas as pd

class Compresor:
    Counter = 0

    def __init__(self, methods, decomp_methods):
        self.current_comp_method = methods[Compresor.Counter % len(methods) - 1]
        self.current_decomp_method = decomp_methods[Compresor.Counter % len(decomp_methods) - 1]
        Compresor.Counter += 1

    def get_file_size(self, path_with_file_name):  # 3, 5, 7
        file_Size = os.path.getsize(path_with_file_name)
        return file_Size

    def compress_decompress(self, method, File_Path):  # 4, 6

        os.system(f'{method} {File_Path}')

        return

    def compare(self, file_after, file_before):  # 8
        result_temp = subprocess.run(
            f"diff -s {file_after} {file_before}",
            shell=True,
            capture_output=True,
            text=True
        )
        if 'identical' in result_temp.stdout:
            return 'identical'
        else:
            return 'not identical'

    def add_method(self):  # 2
        return self.current_comp_method

