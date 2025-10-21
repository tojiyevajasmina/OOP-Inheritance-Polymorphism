class Media:
    def play(self):
        return "Media ijro qilinmoqda"


class Qoshiq(Media):
    def play(self):
        return "Qoshiq ijro etilmoqda"


class Film(Media):
    def play(self):
        return "Film kursatilmoqda"


class Podkast(Media):
    def play(self):
        return "Podkast eshittirilmoqda "


medialar = [Qoshiq(), Film(), Podkast()]


for media in medialar:
    print(media.play())
