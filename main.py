from Alta_de_empleado import *
from Alta_de_sector import *
from Empleado_a_sector import *
from Otorgar_puntos import *
from Consultas import *

if __name__ == "__main__":
    clear()
    print(f"Bienvenido al software de gestión de {Sector.nombre_empresa.upper()}\n")

    while True:

        print("0- Cerrar programa")
        print("""Opciones:
        1- Alta de empleado
        2- Alta de sector
        3- Asignar empleado a sector
        4- Otorgar puntos a sector
        5- Realizar consultas
        """)

        op = input("Ingrese una opción: ")

        if op == "1":
            while True:
                alta_de_empleado()
                a = input("""\n1- Registrar otro empleado\nCualquier otra tecla para terminar\n""")

                if a == "1":
                    continue

                clear()
                break

        if op == "2":
            while True:
                alta_de_sector()
                a = input("""\n1- Registrar otro sector\nCualquier otra tecla para terminar\n""")

                if a == "1":
                    clear()
                    continue

                clear()
                break

        if op == "3":
            asignar_empleado_a_sector()

        if op == "4":
            otorgar_puntos()

        if op == "5":
            clear()
            while True:
                print("0- Cancelar consulta")
                print("""Consultas:
        1- Cantidad de empleados
        2- Ranking de puntos
        3- Calcular aumento de sueldo para empleado de sector con más puntos
        4- Calcular aumento de sueldos para sector
        """)
                an = input("Seleccione una consulta:")

                if an == "0":
                    clear()
                    break

                if an == "1":
                    clear()
                    cantidad_de_empleados()

                if an == "2":
                    clear()
                    ranking, año, mes = ranking_de_puntos()

                    clear()
                    if mes == "13":
                        print(f"Ranking de puntos del año {año}\n")

                    else:
                        print(f"Ranking de puntos del mes {mes} del año {año}\n")

                    for sec in ranking:
                        print(f"{sec[0].nombre}: {sec[1]} puntos")

                    print("\n")

                if an == "3":
                    clear()
                    aumento_de_salario_empleado()

                if an == "4":
                    clear()
                    aumento_de_salario_sector()

        if op == "0":
            clear()
            print("\n\nCerrando Programa\n\n")
            print("................................................................................\n\n")
            break
