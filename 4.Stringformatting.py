name = "Melike"
surname = 'Kulahci'
age = 22

print('My name is {} {}'.format(name, surname))
print('My name is {0} {1}'.format(name, surname))
print('My name is {1} {0}'.format(name, surname))
print('My name is {s} {n}'.format(n=name, s=surname))

result = 200/700

print('Result is {}'.format(result))
print('Result is {r:1.3}'.format(r=result))

print(f'My name is {name} {surname}') # f string

