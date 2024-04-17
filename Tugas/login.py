import getpass
user = {'username' :'admin', 'password' : '1234'}

def login():
    inputuser = input("Masukkan username:  ")
    inputpas = getpass.getpass("Masukkan password:")

    if inputuser == user['username'] and inputpas == user['password']:
        print("login berhasil")
    else:
        print("Username atau password salah")

login()