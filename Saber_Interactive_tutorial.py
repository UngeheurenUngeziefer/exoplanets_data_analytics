import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import plotly.express as px

# открываем две страницы таблицы
# данные о прохождении игроками туториала
sheet_1 = pd.read_excel('Trainee_Analyst_Test_DataSet.xlsx', sheet_name='FirstEnter')
sheet_2 = pd.read_excel('Trainee_Analyst_Test_DataSet.xlsx', sheet_name='RetentionRate')

# проверим наличие пустых значений
# print(sheet_1.isnull().sum())     # 0 во всех полях
# print(sheet_2.isnull().sum())     # 0 во всех полях
# пустых значений нет

# переименуем столбцы без пробелов
sheet_1_names = ['PlayerUid', 'MaxAchievedStep', 'RefPlace']
sheet_1.set_axis(sheet_1_names, axis='columns', inplace=True)

# сколько людей выполнило каждый из шагов
# функция считающая количество данной цифры в столбце MaxAchievedStep
def num_of_max(num):
    step = sheet_1['MaxAchievedStep'] == num
    step = sheet_1[step]
    step = step['MaxAchievedStep'].count()
    return step

# переменные с количеством строк с цифрой в столбце MaxAchievedStep
num_of_0 = num_of_max(0)    # 269
num_of_1 = num_of_max(1)    # 158
num_of_2 = num_of_max(2)    # 28
num_of_3 = num_of_max(3)    # 27
num_of_4 = num_of_max(4)    # 28
num_of_5 = num_of_max(5)    # 16
num_of_6 = num_of_max(6)    # 90
num_of_7 = num_of_max(7)    # 22
num_of_8 = num_of_max(8)    # 554

# количество людей прошедших 0 шаг = всем строкам таблицы
# количество людей прошедших 1 шаг = всем строкам таблицы кроме содержащих 0
# количество людей прошедших 2 шаг = всем строкам таблицы кроме содержащих 0 и 1 и т. д.
all_rows = sheet_1['PlayerUid'].count()
step_0 = all_rows                       # 1192
step_1 = step_0 - num_of_0              # 923
step_2 = step_1 - num_of_1              # 765
step_3 = step_2 - num_of_2              # 737
step_4 = step_3 - num_of_3              # 710
step_5 = step_4 - num_of_4              # 682
step_6 = step_5 - num_of_5              # 666
step_7 = step_6 - num_of_6              # 576
step_8 = step_7 - num_of_7              # 554

# Рисуем воронку по количеству прошедших каждый уровень plot_1.png
# data = dict(
#     number=[step_0, step_1, step_2, step_3, step_4, step_5, step_6, step_7, step_8],
#     stage=['0', '1', '2', '3', '4', '5', '6', '7', '8'])
# fig = px.funnel(data, x='number', y='stage')
# fig.show()

# Отношение количества людей, прошедших отдельные шаги туториала к количеству людей, стартовавших туториал
step_by_started = {'num_by_step': [step_0 / all_rows * 100, step_1 / all_rows * 100, step_2 / all_rows * 100,
                                   step_3 / all_rows * 100, step_4 / all_rows * 100, step_5 / all_rows * 100,
                                   step_6 / all_rows * 100, step_7 / all_rows * 100, step_8 / all_rows * 100],
                   'y': [0, 1, 2, 3, 4, 5, 6, 7, 8]}
correlation_table = pd.DataFrame(data=step_by_started)

# Рисуем график соотношения plot_2.png
# f, ax = plt.subplots(1)
# plt.title('Соотношение количества людей, прошедших отдельные шаги туториала к стартовавшим туториал')
# plt.xlabel('Шаги туториала')
# plt.ylabel('Процент достигших шага туториала')
# plt.xticks(step_by_started['y'])
# plt.grid(axis='y')
# ax.bar(correlation_table['y'], correlation_table['num_by_step'])
# plt.show()

# Посчитать показатель Retention Day 1
# print(sheet_2.isnull().sum())
# пустых значений нет

# print(sheet_2['Registered'].drop_duplicates())
# у нас имеется только 3 дня: 10, 11 и 12 марта 2019 года

# создаём переменные день регистрации и день входа
reg_day = sheet_2['Registered']
enter_day = sheet_2['DateTime']

# создаём базу данных с столбцом retention_day который показывает спустя сколько дней человек зашёл
data = {'retention_day': enter_day - reg_day}
retention_day_table = pd.DataFrame(data=data)
# print(retention_day_table.head(30))

# выведем таблицу с количеством пользователей возвратившихся после каждого количества дней
retention_day_table['num_of_ret_days'] = retention_day_table.groupby('retention_day')['retention_day'].\
    transform('count')
retention_day_table = retention_day_table.drop_duplicates('num_of_ret_days').sort_values('retention_day')\
    .reset_index(drop=True)
# print(retention_day_table)

# перенесём цифры в таблицу и распечатаем воронку количества вернувшийхся plot_3.png
# data = dict(
#     retention_day=[0, 1, 2, 3, 4, 5],
#     num_of_people=[2037, 236, 186, 137, 167, 72])
# fig = px.funnel(data, x='retention_day', y='num_of_people')
# fig.show()

# создадим функцию считающую Retention Day X
def retention_day_x(x):
    num_of_returned_people = retention_day_table['num_of_ret_days'][x]
    current_retention_day = retention_day_table['retention_day'][x]
    num_of_all_registered = sheet_2['PlayerUid'].count()
# отношение количества людей, которые зашли в Х день после первого визита
# к общему количеству совершивших первый вход.
    retention_day = num_of_returned_people / num_of_all_registered
    return retention_day

retention_day_0 = retention_day_x(0)
retention_day_1 = retention_day_x(1)
retention_day_2 = retention_day_x(2)
retention_day_3 = retention_day_x(3)
retention_day_4 = retention_day_x(4)
retention_day_5 = retention_day_x(5)

# сделаем базу данных retention days и построим воронку
data = {'retention_day_index': [retention_day_0, retention_day_1, retention_day_2,
                          retention_day_3, retention_day_4, retention_day_5],
        'day': [0, 1, 2, 3, 4, 5]}
final_ret_day_table = pd.DataFrame(data=data)
# print(final_ret_day_table)

# выведем график показателей retention_day для каждого дня plot_4.png
f, ax = plt.subplots(1)
plt.xlabel('Прошло дней с момента регистрации')
plt.ylabel('Retention Day')
plt.grid(axis='y')
ax.plot(final_ret_day_table['day'], final_ret_day_table['retention_day_index'])
# plt.show()


