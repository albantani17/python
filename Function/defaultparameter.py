#Default Parameter Value
#The following example shows how to use a default parameter value.

#If we call the function without argument, it uses the default value:

def my_function(country = "Jordan"):
    print("I am from " +  country)

my_function("Cameroon")
my_function("Qatar")
my_function()
my_function("Greece")