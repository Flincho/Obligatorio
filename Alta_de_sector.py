from Funciones import *
from Empleado_a_sector import *


def alta_de_sector():
    clear()
    print("Alta de sector\n")

    while True:
        print("0- Cancelar")
        nombre = input("Ingrese nombre del sector: ")

        if nombre == "0":
            clear()
            print("Alta de sector cancelada\n")
            return False

        if nombre == "":
            print("Nombre inválido")
            continue

        nombre = Sector(nombre)

        clear()

        mensaje = f"Sector {nombre.nombre} dado de alta con éxito"
        print("\n" + "#" * len(mensaje))
        print(mensaje)
        print("#" * len(mensaje))

        break

    an = input("""\n1- Asignar empleados al nuevo sector\nCualquier otra tecla para terminar\n""")
    if an == "1":
        clear()
        asignar_empleado_a_sector(nombre)
