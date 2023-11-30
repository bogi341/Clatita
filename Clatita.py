class Clatita:
    def __init__(self, diametru, tip_aluat, umplutura):
        self.diametru = diametru
        self.tip_aluat = tip_aluat
        self.umplutura = umplutura

    def __str__(self):
        return f"Clatita de {self.diametru} cm, cu aluat de {self.tip_aluat} și umplutură de {self.umplutura}"

    def pregatire(self):
        return f"Pregătirea clatitei de {self.diametru} cm"

    def servire(self):
        return f"Servirea clatitei de {self.diametru} cm"


class ClatitaCuGem(Clatita):
    def __init__(self, diametru, tip_aluat, umplutura, gust_gem):
        super().__init__(diametru, tip_aluat, umplutura)
        self.gust_gem = gust_gem

    def __str__(self):
        return f"{super().__str__()}, cu gust de gem: {self.gust_gem}"

    def umplutura_speciala(self):
        return f"Umplutura specială cu gem: {self.gust_gem}"

    def servire(self):
        return f"Servirea clatitei cu gem de {self.diametru} cm"


class ClatitaCuCiocolata(Clatita):
    def __init__(self, diametru, tip_aluat, umplutura, tip_ciocolata):
        super().__init__(diametru, tip_aluat, umplutura)
        self.tip_ciocolata = tip_ciocolata

    def __str__(self):
        return f"{super().__str__()}, cu ciocolată de tip: {self.tip_ciocolata}"

    def topping_ciocolata(self):
        return f"Topping de ciocolată: {self.tip_ciocolata}"

    def servire(self):
        return f"Servirea clatitei cu ciocolată de {self.diametru} cm"


class ClatitaCuBranza(Clatita):
    def __init__(self, diametru, tip_aluat, umplutura, tip_branza):
        super().__init__(diametru, tip_aluat, umplutura)
        self.tip_branza = tip_branza

    def __str__(self):
        return f"{super().__str__()}, cu brânză de tip: {self.tip_branza}"

    def adauga_branza(self):
        return f"Adăugare brânză: {self.tip_branza}"

    def servire(self):
        return f"Servirea clatitei cu brânză de {self.diametru} cm"


if __name__ == "__main__":
    clatita_generica = Clatita(20, "clasic", "nutella")
    clatita_gem = ClatitaCuGem(25, "delicat", "gem de capsuni", "capsuni proaspete")
    clatita_ciocolata = ClatitaCuCiocolata(30, "aerat", "ciocolata cu alune", "ciocolata neagra")
    clatita_branza = ClatitaCuBranza(22, "integral", "branza de vaci", "feta")

    lista_clatite = [clatita_generica, clatita_gem, clatita_ciocolata, clatita_branza]

    for clatita in lista_clatite:
        print(clatita)
        print(clatita.pregatire())
        print(clatita.servire())
        print("-" * 30)
