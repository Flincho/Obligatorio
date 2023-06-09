from Funciones import *


def otorgar_puntos():
    clear()
    print("Otorgar puntos a sector")

    if len(Sector.dict_sectores.keys()) == 0:
        print("No hay sectores registrados\n")
        return False

    sector = seleccionar_sector()
    if sector is False:
        return False

    print(f"\nSector {sector.nombre.upper()} seleccionado para otorgar puntos")

    while True:
        print("\n0- Cancelar")
        mes = input("Ingrese el mes: ")

        if mes == "0":
            clear()
            print("Acción cancelada\n")
            return False

        if mes == "" or not mes.isdigit() or len(mes) > 2 or (0 > int(mes) or int(mes) > 12):
            print("\nMes inválido")
            continue

        if mes[0] == "0":
            mes = mes[1]
        
        mes = int(mes)

        break

    while True:
        print("\n0- Cancelar")
        puntos = input("Ingrese la cantidad de puntos: ")

        if puntos == "0":
            clear()
            print("Acción cancelada\n")
            return False

        if puntos == "" or not isfloat(puntos) or float(puntos) <= 0:
            print("Cantidad de puntos inválida")
            continue

        puntos = float(puntos)
        break

    sector.set_puntos(mes, puntos)

    clear()

    mensaje = f"Se otorgaron {puntos} puntos al sector {sector.nombre} en el mes {mes}"

    print("#" * len(mensaje))
    print(mensaje)
    print("#" * len(mensaje), "\n")
