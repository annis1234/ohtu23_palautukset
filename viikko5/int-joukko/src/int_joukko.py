
class IntJoukko:
    # tämä metodi on ainoa tapa luoda listoja
    def _luo_lista(self, koko):
        return [0] * koko
    
    def __init__(self, kapasiteetti=5, kasvatuskoko=5):

        self.kapasiteetti = self.validoi_kapasiteetti(kapasiteetti)
        self.kasvatuskoko = self.validoi_kasvatuskoko(kasvatuskoko)
        self.alkiojono = self._luo_lista(self.kapasiteetti)
        self.alkioiden_lkm = 0

    def validoi_kapasiteetti(self, kapasiteetti):
        if not isinstance(kapasiteetti, int) or kapasiteetti < 0:
            raise Exception("Väärä kapasiteetti")
        else:
            return kapasiteetti

    def validoi_kasvatuskoko(self, kasvatuskoko):
        if not isinstance(kasvatuskoko, int) or kasvatuskoko < 0:
            raise Exception("Väärä kasvatuskoko")
        else:
            return kasvatuskoko

    def kuuluu(self, n):
        return n in self.alkiojono

    def lisaa(self, n):
        if not self.kuuluu(n):
            self.alkiojono[self.alkioiden_lkm] = n
            self.alkioiden_lkm += 1
            if self.alkioiden_lkm == len(self.alkiojono):
                vanha_alkijono = self.alkiojono
                self.alkiojono =  self._luo_lista(self.alkioiden_lkm + self.kasvatuskoko)
                self.kopioi_lista(vanha_alkijono, self.alkiojono)
            

    def poista(self, n):
        loytyi = False
        apu = 0

        for i in range(0, self.alkioiden_lkm):
            if n == self.alkiojono[i]:
                self.alkiojono[i] = 0
                loytyi = True
                break

        if loytyi:
            for j in range(i, self.alkioiden_lkm - 1):
                apu = self.alkiojono[j]
                self.alkiojono[j] = self.alkiojono[j + 1]
                self.alkiojono[j + 1] = apu

            self.alkioiden_lkm = self.alkioiden_lkm - 1

    def kopioi_lista(self, a, b):
        for i in range(0, len(a)):
            b[i] = a[i]

    def mahtavuus(self):
        return self.alkioiden_lkm

    def to_int_list(self):
        taulu = self._luo_lista(self.alkioiden_lkm)

        for i in range(0, len(taulu)):
            taulu[i] = self.alkiojono[i]

        return taulu

    @staticmethod
    def yhdiste(a, b):
        x = IntJoukko()
        a_taulu = a.to_int_list()
        b_taulu = b.to_int_list()

        for i in range(0, len(a_taulu)):
            x.lisaa(a_taulu[i])

        for i in range(0, len(b_taulu)):
            x.lisaa(b_taulu[i])

        return x

    @staticmethod
    def leikkaus(a, b):
        y = IntJoukko()
        a_taulu = a.to_int_list()
        b_taulu = b.to_int_list()

        for i in range(0, len(a_taulu)):
            for j in range(0, len(b_taulu)):
                if a_taulu[i] == b_taulu[j]:
                    y.lisaa(b_taulu[j])

        return y

    @staticmethod
    def erotus(a, b):
        z = IntJoukko()
        a_taulu = a.to_int_list()
        b_taulu = b.to_int_list()

        for i in range(0, len(a_taulu)):
            z.lisaa(a_taulu[i])

        for i in range(0, len(b_taulu)):
            z.poista(b_taulu[i])

        return z

    def __str__(self):
        if self.alkioiden_lkm == 0:
            return "{}"
        elif self.alkioiden_lkm == 1:
            return "{" + str(self.alkiojono[0]) + "}"
        else:
            tuotos = "{"
            for i in range(0, self.alkioiden_lkm - 1):
                tuotos = tuotos + str(self.alkiojono[i])
                tuotos = tuotos + ", "
            tuotos = tuotos + str(self.alkiojono[self.alkioiden_lkm - 1])
            tuotos = tuotos + "}"
            return tuotos
