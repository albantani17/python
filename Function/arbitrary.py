#arbitrary arguments, *args
#If you do not know how many arguments that will be passed into your function, add a * before the parameter name in the function definition.
#This way the function will receive a tuple of arguments, and can access the items accordingly:

#If the number of arguments is unknown, add a * before the parameter name:
def my_function(*kids):
  print("The youngest child is " + kids[2])

my_function("Emil", "Tobias", "Linus")

#Arbitrary Keyword Arguments, **kwargs
#If you do not know how many keyword arguments that will be passed into your function, add two asterisk: ** before the parameter name in the function definition.

#This way the function will receive a dictionary of arguments, and can access the items accordingly:
print("==========")
def my_keyword(**kid):
  print("His last name is "+ kid["lname"])

my_keyword(fname = "tobias", lname = "bernsen")