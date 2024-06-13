import pandas as pd

class DataHolder:
    def __init__(self):
        self.data = {
            'comp_metode': [],
            'files_list': [],
            'file_size': [],
            'comp_time': [],
            'file_size_after_comp': [],
            'decomp_time': [],
            'file_size_after_decomp': [],
            'check_if_diff': []}
        self.meanCompressionFactor = []
        self.meanCompressionTime = []
        self.meanDecompressionTime = []
        self.unique_methods = []

    def prep(self, Path):
        data = pd.DataFrame(self.data)
        data['compressionFactor'] = 100 - (100 * data['file_size_after_comp'] / data['file_size'])
        data.to_csv(Path, index=False)
        return
    def create_graph_data(self, result_path_check):

        data = pd.read_csv(result_path_check)
        self.unique_methods = list(set(data['comp_metode']))
        averageTime = data['comp_time'].mean()
        for method in self.unique_methods:
            mask = data['comp_metode'] == method
            self.meanCompressionFactor.append(data['compressionFactor'][mask].mean())
            self.meanCompressionTime.append(data['comp_time'][mask].mean())
            self.meanDecompressionTime.append(data['decomp_time'][mask].mean())
