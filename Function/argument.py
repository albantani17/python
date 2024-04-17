#One Argument
print("==========")
def my_function(fname):
    print(fname + " uciha")

my_function("Sasuke")
my_function("Itachi")
my_function("sadara")

#Two Arguments
print("==========")
def add_funct(fname,lname):
    print(fname + " " + lname)

add_funct("Alban", "Haerul")

#This function expects 2 arguments, but gets only 1:

#print("==========")
#def my_function(fname, lname):
#  print(fname + " " + lname)

#my_function("Emil")

#Keyword Arguments
print("==========")
def keyword(child3, child2, child1):
   print("The Youngest child is " +  str(child3))

keyword(child1="Harry McDaniel", child2="Keith Carlson", child3="Flora Lambert")

