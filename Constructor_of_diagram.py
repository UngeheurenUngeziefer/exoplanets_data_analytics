# напишем класс, который будет рисовать нужную диаграмму на основе полученных параметров
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
from pywaffle import Waffle
import warnings; warnings.filterwarnings(action='once')
from Exoplanets_basic_info import list, columns, rus_columns

class Diagrams:
    def __init__(self, prmtr_name):
        self.name = prmtr_name
        self.column = list[self.name]
        index_of_prmtr_name = columns.index(prmtr_name)
        self.rus_name = rus_columns[index_of_prmtr_name]
        self.conf_table = list[list['planet_status'] == 'Confirmed'].copy()
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

    def diverging_bars(self, title):
        x = list[list['planet_status'] == 'Confirmed'].loc[:, [self.name, 'name']].dropna(subset=[self.name])
        x['column_z'] = (x.loc[:, [self.name]] - x.loc[:, [self.name]].mean()) / x.loc[:, [self.name]].std()
        # x['column_z'] = x.loc[:, [self.name]]
        x['colors'] = ['red' if x < 0 else 'green' for x in x['column_z']]
        x.sort_values('column_z', inplace=True)
        x.reset_index(inplace=True)

        plt.figure(figsize=(14, 10), dpi=80)
        plt.hlines(y=x.index, xmin=0, xmax=x.column_z,
                   color=x.colors, alpha=0.4, linewidth=5)

        plt.gca().set(ylabel=self.rus_name, xlabel='Разница')
        plt.yticks(x.index, x.name, fontsize=12)
        plt.title(title, fontdict={'size': 20})
        plt.grid(linestyle='--', alpha=0.5)
        plt.show()

    def pie(self, title):
        self.conf_table['counter'] = self.conf_table.groupby(self.name)[self.name].transform('count')
        self.conf_table = self.conf_table.drop_duplicates(subset=[self.name]).dropna(subset=['counter'])
        self.conf_table = self.conf_table.sort_values(by=[self.name])

        fig, ax = plt.subplots(figsize=(6, 3), subplot_kw=dict(aspect="equal"))
        data = self.conf_table['counter']
        name_of_prmtr = self.conf_table[self.name]

        def func(pct, allvals):
            absolute = int(pct / 100. * np.sum(allvals))
            return "{:.1f}%\n({})".format(pct, absolute)

        wedges, texts, autotexts = ax.pie(data, autopct=lambda pct: func(pct, data),
                                          textprops=dict(color="w"))
        ax.legend(wedges, name_of_prmtr, title='Легенда',
                  loc="center left", bbox_to_anchor=(1, 0, 0.5, 1))
        plt.setp(autotexts, size=8, weight="light")
        ax.set_title(title)
        plt.show()

    def stripplot(self, yprmtr, title):
        self.conf_table = self.conf_table.dropna(subset=[self.name, yprmtr])

        fig, ax = plt.subplots(figsize=(16, 10), dpi=80)
        sns.stripplot(self.conf_table[self.name], self.conf_table[yprmtr],
                      jitter=0.25, size=8, ax=ax, linewidth=.5)
        plt.title(title, fontsize=22)
        plt.xlabel(self.rus_name)
        plt.xticks(rotation=90)
        plt.ylabel(rus_columns[columns.index(yprmtr)])
        plt.show()

    def waffle(self, title, rows):

        df = self.conf_table.groupby(self.name).size().reset_index(name='counts')
        n_categories = df.shape[0]
        colors = [plt.cm.inferno_r(i / float(n_categories)) for i in range(n_categories)]

        plt.figure(
            FigureClass=Waffle,
            plots={
                '111': {
                    'values': df['counts'],
                    'labels': ["{} ({:.2f})".format(n[0], n[1]) for n in df[[self.name, 'counts']].itertuples()],
                    'legend': {'loc': 'upper center', 'bbox_to_anchor': (0.5, -0.02), 'fancybox': True,
                               'ncol': n_categories // rows // 2, 'fontsize': 12},
                    'title': {'label': title, 'loc': 'center', 'fontsize': 18}
                },
            },
            rows=rows,
            colors=colors,
            figsize=(16, 9)
        )
        plt.show()

    def angles_polar(self, title):
        # берём все углы подтверждённых экзопланет с непустыми значениями угла
        # создаём список списков углов, делаем из него список углов
        series_all_angles = self.confirmed_planets_table_with_prmtr.loc[:, [self.name]]
        list_of_lists_angles = series_all_angles.values.tolist()
        flat_list = []
        for sublist in list_of_lists_angles:
            for item in sublist:
                flat_list.append(item)

        theta = np.radians(np.array(flat_list))
        radius = np.ones(theta.size)  # радиусы одинакового размера
        ax = plt.subplot(111, polar=True)
        ax.set_yticklabels([])  # убрать radial ticks
        for t, r in zip(theta, radius):
            ax.plot((0, t), (0, r))
        ax.set_title(title)
        plt.show()

# print(Diagrams('orbital_period').bubbles_prmtr_by_prmtr('Соотношение орбитального периода к массе планеты', 'mass_jup'))
# print(Diagrams('radius').ratio_with_labels_horizontal('Соотношение орбитального периода и массы экзопланеты', 'forestgreen', 'orbital_period', 'bar'))
# print(Diagrams('orbital_period').diverging_bars('Орбитальный период экзопланет (в днях)'))
print(Diagrams('orbital_period').stripplot('name', 'Соотношение орбитального периода и массы экзопланеты'))
# print(Diagrams('radius').waffle('Радиус экзопланет', 50))
# print(Diagrams('mass_jup').pie('Экзопланеты по массе'))
# print(Diagrams('mass_jup').angles_polar('Склонение'))

