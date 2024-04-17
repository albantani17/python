#The __init__() Function
#Namun perbedaan method init dan method yang lainya yaitu, jika method pada umumnya untuk mengakses method tersebut 
#kita harus memanggil nama methodnya, nah sedangkanÂ  
#method init kita tidak perlu memanggil nama methodnya dan secara 
#otomatis proses yang terdapat di dalam method tersebut akan di jalankan
print("==========")
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

p1 = Person("Alban", 19)

print(p1.name)
print(p1.age)

#Contoh Lain
print("==========")
class Mahasiswa():

    def __init__(self, masukan_nama):
        self.nama = masukan_nama

    def nilai(self, nilai): # dijalankan ketika dipangil
        if nilai >= 70:
            print(self.nama,'lulus dengan nilai :',nilai)
        else:
            print(self.nama,'tidak lulus dengan nilai :',nilai)

bayu = Mahasiswa("Bayu Putra")
print(bayu.nama) # dipanggil tanpa menggunakan nama method

bayu.nilai(60); # dipanggil dengan menggunakan nama method

# hasil :
# Bayu Putra
# Bayu Putra tidak lulus dengan nilai : 60
print("==========")
