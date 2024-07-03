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


    # instance methods

    def intro(self):
       print("Hi there! I am " + self.name)

    # instance methods   

    def calculatorAge(self):
       return 2024 - self.year


     # objects=instance

object1 = person('Ali', 1990)
object2 = person('Asya', 2000)

object1.intro()
object2.intro()


print(f"I am {object1.calculatorAge()} years old.")
print(f"I am {object2.calculatorAge()} years old.")
