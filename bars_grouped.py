from Exoplanets_basic_info import list
import matplotlib.pyplot as plt
import numpy as np

list = list.dropna(how='any', subset=['discovered', 'radius_meas_type'])

x_var = 'discovered'
groupby_var = 'radius_meas_type'


df_agg = list.loc[:, [x_var, groupby_var]].groupby(groupby_var)
vals = [df[x_var].values.tolist() for i, df in df_agg]

plt.figure(figsize=(10,20))
colors = [plt.cm.Spectral(i/float(len(vals)-1)) for i in range(len(vals))]
n, bins, patches = plt.hist(vals, 30, stacked=True, density=False, color=colors[:len(vals)])

plt.legend({group: col for group, col in zip(np.unique(list[groupby_var]).tolist(), colors[:len(vals)])})
plt.title('Экзопланеты по типу измерения радиуса по годам', fontsize=22)
plt.xlabel(x_var)
plt.ylabel("Количество открытых планет")
plt.show()