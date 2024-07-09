import matplotlib.pyplot as plt
import numpy as np


t = np.linspace(0, 2*np.pi, 1000)
x = 16 * np.sin(t)**3
y = 13 * np.cos(t) - 5 * np.cos(2*t) - 2 * np.cos(3*t) - np.cos(4*t)


plt.figure(figsize=(8, 6), facecolor='pink')
plt.plot(x, y, color='red', linewidth=4)
plt.fill(x, y, 'red', alpha=1)  # 'alpha' indicates the level of transparency (0: fully transparent, 1: opaque)


plt.title('Heart Shape Function')
plt.axis('equal')  # Ensures equal scale of axes
# Opens the grid, making it easier to visualize the background
#plt.grid(True, color='black', linestyle='--', linewidth=0.5,)

plt.show()
