import matplotlib.pyplot as plt
from Radius_research import confirmed_planets_table_with_radius


# создадим одноимённые переменные для диаграммы
name = confirmed_planets_table_with_radius['name']
distance = confirmed_planets_table_with_radius['distance']
radius_earth = confirmed_planets_table_with_radius['radius_earth']

# нарисуем диаграмму соотношения расстояния до планеты к её радиусу
plt.scatter(distance, radius_earth, s=radius_earth * 2, c=radius_earth, alpha=0.5)
plt.xlabel('Расстояние от Земли (парсек)')
plt.ylabel('Размер (в радиусах Земли)')
plt.title('Соотношение радиуса открытых экзопланет к расстоянию до них')
plt.colorbar()
plt.show()
