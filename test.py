import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import numpy as np
import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import matplotlib.cm as cm
from Exoplanets_basic_info import list, columns, rus_columns
from pywaffle import Waffle

class Diagrams:
    def __init__(self, prmtr_name):
        self.name = prmtr_name
        self.column = list[self.name]
        index_of_prmtr_name = columns.index(prmtr_name)
        self.rus_name = rus_columns[index_of_prmtr_name]
        self.conf_table = list[list['planet_status'] == 'Confirmed'].copy()
        self.confirmed_planets_table_with_prmtr = self.conf_table.dropna(subset=[self.name])

    def waffle(self):

        waffle_plot_width = 16
        waffle_plot_height = 9
        classes = self.confirmed_planets_table_with_prmtr['name']
        values = self.confirmed_planets_table_with_prmtr[self.name]

        def waffle_plot(classes, values, height, width, colormap):
            class_portion = [float(v) / sum(values) for v in values]
            total_tiles = width * height
            tiles_per_class = [round(p * total_tiles) for p in class_portion]
            plot_matrix = np.zeros((height, width))

            class_index = 0
            tile_index = 0

            for col in range(waffle_plot_width):
                for row in range(height):
                    tile_index += 1

                    if tile_index > sum(tiles_per_class[0:class_index]):
                        class_index += 1
                    plot_matrix[row, col] = class_index

            fig = plt.figure()
            plt.matshow(plot_matrix, cmap=colormap)
            plt.colorbar()
            ax = plt.gca()
            ax.set_xticks(np.arange(-.5, (width), 1), minor=True)
            ax.set_yticks(np.arange(-.5, (height), 1), minor=True)
            ax.grid(which='minor', color='w', linestyle='-', linewidth=2)
            legend_handles = []
            for i, c in enumerate(classes):
                lable_str = c + " (" + str(values[i]) + ")"
                color_val = colormap(float(i + 1) / len(classes))
                legend_handles.append(mpatches.Patch(color=color_val, label=lable_str))

            plt.legend(handles=legend_handles, loc=1, ncol=len(classes),
                       bbox_to_anchor=(0., -0.1, 0.95, .10))
            plt.xticks([])
            plt.yticks([])

        waffle_plot(classes, values, waffle_plot_height, waffle_plot_width, plt.cm.coolwarm)
        plt.show()

print(Diagrams('log_g').waffle())
