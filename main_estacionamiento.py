from clases.estacionamiento import Estancia, EstanciaPension, EstanciaNocturna

def main():
    estancia = Estancia("ABC-123", 3)
    pension = EstanciaPension("XYZ-789")
    nocturna = EstanciaNocturna("JKL-456", 5)

    print(estancia.ticket())
    print(pension.ticket())
    print(nocturna.ticket())

if __name__ == "__main__":
    main()