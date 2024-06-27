list = [1,2,3]
tuple = (1,"iki", 3)

print(type(list))
print(type(tuple))

print(list[2])
print(tuple[2])

list = ["merve", 'esma']
print(list)
tuple = ("melike", 'eda')
print(tuple)

list[0]="canım"
print(list)

'''tuple[0]="benim"
print(tuple)''' #This is not happens in tuple!

names= ("elif", "mehmet",)+ tuple
print(names)
