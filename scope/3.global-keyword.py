# Jika kita perlu membuat variabel global, tetapi terjebak dalam scope lokal, maka kita dapat menggunakan kata kunci global.
# Kata kunci global digunakan untuk membuat variabel menjadi global.

def  main():
    global x
    x = 17
    print(x)

main()

print(x)

# dan juga global keyword bisa dipakai jika ingin membuat
# perubahan terhadap global variabel didalam fungsi

z = "saya hanya manusia"

def buang_global():
    global z
    z = "Saya adalah seorang programmer"

buang_global()

print(z)