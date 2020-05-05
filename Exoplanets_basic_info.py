# omega - Аргумент перицентра

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# открываем подготовленную базу экзопланет, универсальная кодировка, без имён столбцов
list = pd.read_csv('exoplanet.eu_catalog.csv', encoding="Windows-1251", header=None)


# создаём список красивых имён столбцам
# назначаем имена столбцам таблицы
columns = ['name', 'planet_status', 'mass_jup', 'radius', 'orbital_period',	'semi_major_axis', 'eccentricity',
           'inclination', 'angular_distance', 'discovered', 'updated', 'omega', 'epoch_of_periastron',
           'conjonction_date', 'primary_transit', 'secondary_transit', 'lambda_angle', 'impact_parameter',
           'velocity_semiamplitude', 'temp_calculated', 'temp_measured', 'hot_point_lon', 'geometric_albedo',
           'log_g', 'publication', 'detection_type', 'mass_detection_type', 'radius_detection_type', 'alternate_names',
           'molecules',	'star_name', 'right_ascention', 'declination', 'mag_v',	'mag_i', 'mag_j', 'mag_h', 'mag_k',
           'star_distance', 'star_metallicity', 'star_mass', 'star_radius', 'star_spectral_type', 'star_age',
           'star_effective_temp', 'star_detected_disc', 'star_magnetic_field', 'star_alternate_names']
list.set_axis(columns, axis='columns', inplace=True)

# находим сумму пустых значений для каждого столбца
empty_values_summ = list.isnull().sum()

# создаём новую таблицу с столбцом пустых значений и столбцом имени значений
data_empty_fields = {'values': columns, 'empty_fields': empty_values_summ}
empty_values_table = pd.DataFrame(data=data_empty_fields)

# группируем по имени значения, находим медианное значение, сортируем по количеству пустых
# выводим в виде столбчатой диаграммы, поворачиваем названия оси х на 90 градусов
# название располагаем ближе к верху области диаграммы и показываем её
# empty_values_table.groupby(['values']).median().sort_values('empty_fields').plot.bar()
# plt.xticks(rotation=90)
# plt.suptitle('Распределение пустых значений в информации о экзопланетах', x=0.5, y=0.99)
# plt.show()

# количество всех планет методом count()
all_opened_planets = list['name'].count()                                                       # 7013

# определим количество звёзд у которых найдены планеты
# узнаем сколько пропущенных и заполненных значений
# узнаем количество звёзд имеющих открытые планеты
star_name_empty_fields = list['star_name'].isna().sum()                                         # 59
star_name_filled_fields = list['star_name'].count()                                             # 6954
star_name_unique = list['star_name'].drop_duplicates().reset_index(drop=True).count()           # 5596
star_name_unique_table = list['star_name'].drop_duplicates().reset_index(drop=True)

# выясним сколько звёзд имеют больше всего планет
# таблица с количеством планет у каждой звезды
list.dropna(subset=['star_name'], inplace=True)
list['num_of_all_planets'] = list.groupby('star_name')['star_name'].transform('count')
stars_by_num_of_all_planets_table = list.loc[:, ['star_name', 'num_of_all_planets']].drop_duplicates()
# print(stars_by_num_of_all_planets_table)

# таблица с количеством планет по системам
list['num_of_count'] = list.groupby('num_of_all_planets')['num_of_all_planets'].transform('count')
num_of_sys_by_all_planets = list.loc[:, ['num_of_all_planets', 'num_of_count']].drop_duplicates()
num_of_sys_by_all_planets['stars_with_planets'] = num_of_sys_by_all_planets['num_of_count'] \
                                                  // num_of_sys_by_all_planets['num_of_all_planets']
num_of_sys_by_all_planets = num_of_sys_by_all_planets.sort_values(by=['num_of_all_planets'])
# print(num_of_sys_by_all_planets.loc[:, ['num_of_all_planets', 'stars_with_planets']])


# столбцы количество систем и количество планет
num_of_sys = num_of_sys_by_all_planets['stars_with_planets']
num_of_planets = num_of_sys_by_all_planets['num_of_all_planets']

# создаём диаграмму со всеми планетами, статистика по звёздным системам
# fig, ax = plt.subplots()
# width = 0.75
# ind = np.arange(len(num_of_sys))
# ax.barh(ind, num_of_sys, width, color="c")
# ax.set_yticks(ind+width/2)
# ax.set_yticklabels(num_of_planets, minor=False)
# plt.title('Количество звёзд с планетами')
# plt.xlabel('Количество звёзд')
# plt.ylabel('Разрядность системы (открыто планет в системе)')
# for i, v in enumerate(num_of_sys):
#     ax.text(v + 3, i + .25, str(v), color='black', fontweight='normal')
# plt.show()

# сделаем такую же диаграмму с количеством планет
# num_of_all_planets = num_of_sys_by_all_planets['num_of_all_planets']
# num_of_count = num_of_sys_by_all_planets['num_of_count']
#
# fig, ax = plt.subplots()
# width = 0.75
# ind = np.arange(len(num_of_count))
# ax.barh(ind, num_of_count, width, color="r")
# ax.set_yticks(ind+width/2)
# ax.set_yticklabels(num_of_all_planets, minor=False)
# plt.title('Распределение планет по разрядности их звёздных систем')
# plt.xlabel('Количество планет')
# plt.ylabel('Разрядность системы (открыто планет в системе)')
# for i, v in enumerate(num_of_count):
#     ax.text(v + 3, i + .25, str(v), color='black', fontweight='normal')
# plt.show()


# находим количество однопланетных систем и многопланетных систем
stars_with_one_planet = num_of_sys_by_all_planets.loc[0, 'num_of_count']      # 4688
stars_with_multiple_planets = star_name_unique - stars_with_one_planet        # 908

# print()
# print('Всего предполагаемых экзопланет: {}'.format(all_opened_planets))
# print()
# print('Количество звёзд с предполагаемыми экзопланетами: {}'.format(star_name_unique))
# print()
# print('Количество звёзд с предполагаемой одной открытой планетой: {}'.format(stars_with_one_planet))
# print()
# print('Количество звёзд с предполагаемо многими планетами: {}'.format(stars_with_multiple_planets))
# print()
# print('Количество планет состоящих в многопланетных системах: {}'.format(num_of_sys_by_all_planets['num_of_count'].sum()
#                                                                          - stars_with_one_planet))
# посчитаем среднее количество планет у звезды на данный момент
# для этого вводим переменную = количество заполненных полей имя звезды
# (оно = количеству планет у которых известна звезда) - уникальные значения имени звезды
# mid_num_of_planets_by_star = star_name_filled_fields / star_name_unique
# print('Среднее количество планет у звезды на май 2020 года: {:.2f}'.format(mid_num_of_planets_by_star))
