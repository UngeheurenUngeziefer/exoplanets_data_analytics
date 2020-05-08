import matplotlib.pyplot as plt
from Mass_research import confirmed_planets_table_with_mass

# сделаем таблицу с заполненными значениями расстояния
confirmed_planets_table_with_mass = confirmed_planets_table_with_mass.dropna()       # 937

# создадим одноимённые переменные для диаграммы
name = confirmed_planets_table_with_mass['name']
distance = confirmed_planets_table_with_mass['distance']
mass_earth = confirmed_planets_table_with_mass['mass_earth']

# нарисуем диаграмму соотношения расстояния до планеты к её массе
plt.scatter(distance, mass_earth, s=mass_earth / 75, c=mass_earth, alpha=0.5)
plt.xlabel('Расстояние от Земли (парсек)')
plt.ylabel('Масса (в массах Земли)')
plt.title('Соотношение массы открытых экзопланет к расстоянию до них')
plt.show()
