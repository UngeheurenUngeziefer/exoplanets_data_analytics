import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import warnings; warnings.filterwarnings(action='once')
from Exoplanets_basic_info import list, columns, rus_columns

class Diagrams:
    def __init__(self, prmtr_name):
        self.name = prmtr_name
        self.column = list[self.name]
        index_of_prmtr_name = columns.index(prmtr_name)
        self.rus_name = rus_columns[index_of_prmtr_name]
        self.conf_table = list[list['planet_status'] == 'Confirmed']
        self.confirmed_planets_table_with_prmtr = self.conf_table.dropna(subset=[self.name])


    def diverging_bars(self, column):
        self.conf_table = list[list['planet_status'] == 'Confirmed']

        df = pd.read_csv("https://github.com/selva86/datasets/raw/master/mtcars.csv")
        x = df.loc[:, ['mpg']]
        df['mpg_z'] = (x - x.mean())/x.std()
        df['colors'] = ['red' if x < 0 else 'green' for x in df['mpg_z']]
        df.sort_values('mpg_z', inplace=True)
        df.reset_index(inplace=True)

        # Draw plot
        plt.figure(figsize=(14,10), dpi= 80)
        plt.hlines(y=df.index, xmin=0, xmax=df.mpg_z, color=df.colors, alpha=0.4, linewidth=5)

        # Decorations
        plt.gca().set(ylabel='$Model$', xlabel='$Mileage$')
        plt.yticks(df.index, df.cars, fontsize=12)
        plt.title('Diverging Bars of Car Mileage', fontdict={'size':20})
        plt.grid(linestyle='--', alpha=0.5)
        plt.show()

prmtr = Diagrams('lambda_angle')
print(prmtr.diverging_bars('lambda_angle'))