from Funciones import *


def asignar_empleado_a_sector(sector=None):
    clear()
    print("Asignación de empleado a sector\n")

    if len(Empleado.dict_empleados.keys()) == 0:
        print("No hay empleados registrados\n")
        return False

    if len(Sector.dict_sectores.keys()) == 0:
        print("No hay sectores registrados\n")
        return False

    while True:
        while True:
            print("0- Cancelar")
            ci = input("Ingrese CI: ")

            if ci == "0":
                clear()
                print("Asignación  cancelada\n")
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

            sector = seleccionar_sector()
            if sector is False:
                return False

        if ci in list(sector.empleados):
            print("El empleado ya pertenece a ese sector")
            return False

        an = sector.set_empleado(Empleado.dict_empleados[ci])
        print(an)

        empleado = Empleado.dict_empleados[ci]

        clear()

        mensaje = f"Empleado {empleado.nombre} ({ci}) asignado al sector {sector.nombre} como {empleado.cargo}"
        print("\n" + "#" * len(mensaje))
        print(mensaje)
        print("#" * len(mensaje))

        a = input("""\n1- Asignar otro empleado\nCualquier otra tecla para terminar\n""")

        if a == "1":
            continue

        clear()

        break
