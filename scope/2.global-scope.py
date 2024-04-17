#Variabel yang berada di badan utama kode itu adalah
#global variabel dan dimiliki global scope
# Contoh

x = 300

def func():
    print(x)

# The function will print the local x, and then the code will print the global x
func()

print(x)