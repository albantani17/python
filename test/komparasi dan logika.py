# membuat area gabungan rentang dari angka

#++++++3-------10++++++

from inspect import isclass


User =float(input("masukkan angka yang bernilai\n lebih kecil dari 3\n atau lebih besar dari 10\n:"))

# ++++++3-------

kurangdari = (User < 3)
print("Kurang dari 3 :",kurangdari)

# -------10++++++
lebihdari = (User > 10)
print("lebih dari 10",lebihdari)

#++++3-------10+++++
isCorrect = kurangdari or lebihdari
print("angka yg dimasukkan", isCorrect)

#------3++++++10------

User =float(input("masukkan angka yang bernilai\nlebih besar dari 3\natau lebih kecil dari 10\n:"))

lebihdari = User > 3
kurangdari = User < 10
print("Lebih dari 3 :",lebihdari)
print("Kurang dari 10 :",lebihdari)

isCorrect = lebihdari or kurangdari
print("angka yang dimasukkan :", isCorrect)