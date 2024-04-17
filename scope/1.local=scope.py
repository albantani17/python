#Variabel yang ada di dalam fungsi  termasuk dalam lingkup
#lokal fungsi itu, dan hanya dapat digunakan di dalam fungsi itu
# Contoh:

#Variabel dalam fungsi
def scope():
    x = 300
    print(x)

scope()

#Fungsi di dalam fungsi
def outer_func():
    x = 300
    def inner_func():
        print(x)
    inner_func()

outer_func()
