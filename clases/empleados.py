class Empleado(object):
    def __init__(self, nombre, salario_base):
        self.nombre = nombre
        self.salario_base = salario_base

    def calcular_pago(self):
        return self.salario_base

    def descripcion(self):
        return f"{self.nombre}: ${self.calcular_pago():,.2f}"

#La clase Vendedor hereda a la clase Empleado.
class Vendedor(Empleado):
    def __init__(self, nombre, salario_base, ventas, comision=0.05):
        super().__init__(nombre, salario_base)
        self.ventas = ventas
        self.comision = comision

    #Polimorfismo: es la capacidad de declarar un método con el mismo nombre de la clase base.
    def calcular_pago(self):
        return super().calcular_pago() + (self.ventas * self.comision)



class EmpleadoPorHora(Empleado):
    def __init__(self, nombre, horas, tarifa):
        super().__init__(nombre, salario_base=0)
        self.horas = horas
        self.tarifa = tarifa

    def calcular_pago(self):
        return self.horas * self.tarifa

    