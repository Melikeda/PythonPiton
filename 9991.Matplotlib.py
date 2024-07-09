import matplotlib.pyplot as plt
import numpy as np

x = [1,2,3,4]
y = [1,4,9,16
     ]
plt.plot(x,y, color="blue", linewidth="5")
plt.axis([0,5,0,20])

plt.title("Chart Title")
plt.xlabel("x Label")
plt.ylabel("y Label")

plt.show()