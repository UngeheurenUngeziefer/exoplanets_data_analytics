import matplotlib.pyplot as plt
import pandas as pd
import matplotlib.cm as cm
import numpy as np

x = np.random.random(10)
y = np.random.random(10)

# Plot...
plt.scatter(x, y, c=y, s=500)
plt.gray()

plt.show()