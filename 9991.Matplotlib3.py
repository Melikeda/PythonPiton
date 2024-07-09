import matplotlib.pyplot as plt
import numpy as np

x = [1,2,3,4,5]
y = [1,4,9,16,25]


plt.plot(x,y, "o--r")
plt.axis([1,5,1,20])

plt.title("Chart Title")
plt.xlabel("x Label")
plt.ylabel("y Label")

plt.show()