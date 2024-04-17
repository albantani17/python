#perhitungan suhu celcius

print("\nKONVERSI SUHU\n")

celcius = float(input('masukan suhu celcius: '))
print("suhu adalah ",celcius,"C")

reamur = (4/5) * celcius
print("suhu dalam reamur adalah ",reamur,"R")

fahrenheit = (9/5) * celcius + 32
print("suhu dalam fahrenheit adalah ",fahrenheit, 'F')

kelvin = celcius + 273
print("suhu dalam kelvin adalah ",kelvin, 'K')

#perhitungan suhu reamur

reamur = float(input("masukan suhu reamur: " ))
print("suhu adalah ",reamur, "R")

celcius = (5/4) * reamur
print("suhu dalam celcius adalah ",celcius,"C")

fahrenheit = (9/4) * reamur + 32
print("suhu dalam celcius adalah ",fahrenheit,"F")

kelvin = (5/4) * reamur + 273
print("suhu dalam celcius adalah ",kelvin,"K")

#perhitungan suhu fahrenheit

fahrenheit = float(input("masukan suhu fahrenheit: "))
print("suhu adalah ",fahrenheit,"F")

celcius = (5/9) * (fahrenheit - 32)
print("suhu dalam celcius adalah ",celcius,"C")

reamur = (4/9) * (fahrenheit - 32)
print("suhu dalam reamur adalah ",reamur,"R")

kelvin = (5/9) * (fahrenheit - 32) + 273
print("suhu dalam kelvin adalah ",kelvin,"K")

#perhitungan suhu kelvin
kelvin = float(input("masukan suhu kelvin: "))
print("suhu adalah",kelvin,"K")

celcius = kelvin - 273
print("suhu dalam celcius adalah ",celcius,"C")

reamur = (4/5) * (kelvin - 273)
print("suhu dalam reamur adalah ",reamur,"R")

fahrenheit = (kelvin - 273) * (9/5) + 32
print("suhu dalam fahrenheit",fahrenheit,"F")