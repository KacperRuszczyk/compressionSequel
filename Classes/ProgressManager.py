import os
import streamlit as st
from Classes.FileManager import FileManager
from Classes.PathManager import PathManager


class ProgressManager:
    def __init__(self):
        self.file_manager = FileManager()
        self.path_manager = PathManager()
        self.percent_progress_bar = 0
        self.progres_amount = 0
        self.progress_bar = 0

    def progress_bar_update(self, methods_amount):
        files_amount = len(os.listdir(self.path_manager.uploaded_dir))
        self.percent_progress_bar = 1 / (files_amount * methods_amount * 2)
        return

    def progress_bar_start(self, methods):
        self.progress_bar_update(len(methods))
        progress_text = "Operation in progress. Please wait."
        self.progres_amount = self.percent_progress_bar
        self.progress_bar = st.progress(0, text=progress_text)
        return

    def progress_bar_iter(self, file_name, current_comp_method):
        progress_text = f"compressing {file_name} with {current_comp_method}. Please wait."
        self.progress_bar.progress(self.progres_amount, text=progress_text)
        if self.progres_amount < 1 - self.percent_progress_bar:
            self.progres_amount += self.percent_progress_bar
        return

    def progress_bar_end(self):
        self.progress_bar.empty()
        st.success('results are done!', icon='🥧')
        return
