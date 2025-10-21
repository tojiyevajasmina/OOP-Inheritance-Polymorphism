class MaishiyTexnika:
    def yoqish(self):
        return "Qurilma yoqildi"

    def uchirish(self):
        return "Qurilma uchirildi"


class Televizor(MaishiyTexnika):
    def yoqish(self):
        return "Televizor yoqildi"

    def uchirish(self):
        return "Televizor uchirildi "


class Muzlatkich(MaishiyTexnika):
    def yoqish(self):
        return "Muzlatkich yoqildi"

    def uchirish(self):
        return "Muzlatkich uchirildi"


qurilmalar = [Televizor(), Muzlatkich()]


for qurilma in qurilmalar:
    print(qurilma.yoqish())
    print(qurilma.uchirish())
