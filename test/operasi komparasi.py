# operasi komparasi
# hasil akan menjadi boolean

a = 4
b = 2

#lebih besar (>)
print('=====(>)=====')
hasil = a > b
print(a,">",b,'=',hasil)
hasil = a > 3
print(a,'>',3,'=',hasil)
hasil = b > 3
print(b,'>',3,'=',hasil)
hasil = a > b
print(a,">",b,'=',hasil)
hasil = a > 3
print(a,'>',3,'=',hasil)
hasil = b > 3
print(b,'>',3,'=',hasil)

#Lebih kecil(<)
print('=====(<)=====')
hasil = a < b
print(a,'<',b,'=',hasil)
hasil = a < 5
print(a,'<',5,'=',hasil)
hasil = b < 5
print(b,'<',5,'=',hasil)

#Lebih besar dari sama dengan(>=)
print('=====(>=)=====')
hasil = a >= b
print(a,">=",b,'=',hasil)
hasil = a >= 5
print(a,'>=',5,'=',hasil)
hasil = b >= 2
print(b,'>=',2,'=',hasil)

#Lebih kecilr dari sama dengan(<=)
print('=====(<=)=====')
hasil = a <= b
print(a,'<=',b,'=',hasil)
hasil = a <= 5
print(a,'<=',5,'=',hasil)
hasil = b <= 2
print(b,'<=',2,'=',hasil)

#Sama dengan(==)
print('=====(==)=====')
hasil = a == b
print(a,'==',b,'=',hasil)
hasil = b == 2
print(b,'==',2,'=',hasil)

#Tidal sama dengan(!=)
print('=====(!=)=====')
hasil = a != b
print(a,'!=',b,'=',hasil)
hasil = b != 2
print(b,'!=',2,'=',hasil)

#is/not sebagai komparasi object identity
print('=====(is/not)=====')
x = 5 #assigment untuk objek
y = 5
print('nilai x = ',x,'id = ',hex(id(x)))
print('nilai y = ',y,'id = ',hex(id(y)))
hasil = x is y
print('x is y = ',hasil)

x = 5 #is not
y = 6
print('nilai x = ',x,'id = ',hex(id(x)))
print('nilai y = ',y,'id = ',hex(id(y)))
hasil = x is not y
print('x is not y = ',hasil)