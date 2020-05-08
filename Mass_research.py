import pandas as pd

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

# Выясним какие планеты наикрупнейшие по массе, а также найдём наименьшие
# Посмотрим сколько значений массы планет у нас не пустые
empty_fields_mass = list['mass_jup'].isna().sum()               # empty fields 5607

# имортируем переменную количества всех планет
from Exoplanets_basic_info import all_opened_planets
filled_fields_mass = all_opened_planets - empty_fields_mass      # filled fields 1406

# получили количество заполненных полей массы планет
# теперь для адекватности результата оставим только подтверждённые планеты
confirmed_planets = list['planet_status'] == 'Confirmed'        # Series boolean
confirmed_planets_table = list[confirmed_planets]               # 4264 rows, таблица с подтверждёнными планетами

# нам нужно избавиться от пустых значений массы в таблице подтверждённых планет
confirmed_planets_table_with_mass = confirmed_planets_table.dropna(subset=['mass_jup'])     # 1238 таких планет

# далее оставим в таблице только столбец имени и массы
confirmed_planets_table_with_mass = (confirmed_planets_table_with_mass.loc[:, ['name', 'mass_jup']])

# создадим конвертер масс юпитера в земные массы
# mass_earth = mass_jup * 317.82838              # Юпитер больше Земли в 318 раз

# добавим поле массы в Землях и расстояние до планеты в таблицу
confirmed_planets_table_with_mass['mass_earth'] = confirmed_planets_table_with_mass['mass_jup'] * 317.82838
confirmed_planets_table_with_mass['distance'] = list['star_distance']
confirmed_planets_table_with_mass = confirmed_planets_table_with_mass.loc[:, ['name', 'distance', 'mass_earth', 'mass_jup']]
confirmed_planets_table_with_mass = confirmed_planets_table_with_mass.sort_values(by=['mass_jup'])
#print(confirmed_planets_table_with_mass)

def results_mass():
    results_mass = confirmed_planets_table_with_mass.loc[:, ['name', 'mass_earth', 'mass_jup']]
    print()
    print('Самые крупные по массе экзопланеты: \n {}'
          .format(results_mass.loc[:, ['name', 'mass_jup']]
                  .sort_values(by='mass_jup', ascending=False).head(5)))
    print()
    print('Самые мелкие по массе экзопланеты: \n {}'
          .format(results_mass.loc[:, ['name', 'mass_earth']]
                  .sort_values(by='mass_earth', ascending=True).head(5)))
    print()
    results_mass_filtered = results_mass[
        (results_mass['mass_earth'] < 1.3) &
        (results_mass['mass_earth'] > 0.8)]


    print('Ближе всего к Земле по массе: \n {}'
          .format(results_mass_filtered.loc[:, ['name', 'mass_earth']]
                  .sort_values(by='mass_earth', ascending=False)))

    less_mass = results_mass[(results_mass['mass_earth'] < 1)]
    more_mass = results_mass[(results_mass['mass_earth'] > 1)]

    print()
    print('Планет по массе крупнее Земли {}, меньше Земли {}\n'
          .format(more_mass['mass_earth'].count(), less_mass['mass_earth'].count()))
#results_mass()