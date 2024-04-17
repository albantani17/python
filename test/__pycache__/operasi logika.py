#operasi logika atau boolean
# not, or, xor

#not
print("====NOT====")
a = False
b = not a
print("data =",a)
print("data =",b)

#or (jika salah satu true, maka hasilnya true)
print("====OR====")
a = True
b = True
c = a or b
print(a,'OR',b,'=',c)
a = True
b = False
c = a or b
print(a,'OR',b,'=',c)
a = False
b = True
c = a or b
print(a,'OR',b,'=',c)
a = False
b = False
c = a or b
print(a,'OR',b,'=',c)

#and (jika 2 2 nya true hasilnya true)
print("====AND====")
a = True
b = True
c = a and b
print(a,'AND',b,'=',c)
a = True
b = False
c = a and b
print(a,'AND',b,'=',c)
a = False
b = True
c = a and b
print(a,'AND',b,'=',c)
a = False
b = False
c = a and b
print(a,'AND',b,'=',c)

#XOR (salah satu true hasilnya true, sisanya false)
print("====XOR====")
a = True
b = True
c = a ^ b
print(a,'XOR',b,'=',c)
a = True
b = False
c = a ^ b
print(a,'XOR',b,'=',c)
a = False
b = True
c = a ^ b
print(a,'XOR',b,'=',c)
a = False
b = False
c = a ^ b
print(a,'XOR',b,'=',c)
