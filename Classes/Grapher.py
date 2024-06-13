import matplotlib.pyplot as plt
import matplotlib.patches as mpatches


class Grapher:
    def og_graph(self, data):
        colors_dict = {
            "gzip": "red",
            "gzip --best": "yellow",
            "gzip --fast": "orange",
            "bzip2": "blue",
            "bzip2 --best": "purple",
            "bzip2 --fast": "magenta",
            "xz": "green",
            "xz --best": "lime",
            "xz --fast": "olive"}
        legend = [mpatches.Patch(color=color, label=label) for label, color in colors_dict.items()]
        colors = [colors_dict[m] for m in data['comp_metode']]
        fig = plt.figure(figsize=(12, 10))
        plt.xticks(fontsize=14)
        plt.yticks(fontsize=14)
        plt.scatter(data['comp_time'], data['compressionFactor'], c=colors)
        plt.xlabel('Compression Time (s)', fontsize=17)
        plt.ylabel('Compression Factor (%)', fontsize=17)
        plt.title(' ')
        plt.legend(handles=legend)
        return fig