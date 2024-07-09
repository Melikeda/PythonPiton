import matplotlib.pyplot as plt

competition_status ="Yes","No","Undecided"

status= [56,23,17]
colors= ["blue", "red","green"]

plt.pie(status, labels=competition_status, colors=colors, shadow=True, explode=(0.05,0.05,0.05), autopct="%1.1f%%")
plt.show()