class Hayvon:
    def ovoz(self):
        return "Noma'lum hayvon tovushi"


class It(Hayvon):
    def ovoz(self):
        return "Vov!"


class Mushuk(Hayvon):
    def ovoz(self):
        return "Miyov!"


hayvonlar = [It(), Mushuk(), Hayvon()]

for hayvon in hayvonlar:
    print(hayvon.ovoz())
