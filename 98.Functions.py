def changename(n):
    n = "Ada"

name = "İdil"

changename(name)
print(name)


def changecity(c):
    c[0] = "Mersin"

city = ["Çorum", "Antalya", "Muğla", "İzmir", "Balikesir", " Çanakkale", "Bursa"]     

changecity(city)
print(city)


def add(a, b, c = 0):
    return sum((a,b))

print(add(10,20))
print(add(10,20,30))


def addtwo(*params):
    return sum((params))

print(addtwo(1,2,3,4,5,6))