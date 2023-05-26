from os import system, name
from Clases import *


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
        for i in range(len(Sector.dict_sectores.keys())):
            print(f"        {i + 1}- {list(Sector.dict_sectores.keys())[i]}")

        sector = input("Seleccione sector: ")

        if sector == "0":
            clear()
            print("\nAcción cancelada\n")
            return False

        if sector == "" or not sector.isdigit():
            print("Selección inválida")
            continue

        if float(sector) in range(1, len(Sector.dict_sectores) + 1):
            sector = list(Sector.dict_sectores.keys())[int(sector) - 1]
            sector = Sector.dict_sectores[sector]
            break

        print("Selección inválida")
    return sector


