# global scope
x = "global x"

def function():
    # local scope
    x = "local x"

function()
print(x)    

####

x = "global x"

def function():
    x = "local x"
    print(x)

function()
  