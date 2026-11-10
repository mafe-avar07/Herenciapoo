class Boleto(object):
    def __init__(self, cliente, función):
        self.cliente = cliente
        self.funcion = funcion
        self.precio_base = 90

    def calcular_precio(self):
        return self.precio_base

    def ticket(self):
        return f"{self.cliente} - {self.funcion}: ${self.calcular_precio():,.2f}"


class BoletoEstudiante(Boleto):
    def __init__(self, cliente, funcion):
        super().__init__(cliente, funcion)

    def calcular_precio(self):
        return super().calcular_precio() * 0.70


class BoletoCortesia(Boleto):
    def __init__(self, cliente, funcion):
        super().__init__(cliente, funcion)

    def calcular_precio(self):
        return 0


class BoletoTerceraEdad(Boleto):
    def __init__(self, cliente, funcion):
        super().__init__(cliente, funcion)

    def calcular_precio(self):
        return super().calcular_precio() / 0.70 * 50