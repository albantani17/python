#Positional-Only Arguments
#You can specify that a function can have ONLY positional arguments, or ONLY keyword arguments.

#To specify that a function can have only positional arguments, add , / after the arguments:

def my_funtion(x , /):
    print(x)

my_funtion(10)  #This will work fine because we are passing one and only argument which is positional.

#Without the , / you are actually allowed to use keyword arguments even if the function expects positional arguments:

def funct(x):
    print(x)

funct(x = 3)

