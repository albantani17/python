def kalkulasi(total_belanja):
    bayar = total_belanja

    if total_belanja <= 100000:
        diskon = total_belanja * 0.05
    elif total_belanja <= 75000:
        diskon = total_belanja * 0.03
    elif total_belanja <= 50000:
        diskon = total_belanja * 0.015
    else:
        diskon = 0

    total_diskon = min(diskon, total_belanja)
    bayar = total_belanja - total_diskon

    return total_belanja, total_diskon, bayar

total_belanja = int(input("Total belanja: Rp "))
result = kalkulasi(total_belanja)

print(f"Jumlah Bayar: Rp{result[0]}")
print(f"Diskon: Rp{result[1]}")
print(f"Total Bayar: Rp{result[2]}")
