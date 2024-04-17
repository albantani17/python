class Ruang:
    def __init__(self, panjang, lebar):
        self.panjang = panjang
        self.lebar = lebar
    
    def luaspersegi(self):
        return self.panjang * self.lebar
    
    def kelilingpersegi(self):
        return 2 * (self.panjang + self.lebar)
    
data = (Ruang(10,9))

print(data.luaspersegi())
print(data.kelilingpersegi())