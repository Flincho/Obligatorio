from Alta_de_empleado import *
from Alta_de_sector import *
from Empleado_a_sector import *
from Otorgar_puntos import *
from Consultas import *

if __name__ == "__main__":
    tests()
    clear()
    print(f"Bienvenido al software de gestión de {Sector.nombre_empresa.upper()}\n")

    while True:
        print("""Opciones:
    1- Alta de empleado
    2- Alta de sector
    3- Asignar empleado a sector
    4- Otorgar puntos a sector
    5- Realizar consultas
    6- Cerrar programa
    """)

        op = input("Ingrese una opción: ")

        if op == "1":
            while True:
                alta_de_empleado()
                a = input("""1- Registrar otro empleado\nCualquier otra tecla para terminar\n""")

                if a == "1":
                    continue

                clear()
                break
            continue

        if op == "2":
            while True:
                alta_de_sector()
                a = input("1- Registrar otro sector\nCualquier otra tecla para terminar\n")

                if a == "1":
                    clear()
                    continue

                clear()
                break
            continue

        if op == "3":
            asignar_empleado_a_sector()
            continue

        if op == "4":
            otorgar_puntos()
            continue

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
                    continue

                if an == "2":
                    clear()
                    ranking()
                    continue

                if an == "3":
                    clear()
                    aumento_de_salario_empleado()
                    print("")
                    continue

                if an == "4":
                    clear()
                    aumento_de_salario_sector()
                    continue

                clear()
                print("Opción inválida\n")
            continue

        if op == "6":
            clear()
            print("Cerrando Programa\n\n")
            print("................................................................................\n\n")
            break

        clear()
        print("Opción inválida\n")
