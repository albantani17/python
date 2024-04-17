#Keyword-Only Arguments
def funct(*, x):
    print(x)

funct(x = 3)

#Without the *, you are allowed to use positionale arguments even if the function expects keyword arguments:

def myfunction(z):
    print(z)

myfunction(3)