import matplotlib.pyplot as plt
import numpy as np
import math

x = (-5*(math.pi), 5*(math.pi), 10**7)
y = np.random.standard_cauchy(size=10**7)
y1 = np.random.normal(loc = -10,scale=7, size=None)
y2 = np.random.normal(loc = 10,scale = 5, size=None)
y3 = np.random.normal(loc = 25,scale = 10, size=None)

plt.hist(x, y,
         range=(0,5),
         bins=100,
         density=True
         )
plt.show()