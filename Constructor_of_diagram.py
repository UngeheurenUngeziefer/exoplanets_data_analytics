# напишем класс, который будет рисовать нужную диаграмму на основе полученных параметров
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

    def bubbles_prmtr_by_prmtr(self, title, second_prmtr):
        self.conf_table = self.conf_table.dropna(subset=[second_prmtr, self.name])
        first_prmtr_column = self.confirmed_planets_table_with_prmtr[second_prmtr]
        second_prmtr_column = self.confirmed_planets_table_with_prmtr[self.name]
        plt.scatter(second_prmtr_column, first_prmtr_column, s=first_prmtr_column,
                    c=first_prmtr_column, alpha=0.5)
        sec_index = columns.index(second_prmtr)
        plt.xlabel('{}'.format(self.rus_name))
        plt.ylabel('{}'.format(rus_columns[sec_index]))
        plt.title('{}'.format(title))
        plt.colorbar()
        plt.show()

    def ratio_with_labels_horizontal(self, title, color, xprmtr, dtype):
        # confirmed_planets_table = self.conf_table
        # таблица с заполненными столбацами х и у
        self.conf_table = self.conf_table.dropna(subset=[xprmtr, self.name])
        self.conf_table['count_of_y'] = self.conf_table.groupby(self.name)[self.name].transform('count')
        self.conf_table.loc[:, [self.name, 'count_of_y']].drop_duplicates().sort_values(by=[self.name])
        self.conf_table = self.conf_table.drop_duplicates(subset=[xprmtr])
        y = self.conf_table['count_of_y']
        x = self.conf_table[xprmtr]

        x_index = columns.index(xprmtr)
        plt.xlabel('{}'.format(rus_columns[x_index]))
        plt.ylabel('{}'.format(self.rus_name))

        plt.xticks(x, rotation=75)
        plt.yticks(label=self.rus_name, fontweight='light')
        plt.title(title)

        if dtype == 'bar':
            plt.bar(x, y, color=color)
        elif dtype == 'scatter':
            plt.scatter(x, y, color=color)
        elif dtype == 'plot':
            plt.plot(x, y, color=color)
        plt.show()

    def diverging_bars(self, bars):
        self.conf_table.dropna(subset=[bars])
        x = self.conf_table.loc[:, [bars]]
        self.conf_table['bars_z'] = (x - x.mean()) / x.std()
        self.conf_table['colors'] = ['red' if x < 0 else 'green' for x in self.conf_table['bars_z']]
        self.conf_table.sort_values('bars_z', inplace=True)
        # self.conf_table.reset_index(inplace=True)

        plt.figure(figsize=(14, 10), dpi=80)
        plt.hlines(y=self.conf_table.index, xmin=0, xmax=self.conf_table.bars_z,
                   color=self.conf_table.colors, alpha=0.4, linewidth=5)

        plt.gca().set(ylabel='Название', xlabel='Сравнение')
        plt.yticks(self.conf_table[bars], self.conf_table['name'], fontsize=12)
        plt.title('Имя таблицы', fontdict={'size': 20})
        plt.grid(linestyle='--', alpha=0.5)
        plt.show()


prmtr = Diagrams('lambda_angle')
# print(prmtr.bubbles_prmtr_by_prmtr('соотношение', 'discovered'))
# print(prmtr.ratio_with_labels_horizontal('Количество открытых в год',
#                                          'forestgreen', 'discovered', 'scatter'))
print(prmtr.diverging_bars('lambda_angle'))
