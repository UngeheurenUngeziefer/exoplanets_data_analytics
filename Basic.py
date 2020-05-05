import pandas as pd
import numpy as np

list_of_planets = pd.read_csv('exoplanets_catalog.csv', encoding="Windows-1251",
                              names=['Имя', 'Статус', 'Масса', 'Радиус', 'Угловая дистанция',
                                     'Большая полуось', 'Открытие', 'Опубликованность', 'Тип обнаружения',
                                     'Альтернативное имя', 'Обнаруженные молекулы', 'Звезда-хост',
                                     'Расстояние до звезды-хоста (парсек)', 'Масса звезды', 'Радиус звезды',
                                     'Расстояние до звезды-хоста (световых лет)'])

#                        0       1        2                       3
# print(list_of_planets[['Имя', 'Масса', 'Радиус', 'Расстояние до звезды-хоста (световых лет)']])

# функция сортировки по стобцу, отображает имя и столбец по которому идёт сортировка, первые 5
def sorting_planets(name1, name2):
    list_of_planets_sorted = list_of_planets.sort_values([name2], ascending=False)
    list_of_planets_sorted.head()
    print(list_of_planets_sorted.head()[[name1, name2]])



print('Самые крупные планеты по массе: ')
sorting_planets('Имя', 'Масса')
print()

print('Самые крупные планеты по размеру: ')
sorting_planets('Имя', 'Радиус')
print()

print('Самые близике к Земле экзопланеты: ')
list_of_planets_sorted = list_of_planets.sort_values(['Расстояние до звезды-хоста (парсек)'])
list_of_planets_sorted.head()
print(list_of_planets_sorted.head()[['Имя', 'Расстояние до звезды-хоста (парсек)']])
print()

print('Самые далёкие от Земли экзопланеты: ')
sorting_planets('Имя', 'Расстояние до звезды-хоста (парсек)')
print()






