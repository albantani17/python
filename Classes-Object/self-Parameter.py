#The self Parameter
#Jadi fungsi dari “self” ini sebenarnya adalah sebagai sebuah variabel saja yang yang menyatakan kelas itu sendiri. 
#Nah itu sebabnya.. Jika kita ingin memanggil sebuah variabel atau metode di dalam sebuah class, 
#dan metode yang akan kita panggil ada di class itu juga, maka kita memakai kata “self” di depan nama variabel atau metodenya.

#Tidak harus dinamain self, bisa yang lain, tetapi itu harus menjadi parameter pertama dari fungsi apa pun di kelas

#Contoh menggunakan kata lain daripada self:
class Kelas:
    def __init__(abc, name, age):
        abc.name = name
        abc.age = age

    def myfunc(abc):
        print("Hello", abc.name)

nama = Kelas("Alban",19)
nama.myfunc()