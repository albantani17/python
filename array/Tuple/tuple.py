#Tuple mirip seperti list bisa 
#naro banyak item di 1 variabel 
#tapi berurutan dan tidak bisa diubah
#boleh duplikat artinya boleh sama isinya

print("=========")
thistuple = ("apple", "banana", "cherry")
print(thistuple)

print("=========")
thistuple2 = ("apple", "banana", "cherry", "apple", "cherry")
print(thistuple2)

#Tuple lenght
print("=========")
print(len(thistuple))

#membuat tuple dengan 1 item
#untuk membuat tuple harus ada koma
print("=========")
thistuple3 = ("apple",)
print(type(thistuple3))
#Kalau tidak ada koma maka akan menjadi string
thistuple4 = ("apple")
print(type(thistuple4))

#Tipe Data
#Item tuple boleh tipe data apa saja , termasuk string, integer, float, boolean
fruit_tuple = ("apple", "banana", "cherry")
number_tuple =  (10, 20, 30)
boolean_tuple = (True, False, True)

#dalam 1 tuple boleh tipe data yang berbeda beda
tuple1 =  ("I like apple","I love banana",56,"Python is awesome")

print("=========")
#The tuple() COnstructor
#Untuk membuat tuple dari variable lainnya gunakan constructor tuple()
tuple2 = tuple(("apple", "banana", "cherry")) # note the double round-brackets
print(tuple2)