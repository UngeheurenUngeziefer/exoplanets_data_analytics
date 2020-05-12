import matplotlib.pyplot as plt

from Exoplanets_basic_info import list


list = list.groupby('discovered').count()
list.reset_index(level=0, inplace=True)
print(list)

x = list['discovered']
y = list['name']
plt.bar(x, y, color='darkgray')
plt.xticks(x, rotation=75)
plt.xlabel('Год')
plt.ylabel('Количество открытых планет')
plt.title('Открытие экзопланет по годам')
plt.show()
