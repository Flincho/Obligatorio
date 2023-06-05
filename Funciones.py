from os import system, name
from Clases.Empleado_cl import *
from Clases.Sector_cl import *


def clear():
    if name == "nt":
        system('cls')
    else:
        system("clear")


def seleccionar_sector():

    if len(Sector.dict_sectores.keys()) == 0:
        print("No hay sectores registrados\n")
        return False

    while True:
        print("\n0- Cancelar")
        print("Sectores:")
        # Imprime los sectores registrados, con su número de orden, arranca en 1 por el i + 1
        for i in range(len(Sector.dict_sectores.keys())):
            print(f"        {i + 1}- {list(Sector.dict_sectores.keys())[i]}")

        sector = input("\nSeleccione sector: ")

        if sector == "0":
            clear()
            print("Acción cancelada\n")
            return False
        # Si no existe contenido,o letras, imprime selección invalida
        if sector == "" or not sector.isdigit():
            print("Selección inválida")
            continue

        if int(sector) in range(1, len(Sector.dict_sectores) + 1):
            sector = list(Sector.dict_sectores.values())[int(sector) - 1]
            return sector
            break

        print("Selección inválida")


def isfloat(num):
    try:
        float(num)
        return True
    except ValueError:
        return False


def tests():

    test = [54631974, 55555555, 77777777, 66666666]
    test[0] = Empleado("Alex Ernst", 54631974, "Jefe de sector", 70000)
    test[1] = Empleado("Sol Pereira", 55555555, "Team leader", 4555)
    test[2] = Empleado("Fernando Alonso", 77777777, "Analista en sistemas", 6000)
    test[3] = Empleado("Carlos Sainz", 66666666, "Desarrollador full stack", 2200)
    gc = Sector("Gestión de calidad")
    testing = Sector("Testing")
    gc.set_puntos(12, 500)
    gc.set_puntos(4, 660)
    testing.set_puntos(12, 1900)


def pedir_ci():
    while True:
        print("\n0- Cancelar")
        ci = input("\nIngrese CI: ")

        if ci == "0":
            clear()
            print("Acción cancelada\n")
            return False

        if len(ci) != 8 or not ci.isdigit():
            print("CI inválida")
            continue

        return int(ci)
