from Funciones import *


def cantidad_de_empleados():
    clear()
    print("Cantidad de empleados\n")

    if len(Sector.dict_sectores.keys()) == 0:
        print("No hay sectores registrados\n")
        return False

    if len(Empleado.dict_empleados.keys()) == 0:
        print("No hay empleados registrados\n")
        return False

    while True:
        print("Sectores:")
        print("\n0- Cancelar")

        for i in range(len(Sector.dict_sectores.keys())):
            print(f"{i + 1}- {list(Sector.dict_sectores.keys())[i]}")

        cant_sectores = len(Sector.dict_sectores.keys())
        print(f"{cant_sectores + 1}- Todos los sectores")

        sector = input("Seleccione sector: ")

        if sector == "0":
            clear()
            print("\nConsulta cancelada\n")
            return False

        if sector == "" or not sector.isdigit():
            print("Selección inválida")
            continue

        if float(sector) in range(1, len(Sector.dict_sectores) + 1):
            sector = list(Sector.dict_sectores.keys())[int(sector) - 1]
            sector = Sector.dict_sectores[sector]
            break

        if float(sector) == cant_sectores + 1:
            sector = None
            break

        print("Selección inválida")

    while True:
        print("\n0- Cancelar")
        print("""Cargos:
        1- Analista en sistemas
        2- Desarrollador full stack
        3- Team leader
        4- Jefe de sector
        5- Todos los cargos""")

        cargo = input("Seleccione cargo: ")

        if cargo == "0":
            clear()
            print("\nConsulta cancelada\n")
            return False

        if not cargo.isdigit() or int(cargo) not in range(1, 6):
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

        if cargo == "5":
            cargo = None
            break

    jefes_de_sector = []
    team_leaders = []
    desarrolladores_full_stack = []
    analistas_en_sistemas = []
    general = []

    if sector is None and cargo is None:
        clear()
        print(f"\nHay {len(Empleado.dict_empleados.keys())} empleado/s en toda la empresa\n")

        for empleado in Empleado.dict_empleados.values():
            if empleado.cargo == "Jefe de sector":
                jefes_de_sector.append(empleado)

            if empleado.cargo == "Team leader":
                team_leaders.append(empleado)

            if empleado.cargo == "Desarrollador full stack":
                desarrolladores_full_stack.append(empleado)

            if empleado.cargo == "Analista en sistemas":
                analistas_en_sistemas.append(empleado)

        for empleado in jefes_de_sector:
            print(empleado)

        for empleado in team_leaders:
            print(empleado)

        for empleado in desarrolladores_full_stack:
            print(empleado)

        for empleado in analistas_en_sistemas:
            print(empleado)
        print("\n")
        return True

    if sector is None and cargo is not None:
        cant = 0
        for empleado in Empleado.dict_empleados.values():
            if empleado.cargo == cargo:
                general.append(empleado)
                cant += 1

        clear()
        print(f"\nHay {cant} empleado/s en toda la empresa con el cargo {cargo}\n")

        for empleado in general:
            print(empleado)
        print("\n")
        return True

    if sector is not None and cargo is None:
        clear()
        print(f"\nHay {len(sector.empleados)} empleado/s en el sector {sector.nombre}")

        for empleado in sector.empleados:
            if empleado.cargo == "Jefe de sector":
                jefes_de_sector.append(empleado)

            if empleado.cargo == "Team leader":
                team_leaders.append(empleado)

            if empleado.cargo == "Desarrollador full stack":
                desarrolladores_full_stack.append(empleado)

            if empleado.cargo == "Analista en sistemas":
                analistas_en_sistemas.append(empleado)

        for empleado in jefes_de_sector:
            print(empleado)

        for empleado in team_leaders:
            print(empleado)

        for empleado in desarrolladores_full_stack:
            print(empleado)

        for empleado in analistas_en_sistemas:
            print(empleado)
        print("\n")

        return True

    if sector is not None and cargo is not None:
        cant = 0
        for empleado in sector.empleados:
            if empleado.cargo == cargo:
                general.append(empleado)
                cant += 1

        clear()
        print(f"\nHay {cant} empleado/s en el sector {sector.nombre} con el cargo {cargo}\n")

        for empleado in general:
            print(empleado)
        print("\n")
        return True


def ranking_de_puntos(año=None, mes=None):
    clear()
    print("Ranking de puntos\n")
    if año is None:
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

    if mes is None:
        while True:
            print("\n0- Cancelar")
            print("13- Todo el año")
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

    ranking = []

    for sector in Sector.dict_sectores.values():
        puntos = Sector.get_puntos(sector, año, mes)
        el = [sector, puntos]
        ranking.append(el)

    ranking.sort(key=lambda sec: sec[1], reverse=True)

    return ranking, año, mes


def aumento_de_salario_empleado():
    clear()
    print("Calcular el aumento de salario el próximo año para un empleado\n")

    if len(Sector.dict_sectores.keys()) == 0:
        print("No hay sectores registrados\n")
        return False

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

    ranking, año, mes = ranking_de_puntos(año, "13")
    sector = ranking[0][0]

    list_empleados = [[], [], [], []]

    if sector.empleados == []:
        print(f"\nNo hay empleados en el sector {sector.nombre}\n")
        return False

    for empleado in sector.empleados:
        if empleado.cargo == "Jefe de sector":
            list_empleados[0].append(empleado)

        if empleado.cargo == "Team leader":
            list_empleados[1].append(empleado)

        if empleado.cargo == "Desarrollador full stack":
            list_empleados[2].append(empleado)

        if empleado.cargo == "Analista en sistemas":
            list_empleados[3].append(empleado)

    n_lista = []
    for car in range(4):
        if car == []:
            continue
        for emp in list_empleados[car]:
            n_lista.append(emp)

    list_empleados = n_lista

    while True:
        contador = 0
        print("\n0- Cancelar")
        print(f"Empleados del sector {sector.nombre}:")
        for empleado in list_empleados:
            contador += 1
            print(f"{contador}- {empleado}")

        an = input("Seleccione empleado para calcularle el aumento de salario: ")

        if an == "0":
            clear()
            print("\nAcción cancelada\n")
            return False

        if an == "" or not an.isdigit() or 0 > int(an) or int(an) > contador:
            print("Opción inválida")
            continue

        empleado = list_empleados[int(an) - 1]
        break
    clear()
    print(f"\nAumento de salario para {empleado.nombre} ({empleado.ci}):")
    print(f"${empleado.salario} -----> ${round(empleado.salario * 1.15)}\n\n")


def aumento_de_salario_sector():
    clear()
    print("Calcular el aumento de salario para el próximo año de todo un sector\n")

    if len(Sector.dict_sectores.keys()) == 0:
        print("No hay sectores registrados\n")
        return False

    sector = seleccionar_sector()

    if sector.empleados == []:
        print(f"\nNo hay empleados en el sector {sector.nombre}\n")
        return False

    salario_total = 0
    for empleado in sector.empleados:
        salario_total += empleado.salario

    clear()

    print(f"\nSalario total del sector {sector.nombre}: ${salario_total}")
    print(f"Salario total del sector {sector.nombre} con aumento: ${round(salario_total * 1.15)}\n\n")