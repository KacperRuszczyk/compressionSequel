import shutil
import os

from Classes.DataHolder import DataHolder
from Classes.Compresor import Compresor
from Classes.FileManager import FileManager
from Classes.PathManager import PathManager
from Classes.ProgressManager import ProgressManager


class Master:

    def __init__(self):
        self.data_holder = DataHolder()
        self.file_manager = FileManager()
        self.path_manager = PathManager()
        self.progress_manager = ProgressManager()

    def compression_function(self, methods, decomp_methods):
        self.progress_manager.progress_bar_start(methods)

        for file_name in os.listdir(self.path_manager.uploaded_dir):
            self.compression_subfunction(file_name, methods, decomp_methods)

        self.data_holder.prep(self.path_manager.result_path_check)
        self.progress_manager.progress_bar_end()
        return

    def compression_subfunction(self, file_name, methods, decomp_methods):
        path_with_og_file = os.path.join(self.path_manager.uploaded_dir, file_name)
        path_with_file_name = os.path.join(self.path_manager.compressed_dir, file_name)
        shutil.copy(path_with_og_file, path_with_file_name)
        for method in methods:
            compresor = Compresor(methods, decomp_methods)

            self.data_holder.data['files_list'].append(file_name)  # 1
            self.data_holder.data['comp_metode'].append(compresor.add_method())  # 2
            self.data_holder.data['file_size'].append(compresor.get_file_size(path_with_file_name))  # 3

            self.progress_manager.progress_bar_iter(file_name, compresor.current_comp_method)  # bar_comp

            self.data_holder.data['comp_time'].append(
                compresor.compress_decompress(compresor.current_comp_method, path_with_file_name))  # 4
            path_with_file_name = self.file_manager.path_with_file_name_update(path_with_file_name)  # update

            self.progress_manager.progress_bar_iter(file_name, compresor.current_decomp_method)  # bar_decomp

            self.data_holder.data['file_size_after_comp'].append(compresor.get_file_size(path_with_file_name))  # 5
            self.data_holder.data['decomp_time'].append(
                compresor.compress_decompress(compresor.current_decomp_method, path_with_file_name))  # 6

            path_with_file_name = self.file_manager.path_with_file_name_update(path_with_file_name)  # update

            self.data_holder.data['file_size_after_decomp'].append(compresor.get_file_size(path_with_file_name))  # 7
            self.data_holder.data['check_if_diff'].append(
                compresor.compare(path_with_file_name, path_with_og_file))  # 8

        self.file_manager.remove_file(path_with_file_name)
        return
