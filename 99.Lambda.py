def square(num):
    return num ** 2

result = square(2)
print(result)


# map expression

def squaretwo(num):
    return num ** 2

numbers = [3,4,5,6]

result = list(map(square, numbers))
print(result)


# lambda expression

def checkeven(num):
    return num%2==0

numbers = [1,2,3,4,5,6,7,8,9,10]

result = list(filter(lambda num: num%2==0, numbers))

print(result)