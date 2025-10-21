class Foydalanuvchi:
    def kirish_darajasi(self):
        return "Noma'lum kirish darajasi"

class Administrator(Foydalanuvchi):
    def kirish_darajasi(self):
        return "To'liq kirish huquqi"

class Mehmon(Foydalanuvchi):
    def kirish_darajasi(self):
        return "Cheklangan kirish huquqi"

foydalanuvchilar = [Administrator(), Mehmon(), Foydalanuvchi()]

for foydalanuvchi in foydalanuvchilar:
    print(foydalanuvchi.kirish_darajasi())
