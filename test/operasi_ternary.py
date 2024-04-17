# kamu = input("aku suka kamu, mau gak jadi pacar aku? [dalam hati: ya/tidak]")
# if kamu == "tidak" :
#     print ("Maaf kamu terlalu baik buat aku")
# else : 
#     print("Iya mau banget")

#Contoh lain
from playsound import playsound
# from moviepy.editor import VideoFileClip
# import numpy as np

# #hanya file randm
# random = 'C:\\Users\\ASUS\\Documents\\python\\test\\rugidong.mp3'

total_belanja = int(input("Total belanja: Rp "))
# # jumlah yang harus dibayar adalah berapa total belanjaannya
# # tapi kalau dapat diskon akan berkurang
bayar = total_belanja
# jika dia belanja di atas 1 juta maka berikan bonus dan diskon
if total_belanja >= 100000:
     diskon = total_belanja * 5/100 #5% #hitung diskonnya
     total_diskon = total_belanja * 5//100
     bayar = total_belanja - diskon
     print(f"Jumlah Bayar: Rp{total_belanja}")
     print(f"Diskon: Rp{total_diskon}" )
     print(f"Total Bayar: Rp {bayar}")
elif total_belanja >= 75000 :
     diskon = total_belanja * 3/100
     totalskon = total_belanja * 3//100
     bayar = total_belanja - diskon
     print(f"Jumlah Bayar: Rp{total_belanja}")
     print(f"Diskon: Rp{totalskon}" )
     print(f"Total Bayar: Rp {int(bayar)}")
elif total_belanja >= 50000 :
     diskon = total_belanja * 1.5 / 100
     total_diskon = total_belanja * 1.5//100
     bayar = total_belanja - diskon
     print(f"Jumlah Bayar: Rp{int(total_belanja)}")     
     print(f"Diskon : Rp {int(total_diskon)}")
     print(f"Total Bayar: Rp {int(bayar)}")
else:
     print(f"Total Bayar: Rp {int(total_belanja)}")





#      #File Video
#      cap = cv2.VideoCapture(random)
#      #Kalau video berhasil dibuka
#      if not cap.isOpened():
#           print("Error")
#           exit()
#      #informasi Video
#      width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
#      height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
#      fps = cap.get(cv2.CAP_PROP_FPS)
#      #membuat jendela
#      cv2.namedWindow("Video Player", cv2.WINDOW_NORMAL)


#      while True :
#           #baca frame dari video
#           ret, frame = cap.read()
#           #periksa apakah frame video berhasil berjalan
#           if not ret:
#                print("END")
#                break
#            # Memutar frame ke orientasi potret
#           rotated_frame = cv2.transpose(frame)
#           rotated_frame = cv2.flip(rotated_frame, flipCode=1)  # Flip secara horizontal
#           #tampilan frame yang diputar
#           cv2.imshow('video player', rotated_frame)
#           #menghentikan loop ketika user menekan tombol q
#           if cv2.waitKey(33) & 0xFF == ord('q'):
#                break
#      #tutup jendela
#      cap.release()
#      cv2.destroyAllWindows()

# cukup = int(input("Berapa Umur Anda  "))

# if cukup >= 18:
#       print("Kamu boleh buat ktp")
# else :
#      print("Kamu belum cukup umur")


# nilai = int(input("Berapa nilai kamu? "))
# if nilai >= 101:
#    grade = "diluar nalar"
# elif nilai >= 90:
#    grade = "A"
# elif nilai >= 80:
#    grade = "B"
# elif nilai >= 70:
#    grade = "C"
# else:
#     grade= "D"

# if grade == "diluar nalar":
#       print("Kamu %s" % grade)
# else:
#       print(f"Kamu dapat grade {grade}")
# elif nilai >= 50:
#    grade = "C"
# elif nilai >= 40:
#    grade = "D"