from Funciones import *


def alta_de_empleado():
    clear()
    print("Alta de empleado\n")

    while True:
        print("0- Cancelar")
        nombre = input("Ingrese nombre y apellido: ")
        nombre = nombre.strip()

        if nombre == "0":
            clear()
            print("Alta de empleado cancelada\n")
            return False

        if nombre != "" and nombre.find(" ") != -1:
            break

        print("\nNombre y apellido inválido\n")

    while True:
        print("")
        ci = pedir_ci()
        if ci is False:
            clear()
            print("Alta de empleado cancelada\n")
            return False

        if ci in Empleado.dict_empleados.keys():
            print("Ya existe un empleado con esa CI")
            continue

        break

    while True:
        print("\n0- Cancelar")
        salario = input("Ingrese salario: ")

        if salario == "0":
            clear()
            print("Alta de empleado cancelada\n")
            return False

        if isfloat(salario) and float(salario) >= 0:
            salario = float(salario)
            break

        print("Salario inválido")

    while True:
        print("\n0- Cancelar")
        print("""Cargos:
    1- Analista en sistemas
    2- Desarrollador full stack
    3- Team leader
    4- Jefe de sector""")

        cargo = input("\nSeleccione cargo: ")

        if cargo == "0":
            clear()
            print("Alta de empleado cancelada\n")
            return False

        if len(cargo) > 1 or not cargo.isdigit() or int(cargo) not in range(1, 5):
            print("\nOpción inválida")
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

    ci = Empleado(nombre, ci, cargo, salario)

    clear()

    mensaje = f"Empleado {ci.nombre} ({ci.ci}) dado de alta con éxito"
    print("#" * len(mensaje))
    print(mensaje)
    print("#" * len(mensaje) + "\n")
    return True
