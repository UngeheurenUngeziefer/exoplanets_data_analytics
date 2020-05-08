import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.cm as cm
import numpy as np
import scipy
import random
from Exoplanets_basic_info import list, all_opened_planets
from Mass_research import confirmed_planets, confirmed_planets_table

# выведем статистику для радиусов планет
empty_fields_radius = list['radius'].isna().sum()                   # empty fields 1420
filled_fields_radius = all_opened_planets - empty_fields_radius     # filled fields 5593

# оставим только подтверждённые планеты
confirmed_planets_table_with_radius = confirmed_planets_table.dropna(subset=['radius'])     # 3137 таких планет

# далее оставим в таблице только столбец имени и радиуса
confirmed_planets_table_with_radius = (confirmed_planets_table_with_radius.loc[:, ['name', 'radius']])

# добавим поле радиуса в Землях и расстояние до планеты в таблицу
confirmed_planets_table_with_radius['radius_earth'] = confirmed_planets_table_with_radius['radius'] * 69911 / 6371.2
confirmed_planets_table_with_radius['distance'] = list['star_distance']
confirmed_planets_table_with_radius = confirmed_planets_table_with_radius.loc[:, ['name', 'distance', 'radius', 'radius_earth']]
confirmed_planets_table_with_radius = confirmed_planets_table_with_radius.sort_values(by=['radius'])
confirmed_planets_table_with_radius = confirmed_planets_table_with_radius.dropna()              # 2037

def results_radius():
    results_radius = confirmed_planets_table_with_radius.loc[:, ['name', 'radius_earth', 'radius']]
    print()
    print('Самые крупные по радиусу экзопланеты (в радиусах Юпитера): \n {}'
          .format(results_radius.loc[:, ['name', 'radius']]
                  .sort_values(by='radius', ascending=False).head(5)))
    print()
    print('Самые мелкие по радиусу экзопланеты (в массах Земли): \n {}'
          .format(results_radius.loc[:, ['name', 'radius_earth']]
                  .sort_values(by='radius_earth', ascending=True).head(5)))
    print()
    results_radius_filtered = results_radius[
        (results_radius['radius_earth'] < 1.01) &
        (results_radius['radius_earth'] > 0.99)]


    print('Ближе всего к Земле по радиусу: \n {}'
          .format(results_radius_filtered.loc[:, ['name', 'radius_earth']]
                  .sort_values(by='radius_earth', ascending=False)))

    less_radius = results_radius[(results_radius['radius_earth'] < 1)]
    more_radius = results_radius[(results_radius['radius_earth'] > 1)]

    print()
    print('Планет по радиусу крупнее Земли {}, меньше Земли {}\n'
          .format(more_radius['radius_earth'].count(), less_radius['radius_earth'].count()))
#results_radius()
