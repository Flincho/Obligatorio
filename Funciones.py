from os import system, name
from Clases import *

#limpiar terminal segun sistema operativo
def clear():
    if name == "nt":
        system('cls')
    else:
        system("clear")

#Seleccionar sectores existentes
def seleccionar_sector():

    if len(Sector.dict_sectores.keys()) == 0:
        print("No hay sectores registrados\n")
        return False

    while True:
        print("\n0- Cancelar")
        print("Sectores:")
#Imprime los sectores registrados, con su numero de orden, arranca en 1 por el i + 1
        for i in range(len(Sector.dict_sectores.keys())):
            print(f"        {i + 1}- {list(Sector.dict_sectores.keys())[i]}")

        sector = input("\nSeleccione sector: ")

        if sector == "0":
            clear()
            print("Acción cancelada\n")
            return False
#Si no existe contenido,o letras, imprime seleccion invalida
        if sector == "" or not sector.isdigit():
            print("Selección inválida")
            continue
#Sumo y resto 1 para que el numero de orden sea el mismo que el indice de la lista
        if int(sector) in range(1, len(Sector.dict_sectores) + 1):
            sector = list(Sector.dict_sectores.values())[int(sector) - 1]
#Con el breake salgo del while           
            break

        print("Selección inválida")
    return sector


def tests():

    test = [54631974, 55555555, 77777777, 66666666]
    test[0] = Empleado("Alex Ernst", 54631974, "Jefe de sector", 70000, None)
    test[1] = Empleado("Sol Pereira", 55555555, "Team leader", 4555, test[0])
    test[2] = Empleado("Fernando Alonso", 77777777, "Analista en sistemas", 6000, test[1])
    test[3] = Empleado("Carlos Sainz", 66666666, "Desarrollador full stack", 2200, test[1])
    gc = Sector("Gestión de calidad")
    testing = Sector("Testing")
    #testing.set_empleado(test[0])
    #testing.set_empleado(test[1])
    gc.set_puntos("2023", "12", 500)
    gc.set_puntos("2023", "4", 660)
    testing.set_puntos("2023", "12", 1900)