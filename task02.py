class Transport:
    def korsat(self):
        return "Bu transport vositasi."


class YengilMashina(Transport):
    def korsat(self):
        return "Bu yengil mashina. 4 ta g'ildirakka ega"


class Velosiped(Transport):
    def korsat(self):
        return "Bu velosiped. 2 ta g'ildirakka ega "


transportlar = [YengilMashina(), Velosiped(), Transport()]

for t in transportlar:
    print(t.korsat())
