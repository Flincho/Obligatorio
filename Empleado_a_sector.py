from Funciones import *


def asignar_empleado_a_sector(sector=None):
    clear()

    marcador = 0
    if sector is not None:
        marcador = 1

    print("Asignar empleado a sector\n")

    if len(Empleado.dict_empleados.keys()) == 0:
        print("\nNo hay empleados registrados\n")
        return False

    if len(Sector.dict_sectores.keys()) == 0:
        print("\nNo hay sectores registrados\n")
        return False

    while True:
        while True:
            ci = pedir_ci()

            if ci is False:
                clear()
                print("Asignación de empleado cancelada\n")
                return False

            if ci not in Empleado.dict_empleados.keys():
                print("\nNo existe un empleado con esa CI\n")
                continue

            break

        empleado = Empleado.dict_empleados[ci]

        if empleado.sector is not None:
            print(f"\n{empleado.nombre} ({empleado.ci}) ya pertenece al sector {empleado.sector.nombre.upper()}\n")

            while True:
                print("Desea reasignarlo?\n0- No\n1- Si\n")
                re = input("Ingrese opción: ")

                if re == "0":
                    clear()
                    return False

                if re == "1":
                    break

                print("\nOpción inválida\n")

        print(f"\n{empleado.nombre} ({empleado.ci}) {empleado.cargo.upper()}")

        if sector is None:

            sector = seleccionar_sector()
            if sector is False:
                return False

        print(sector)

        if ci in sector.empleados:
            print("El empleado ya pertenece a ese sector")
            return False

        clear()

        empleado = Empleado.dict_empleados[ci]
        if empleado.sector is not None:
            empleado.sector.empleados.remove(empleado)

            if empleado.cargo is "Team leader":
                empleado.sector.team_leaders.remove(empleado)

        empleado.sector = sector
        sector.empleados = empleado

        mensaje = f"Empleado {empleado.nombre} ({ci}) asignado al sector {sector.nombre} como {empleado.cargo}"
        print("#" * len(mensaje))
        print(mensaje)
        print("#" * len(mensaje))

        a = input("""\n1- Asignar otro empleado\nCualquier otra tecla para terminar\n""")

        if a == "1":
            if marcador == 0:
                sector = None
            clear()
            continue

        clear()

        break
