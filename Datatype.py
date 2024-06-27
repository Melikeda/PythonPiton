name = "Melike"
surname = 'Kulahci'
age = 22

greeting = "My name is "+ name +" "+ surname + ' and I am '+ str(22) + " years old" #(str)data type conversion

length = len(greeting)

print(greeting)
print(greeting[4])
print(greeting[13])
print(greeting[-9])  #9th from last
print(len(greeting))
print(greeting[length-1])
print(greeting[2:5])  #2 to 5
print(greeting[3:])
print(greeting[:15])
print(greeting[1:40:3])  #3 by 3 from 1 to 40