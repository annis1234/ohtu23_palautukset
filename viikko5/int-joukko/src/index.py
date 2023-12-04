import unittest
from int_joukko import IntJoukko


def main():
  joukko = IntJoukko()
  joukko.lisaa(1)
  joukko.lisaa(2)
  joukko.lisaa(5)
  joukko.lisaa(6)

  joukko2 = IntJoukko()
  joukko2.lisaa(2)
  joukko2.lisaa(3)
  joukko2.lisaa(4)

  tulos = IntJoukko.erotus(joukko, joukko2)

  vastauksen_luvut = tulos.to_int_list()

  print(vastauksen_luvut)

# odotettu = [1, 5, 6]


if __name__ == "__main__":
    main()
