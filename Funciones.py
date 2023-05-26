from os import system
from Clases import *


def alta_de_empleado():
    system("cls")
    while True:
        print("\n0- Cancelar")
        nombre = input("Ingrese nombre y apellido: ")

        if nombre == "0":
            system("cls")
            print("\nAlta de empleado cancelada\n")
            return False

        if nombre != "" and nombre.find(" ") != -1:
            break

        print("Nombre y apellido inválido")

    while True:
        print("\n0- Cancelar")
        ci = input("Ingrese CI: ")

        if ci == "0":
            system("cls")
            print("\nAlta de empleado cancelada\n")
            return False

        if len(ci) != 8 or not ci.isdigit():
            print("CI inválida")
            continue

        ci = int(ci)

        if ci in Empleado.dict_empleados.keys():
            print("Ya existe un empleado con esa CI")
            continue

        break

    while True:
        print("\n0- Cancelar")
        salario = input("Ingrese salario: ")

        if salario == "0":
            system("cls")
            print("\nAlta de empleado cancelada\n")
            return False
        if salario.isdigit() and int(salario) >= 0:
            salario = int(salario)
            break

        print("Salario inválido")

    while True:
        print("\n0- Cancelar")
        print("""Seleccione cargo:
              1- Analista en sistemas
              2- Desarrollador full stack
              3- Team leader
              4- Jefe de sector""")

        cargo = input("Ingrese opción: ")

        if cargo == "0":
            system("cls")
            print("\nAlta de empleado cancelada\n")
            return False

        if not cargo.isdigit() or int(cargo) not in range(1, 5):
            print("Opción inválida")
            continue

        if cargo == "1":
            cargo = "Analista en sistemas"
            break

        if cargo == "2":
            cargo = "Desarrollador full stack"
            break

        if cargo == "3":
            cargo = "Team leader"
            break

        if cargo == "4":
            cargo = "Jefe de sector"
            break

    if cargo != "Jefe de sector":
        while True:
            print("\n0- Cancelar")
            supervisor = input("Ingrese CI del supervisor: ")

            if supervisor == "0":
                system("cls")
                print("\nAlta de empleado cancelada\n")
                return False

            if len(supervisor) != 8 or not supervisor.isdigit():
                print("CI de supervisor inválida")
                continue

            supervisor = int(supervisor)
            sup_obj = Empleado.dict_empleados[supervisor]

            if supervisor not in Empleado.dict_empleados.keys():
                print("CI de supervisor inválida")
                continue

            if cargo == "Team leader" and sup_obj.cargo != "Jefe de sector":
                print("La CI ingresada no es de un jefe de sector")
                continue

            if cargo == ("Analista en sistemas" or "Desarrollador full stack") and sup_obj.cargo != "Team leader":
                print("La CI ingresada no es de un team leader")
                continue

            break

    else:
        supervisor = None

    ci = Empleado(nombre, ci, cargo, salario, supervisor)

    system("cls")

    mensaje = f"Empleado {ci.nombre} ({ci.ci}) dado de alta con éxito"
    print("\n" + "#" * len(mensaje))
    print(mensaje)
    print("#" * len(mensaje))

    return True


def alta_de_sector():
    system("cls")
    while True:
        print("\n0- Cancelar")
        nombre = input("Ingrese nombre del sector: ")

        if nombre == "0":
            system("cls")
            print("\nAlta de sector cancelada\n")
            return False

        if nombre == "":
            print("Nombre inválido")
            continue

        nombre = Sector(nombre)

        system("cls")

        mensaje = f"Sector {nombre.nombre} dado de alta con éxito"
        print("\n" + "#" * len(mensaje))
        print(mensaje)
        print("#" * len(mensaje))

        break

    an = input("""\n1- Asignar empleados al nuevo sector\nCualquier otra tecla para terminar\n""")
    if an == "1":
        system("cls")
        asignar_empleado_a_sector(nombre)


def asignar_empleado_a_sector(sector=None):
    system("cls")
    while True:
        while True:
            print("\n0- Cancelar")
            ci = input("Ingrese CI: ")

            if ci == "0":
                system("cls")
                print("\nAsignación  cancelada\n")
                return False

            if len(ci) != 8 or not ci.isdigit():
                print("CI inválida")
                continue

            ci = int(ci)

            if ci not in Empleado.dict_empleados.keys():
                print("No existe un empleado con esa CI")
                continue

            break

        if sector is None:
            while True:
                print("\n0- Cancelar")

                for i in range(len(Sector.dict_sectores.keys())):
                    print(f"{i+1}- {list(Sector.dict_sectores.keys())[i]}")

                sector = input("Seleccione sector: ")

                if sector == "0":
                    system("cls")
                    print("\nAsignación cancelada\n")
                    return False

                if sector == "" or not sector.isdigit():
                    print("Selección inválida")
                    continue

                if float(sector) in range(1, len(Sector.dict_sectores)+1):
                    sector = list(Sector.dict_sectores.keys())[int(sector)-1]
                    sector = Sector.dict_sectores[sector]
                    break

                print("Selección inválida")

        if ci in list(sector.empleados):
            print("El empleado ya pertenece a ese sector")
            return False

        an = sector.set_empleado(Empleado.dict_empleados[ci])
        print(an)

        empleado = Empleado.dict_empleados[ci]

        system("cls")

        mensaje = f"Empleado {empleado.nombre} ({ci}) asignado al sector {sector.nombre} como {empleado.cargo}"
        print("\n" + "#" * len(mensaje))
        print(mensaje)
        print("#" * len(mensaje))

        a = input("""\n1- Asignar otro empleado\nCualquier otra tecla para terminar\n""")

        if a == "1":
            continue

        system("cls")

        break


def otorgar_puntos():
    system("cls")

    while True:
        print("\n0- Cancelar")

        for i in range(len(Sector.dict_sectores.keys())):
            print(f"{i + 1}- {list(Sector.dict_sectores.keys())[i]}")

        sector = input("Seleccione sector para otorgar puntos: ")

        if sector == "0":
            system("cls")
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

    print(f"\nSector {sector.nombre} seleccionado para otorgar puntos")

    while True:
        print("\n0- Cancelar")
        año = input("Ingrese el año: ")

        if año == "0":
            system("cls")
            print("\nAcción cancelada\n")
            return False

        if año == "" or not año.isdigit() or (2023 < int(año) or int(año) > 2100):
            print("Año inválido")
            continue

        break

    while True:
        print("\n0- Cancelar")
        mes = input("Ingrese el mes: ")

        if mes == "0":
            system("cls")
            print("\nAcción cancelada\n")
            return False

        if mes == "" or not mes.isdigit() or (0 > int(mes) or int(mes) > 13):
            print("Mes inválido")
            continue

        break

    while True:
        print("\n0- Cancelar")
        puntos = input("Ingrese la cantidad de puntos: ")

        if puntos == "0":
            system("cls")
            print("\nAcción cancelada\n")
            return False

        if puntos == "" or not puntos.isdigit() or int(puntos) <= 0:
            print("Cantidad de puntos inválidos")
            continue

        puntos = int(puntos)
        break

    Sector.set_puntos(sector, año, mes, puntos)

    system("cls")

    mensaje = f"Se otorgaron {puntos} puntos al sector {sector.nombre} en el mes {mes} del año {año}"

    print("\n" + "#" * len(mensaje))
    print(mensaje)
    print("#" * len(mensaje), "\n\n")
