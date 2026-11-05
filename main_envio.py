from clases.paqueteria import Envio, EnvioExpress, EnvioSobre


def main():
    envio = Envio("Hugo", 10)
    sobre = EnvioSobre("Paco")
    express = EnvioExpress("Luis", 20)

    print(envio.resumen())
    print(sobre.resumen())
    print(express.resumen())

if __name__ == "__main__":
    main()