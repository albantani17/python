while True:
    umur = int(input("Berapa Umur kamu?  "))

    if umur >= 21:
        print("kamu boleh ikut pemilu")
    elif umur >= 15:
        menikah = input("Kamu sudah menikah atau belum?[ya/tidak]  ")
        if "tidak" in menikah.lower():
            print("Kamu tidak boleh ikut pemilu")
        elif "ya" in menikah.lower():
            print("kamu boleh ikut pemilu")
        else:
            ulangi = input("Coba bilang sekali lagi?")
            if ulangi.lower() != "ya":
                break
    else:
        print("kamu tidak boleh ikut pemilu")
        