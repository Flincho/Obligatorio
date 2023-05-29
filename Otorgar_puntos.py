from Funciones import *


def otorgar_puntos():
    clear()
    print("Otorgar de puntos a sector\n")

    if len(Sector.dict_sectores.keys()) == 0:
        print("No hay sectores registrados\n")
        return False

    sector = seleccionar_sector()
    if sector is False:
        return False

    print(f"\nSector {sector.nombre} seleccionado para otorgar puntos")

    while True:
        print("\n0- Cancelar")
        año = input("Ingrese el año: ")

        if año == "0":
            clear()
            print("\nAcción cancelada\n")
            return False

        if año == "" or not año.isdigit() or len(año) > 4 or 2023 > int(año) or int(año) > 2100:
            print("Año inválido")
            continue

        break

    while True:
        print("\n0- Cancelar")
        mes = input("Ingrese el mes: ")

        if mes == "0":
            clear()
            print("\nAcción cancelada\n")
            return False

        if mes == "" or not mes.isdigit() or len(mes) > 2 or (0 > int(mes) or int(mes) > 13):
            print("Mes inválido")
            continue

        if mes[0] == "0":
            mes = mes[1]

        break

    while True:
        print("\n0- Cancelar")
        puntos = input("Ingrese la cantidad de puntos: ")

        if puntos == "0":
            clear()
            print("\nAcción cancelada\n")
            return False

        if puntos == "" or not isfloat(puntos) or int(puntos) <= 0:
            print("Cantidad de puntos inválidos")
            continue

        puntos = float(puntos)
        break

    sector.set_puntos(año, mes, puntos)

    clear()

    mensaje = f"Se otorgaron {puntos} puntos al sector {sector.nombre} en el mes {mes} del año {año}"

    print("\n" + "#" * len(mensaje))
    print(mensaje)
    print("#" * len(mensaje), "\n\n")
