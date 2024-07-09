import matplotlib.pyplot as plt

plt.bar([0.25,1.25,2.25,3.25,4.25],[40,20,70,10,50], label="BMW", width=.5, color="purple")
plt.bar([0.75,1.75,2.75,3.75,4.75],[80,60,10,30,10], label="AUDI", width=.5, color="black")

plt.legend()
plt.xlabel("Day")
plt.ylabel("km")
plt.title("Vehicle information")

plt.show()