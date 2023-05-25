from Clases import *


def alta_de_empleado():

    while True:
        print("\n0- Cancelar")
        nombre = input("Ingrese nombre y apellido: ")

        if nombre == "0":
            print("\nAlta de empleado cancelada\n")
            return False

        if nombre != "" and nombre.find(" ") != -1:
            break

        print("Nombre y apellido inválido")

    while True:
        print("\n0- Cancelar")
        ci = input("Ingrese CI: ")

        if ci == "0":
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

            if (cargo == "Analista en sistemas" or cargo == "Desarrollador full stack") and sup_obj.cargo != "Team leader":
                print("La CI ingresada no es de un team leader")
                continue

            break

    else:
        supervisor = None

    ci = Empleado(nombre, ci, cargo, salario, supervisor)

    mensaje = f"Empleado {ci.nombre} ({ci.ci}) dado de alta con éxito"
    print("\n" + "#" * len(mensaje))
    print(mensaje)
    print("#" * len(mensaje))

    return True
