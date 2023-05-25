from Funciones import *

if __name__ == "__main__":
    print(f"Bienvenido al software de gestión de {Sector.nombre_empresa.upper()}\n\n")

    test = [54631974, 55555555, 77777777, 66666666]
    test[0] = Empleado("Alex Ernst", 54631974, "Jefe de sector", 0, None)
    test[1] = Empleado("Sol Pereira", 55555555, "Team leader", 0, test[0])
    test[2] = Empleado("Fernando Alonso", 77777777, "Analista en sistemas", 0, test[1])
    test[3] = Empleado("Carlos Sainz", 66666666, "Desarrollador full stack", 0, test[1])

    while True:

        print("""Opciones:
        1- Alta de empleado
        2- Alta de sector
        3- Asignar empleado a sector
        4- Otorgar puntos a sector
        5- Realizar consultas
        6- Salir\n""")

        op = input("Ingrese una opción: ")

        if op == "1":
            while True:
                alta_de_empleado()
                a = input("""\n1- Registrar otro empleado\nCualquier otra tecla para terminar\n""")

                if a == "1":
                    continue

                break

        if op == "2":
            while True:
                alta_de_sector()
                a = input("""\n1- Registrar otro sector\nCualquier otra tecla para terminar\n""")

                if a == "1":
                    continue

                break

        if op == "3":
            asignar_empleado_a_sector()

        if op == "6":
            print("\n\nCerrando Programa")
            print("...............................................................................")
            break

