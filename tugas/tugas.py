#kalkulator sederhana
def tambah(x,y):
    return x + y

def kurang(x,y):
    return x - y

def kali(x,y):
    return x * y

def bagi(x,y):
    if y == 0:
        print("Error tidak bisa dibagi 0")
    return x / y



while True:
    print("===============================================================")
    print("Pilih Operasi yang diinginkan dengan mengetikkan angka(1,2,3,4)")
    print("1. Pertambahan")
    print("2. Pengurangan")
    print("3. Perkalian")
    print("4. Pembagian")
    user = input("")
    if user in ("1","2","3","4"):
        num1 = float(input("Masukkan angka pertama : "))
        num2 = float(input("Masukkan angka kedua : "))

    if user == "1":
        print("Hasil = ", tambah(num1,num2))
    elif user == "2":
        print("Hasil = ", kurang(num1,num2))
    elif user == "3":
        print("Hasil = ", kali(num1,num2))
    elif user == "4":
        print("Hasil = ", bagi(num1,num2))
    else:
        print("Invalid Input")
    nextcalc = input("Mau melakukan kalkulasi lain? (yes/no) ")
    if nextcalc.lower() != "yes":
        break