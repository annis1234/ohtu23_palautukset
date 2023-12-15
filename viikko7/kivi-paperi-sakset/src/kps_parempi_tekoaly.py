
from tekoaly_parannettu import TekoalyParannettu
from kivi_paperi_sakset import KiviPaperiSakset


class KPSParempiTekoaly(KiviPaperiSakset):
    def __init__(self):
        self.tekoaly = TekoalyParannettu(10)

    def _toisen_siirto(self, ensimmainen_siirto):
        tokan_siirto = self.tekoaly.anna_siirto()
        print("Tietokone valitsi", tokan_siirto)
        self.tekoaly.aseta_siirto(ensimmainen_siirto)
        return tokan_siirto
    