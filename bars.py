from Exoplanets_basic_info import list
import matplotlib.pyplot as plt
from molecules import molecules_df

x = molecules_df['molecule']
y = molecules_df['planets_have']
plt.bar(x, y, color='royalblue')
plt.xticks(x, rotation=75)
plt.yticks(y)
plt.xlabel('Молекулы')
plt.ylabel('Количество экзопланет на которых найдена')
plt.title('Молекулы по количеству планет на которых они обнаружены')
plt.grid(axis=y)
plt.show()
