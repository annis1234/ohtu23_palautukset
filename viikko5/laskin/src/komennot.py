class Summa:

    def __init__(self, sovelluslogiikka, lue_syote):
        self.sovelluslogiikka = sovelluslogiikka
        self.lue_syote = lue_syote
        self.vanha_arvo = self.sovelluslogiikka.arvo()

    def suorita(self):
        self.vanha_arvo = self.sovelluslogiikka.arvo()
        arvo = int(self.lue_syote())
        self.sovelluslogiikka.plus(arvo)

    def kumoa(self):
        self.sovelluslogiikka.aseta_arvo(self.vanha_arvo)


class Erotus:
    def __init__(self, sovelluslogiikka, lue_syote):
        self.sovelluslogiikka = sovelluslogiikka
        self.lue_syote = lue_syote
        self.vanha_arvo = self.sovelluslogiikka.arvo()

    def suorita(self):
        self.vanha_arvo = self.sovelluslogiikka.arvo()
        arvo = int(self.lue_syote())
        self.sovelluslogiikka.miinus(arvo)

    def kumoa(self):
        self.sovelluslogiikka.aseta_arvo(self.vanha_arvo)

class Nollaus:
    def __init__(self, sovelluslogiikka):
        self.sovelluslogiikka = sovelluslogiikka
        self.vanha_arvo = self.sovelluslogiikka.arvo()

    def suorita(self):
        self.vanha_arvo = self.sovelluslogiikka.arvo()
        self.sovelluslogiikka.nollaa()
    
    def kumoa(self):
        self.sovelluslogiikka.aseta_arvo(self.vanha_arvo)