def sayHello():
    print("Hello!")

sayHello()    

# with parameter

def sayHi(name):
    print("Hi! " + name)

sayHi('Melike')    


def sayHİ(name = 'user'):
    print("Hi! " + name)

sayHİ('Eda')  
sayHİ()  

# with return 

def myfunction():
    return "Hi!"

msg = myfunction()

print(msg)

# sum of two numbers

def total(num1, num2):
    return num1 + num2

result = total(10,20)

print(result)

# age calculation

def agecalculator(birthyear):
    return 2024 - birthyear

age = agecalculator(2007)

print(age)