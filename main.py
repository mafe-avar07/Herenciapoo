from clases.empleados import Empleado, EmpleadoPorHora, Vendedor

def main():
    empleado = Empleado("Hugo", 2500)
    vendedor = Vendedor("Paco", 2500, 1000)
    empleadoHora = EmpleadoPorHora("Luis", 20, 100)

    print(empleado.descripcion())
    print(vendedor.descripcion())
    print(empleadoHora.descripcion())

if __name__ == "__main__":
    main()