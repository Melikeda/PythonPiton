import random

result = random.random() # 0.0 1.0
result = random.uniform(10, 100)
result = int(random.uniform(10, 100))
result = random.randint(1,100)

print(result)


########


import random 

names = ["Sea", "Beach", "Night", "Sun"]

result = names[random.randint(0, len(names)-1)]

print(result)
