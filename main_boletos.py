from clases.boletos import Boleto, BoletoEstudiante, BoletoCortesia, BoletoTerceraEdad

def main():
    boleto = Boleto("Andrea", "Sala 2, 18:00")
    estudiante = BoletoEstudiante("Bruno", "Sala 2, 18:00")
    cortesia = BoletoCortesia("Carla", "Sala 5, 20:30")
    tercera_edad = BoletoTerceraEdad("Diana", "Sala 1, 16:00")

    print(boleto.ticket())
    print(estudiante.ticket())
    print(cortesia.ticket())
    print(terceraEdad.ticket())

if __name__ == "__main__":
    main()
