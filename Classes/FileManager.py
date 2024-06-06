import os
import shutil


class FileManager:
    def __init__(self):

        self.percent_progress_bar = 0
        self.data_dir = '/mount/src/compressionsequel/work_space/data_dir'
        self.compressed_dir = '/mount/src/compressionsequel/work_space/compressed_dir'
        self.decompressed_dir = '/mount/src/compressionsequel/work_space/decompressed_dir'
        self.results_dir = '/mount/src/compressionsequel/work_space/results_dir'
        self.uploaded_dir = '/mount/src/compressionsequel/work_space/uploaded_dir'
        self.sample_files1 = '/mount/src/compressionsequel/pages'
        self.sample_files2 = '/mount/src/compressionsequel/images'
        self.result_path_check = '/mount/src/compressionsequel/work_space/results_dir/result.csv'
    def progress_bar_update(self, methods_amount):
        files_amount = len(os.listdir(self.uploaded_dir))
        self.percent_progress_bar = 1 / (files_amount * methods_amount * 2)
        return

    def save_file(self, uploaded_files):
        for uploaded_file in uploaded_files:
            file_name = uploaded_file.name.replace(" ", "").replace("(", "").replace(")", "")
            with open(os.path.join(self.uploaded_dir, file_name), "wb") as f:
                f.write(uploaded_file.getbuffer())
        return

    def sample_files(self):
        files_to_copy = os.listdir(self.sample_files1)
        for file_name in files_to_copy:
            source_path = os.path.join(self.sample_files1, file_name)
            destination_path = os.path.join(self.uploaded_dir, file_name)
            shutil.copy(source_path, destination_path)
        files_to_copy = os.listdir(self.sample_files2)
        for file_name in files_to_copy:
            source_path = os.path.join(self.sample_files2, file_name)
            destination_path = os.path.join(self.uploaded_dir, file_name)
            shutil.copy(source_path, destination_path)
        return

    def copy_files_from_to(self, files_from, files_to):
        files_to_copy = os.listdir(files_from)
        for file_name in files_to_copy:
            source_path = os.path.join(files_from, file_name)
            destination_path = os.path.join(files_to, file_name)
            shutil.copy(source_path, destination_path)
        return

    def move_all_files_from_to(self, files_from, files_to):
        files_to_move = os.listdir(files_from)
        for file_name in files_to_move:
            source_path = os.path.join(files_from, file_name)
            shutil.move(source_path, files_to)
        return

    def remove_file(self, path_with_file_name):
        if os.path.isfile(path_with_file_name):
            os.remove(path_with_file_name)
        return

    def remove_all_files(self, Dir_Path):
        for file_name in os.listdir(Dir_Path):
            path_with_file_name = os.path.join(Dir_Path, file_name)
            os.remove(path_with_file_name)
        return

    def get_list_files_in_dir(self, Dir_Path):
        File_List = os.listdir(Dir_Path)
        return File_List

    def path_with_file_name_update(self, path_with_file_name_old):
        self.remove_file(path_with_file_name_old)
        file_name = self.get_list_files_in_dir(self.compressed_dir)
        new_path_with_file_name_new = os.path.join(self.compressed_dir, file_name[0])
        return new_path_with_file_name_new

    def clear_work_space(self):
        for file_name in os.listdir(self.data_dir):
            path_with_file_name = os.path.join(self.data_dir, file_name)
            os.remove(path_with_file_name)
        for file_name in os.listdir(self.compressed_dir):
            path_with_file_name = os.path.join(self.compressed_dir, file_name)
            os.remove(path_with_file_name)
        for file_name in os.listdir(self.decompressed_dir):
            path_with_file_name = os.path.join(self.decompressed_dir, file_name)
            os.remove(path_with_file_name)
        for file_name in os.listdir(self.results_dir):
            path_with_file_name = os.path.join(self.results_dir, file_name)
            os.remove(path_with_file_name)
        for file_name in os.listdir(self.uploaded_dir):
            path_with_file_name = os.path.join(self.uploaded_dir, file_name)
            os.remove(path_with_file_name)
        return
