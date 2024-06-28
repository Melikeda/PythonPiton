thisList = ["apple", "banana", "orange", "apple", "orange"]
thisLİST = ["tomato", " potato"]

print(thisList)
print(type(thisList))

#Change List Items

thisList[2:3] = ["blackcurrant", "watermelon"]
print(thisList)

thisList[3:6]  = ["watermelon"]
print(thisList)

# Add List Items

thisList.insert(2, "cherry")  #insert
print(thisList)

thisList.append("apple")  #append
print(thisList)

thisList.extend(thisLİST)  #extend
print(thisList)

#Remove List Items

thisList.remove("tomato")  #remove
print(thisList)

thisList.pop(0)  #pop
print(thisList)

del thisList[0]  #del
print(thisList)

#thisList.clear()


########


list2 = ["map", 40, "flower"]

print(list2)
print(type(list2))

#Change List Items

print(list2[-1])
print(list2[:3])
print(list2[-2:-1])


if "map" in list2:
    print( "Yes, 'map' is in list2" )

# Loop Lists

#For Loop

for x in list2:
    print(x)

#While Loop

i = 0
while i < len(list2):
    print(list2[i])
    i = i+1
    

list3 = [100, 4, 65, 33, 1]   

#Sort List Alphanumerically

list3.sort()
print(list3)

#Copy Lists

mylist = list3.copy()
print(mylist)

mylist =list(list3)
print(mylist)

#Join Two Lists

list4 = list3 + mylist
print(list4)


 

