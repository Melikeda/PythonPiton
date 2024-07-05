from datetime import datetime

now =datetime.now() # now = datetime.today() is same # object

result = datetime.now()
result = datetime.now().year
result = datetime.now().month
result = datetime.now().hour
result = datetime.now().second

result = datetime.ctime(now)
result = datetime.strftime(now,'%Y')
result = datetime.strftime(now,'%x')
result = datetime.strftime(now,'%d')
result = datetime.strftime(now,'%B %A')


print(result)

######

t = '16 March 2024'
day, month, year = t.split()
print(day)
print(month)
print(year)

####

d = '01 March 2002 Hour 23:32:40'
dt = datetime.strptime(d, '%d %B %Y Hour %H:%M:%S')

print(dt)