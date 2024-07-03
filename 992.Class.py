    # class
class person:
    pass

    # class atributes

    address = "No information"

    #constructor

    def __init__(self, name, year):
        
    # object atributes

     self.name = name
     self.year = year


    #methods


     # objects=instance

object1 = person('Ali', 1990)
object2 = person('Asya', 2000)

    # updating

object1.name = "Mehmet"
object2.address = "İzmir"

print(f" name = {object1.name} year = {object1.year} address = {object1.address}")
print(f" name = {object2.name} year = {object2.year} address = {object2.address}")

print(object1)
print(object2)

    