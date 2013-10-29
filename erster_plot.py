# erster Plot
# Vektor in Python plotten

import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0,2*np.pi,100)
y = np.sin(x)

plt.plot(x,y)
# plt.savefig('erster_plot.png')
plt.show()