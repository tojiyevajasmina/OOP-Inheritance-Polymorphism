class Tortburchak:
    def __init__(self, eni, buyi):
        self.eni = eni
        self.buyi = buyi

    def get_area(self):
        return self.eni * self.buyi

class Kvadrat:
    def __init__(self, tomon):
        self.tomon = tomon

    def get_area(self):
        return self.tomon * self.tomon


shakllar = [
    Tortburchak(5, 7),
    Tortburchak(3, 4),
    Kvadrat(4),
    Kvadrat(8),
    Kvadrat(2)
]


yuzalar = [shakl.get_area() for shakl in shakllar]


print("Eng katta yuza:", max(yuzalar))
