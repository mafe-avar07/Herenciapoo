class Estancia(object):
    def _init_(self, placa, horas):
        if horas <= 0:
            raise ValueError("El número de horas debe ser mayor que cero.")

        self.placa = placa
        self.horas = horas

    def cobrar(self):
        return self.horas * 20

    def ticket(self):
        return f"{self.placa} ({self.horas} h): ${self.cobrar():,.2f}"


class EstanciaPension(Estancia):
    def _init_(self, placa):
        super()._init_(placa, 24)

    def cobrar(self):
        return 250


class EstanciaNocturna(Estancia):
    def _init_(self, placa, horas):
        super()._init_(placa, horas)

    def cobrar(self):
        return super().cobrar() + 50