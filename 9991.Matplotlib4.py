import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0,2,100)

plt.plot(x, x, label="lineer", color="red")
plt.plot(x, x**2, label="quadratic", color="pink")
plt.plot(x, x**3, label="cubic", color="purple")

plt.title("Simple Plot")
plt.xlabel("x Label")
plt.ylabel("y Label")

plt.legend()

plt.show()