from csv import reader, writer

# создадим функцию, которая считает расстояние до экзопланеты и переводит его в световые года
# def apprx_distance_in_light_years(planet_name, semi_major_axis, angular_dist_arcsec):
#     if not semi_major_axis and not angular_dist_arcsec:
#         print('Отсутствуют оба значения')
#     elif not semi_major_axis and angular_dist_arcsec is not None:
#         print('Отсутствует значение большой полуоси')
#     elif semi_major_axis is not None and not angular_dist_arcsec:
#         print('Отсутствует значение углового расстояния')
#     else:
#         distance_parsec = float(semi_major_axis) / float(angular_dist_arcsec)
#         apprx_distance_in_light_years = distance_parsec * 3.26156
#         print('{:.2f}'.format(apprx_distance_in_light_years))

# сделаем цикл, вычисляющий расстояние и печатающий его для каждой экзопланеты
# for num in range(1, len(list_of_planets)):
#     apprx_distance_in_light_years(list_of_planets[num][0], list_of_planets[num][5], list_of_planets[num][4])


# откроем и прочитаем данные как список списков
with open('exoplanets_catalog.csv', 'r') as read_ec:
    csv_reader = reader(read_ec)
    list_of_planets = list(csv_reader)

# создадим функцию, которая считает расстояние до экзопланеты и переводит его в световые года
def apprx_distance_in_light_years(planet_name, semi_major_axis, angular_dist_arcsec):
    if not semi_major_axis and not angular_dist_arcsec:
        print('Для {} отсутствуют значения углового расстояния и размера большой полуоси'.format(planet_name))
    elif not semi_major_axis and angular_dist_arcsec is not None:
        print('Расстояние до {} неизвестно, отсутствует значение большой полуоси'.format(planet_name))
    elif semi_major_axis is not None and not angular_dist_arcsec:
        print('Расстояние до {} неизвестно, отсутствует значение углового расстояния'.format(planet_name))
    else:
        distance_parsec = float(semi_major_axis) / float(angular_dist_arcsec)
        apprx_distance_in_light_years = distance_parsec * 3.26156
        print('Расстояние до {}: {:.2f} световых лет'.format(planet_name, apprx_distance_in_light_years))

# сделаем цикл, вычисляющий расстояние и печатающий его для каждой экзопланеты
for num in range(1, len(list_of_planets)):
    apprx_distance_in_light_years(list_of_planets[num][0], list_of_planets[num][5], list_of_planets[num][4])


