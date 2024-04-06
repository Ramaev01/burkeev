import matplotlib.pyplot as plt
import numpy as np
import math

x = np.linspace(-3*(math.pi),3*(math.pi),250)
y = np.random.normal(loc=1, scale=4, size=len(x)) * 20

plt.figure(figsize=(10,5))
plt.scatter(x, y)

plt.scatter(x, y, s=300, marker='s', c='violet', lw=2, edgecolor='black', hatch='**')
plt.title(
 label='$sin(x)$ with random noise', # Заголовок
 fontsize=20 # Размер шрифта
)
plt.xlabel('x range', fontsize=18)
plt.ylabel('y range', fontsize=18)
plt.tick_params(labelsize=16)
plt.xticks(
 ticks=np.arange(-10, 11, 2) # Нужные значения по оси x
)
plt.yticks(
 ticks=np.arange(-1.5, 2,0.5), # Значения по оси y будут заменены на подкписи,
 # Которые будут на этих позициях
 labels=['можно', 'написать', 'все', 'что', 'хочется', 'вообще', 'все ='][::-1]
)

plt.show()