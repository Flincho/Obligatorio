from Funciones import *

if __name__ == "__main__":
    l = [54631974]

    l[0] = Empleado("Alex Ernst", 54631974, "Jefe de sector", 0, None)
    print(l[0].cargo)

    while True:
        print(Empleado.dict_empleados)
        alta_de_empleado()

        a = input("""\n0- Terminar alta de empleaddo\n1- Registrar empleado""")

        if a == "0":
            break

        if a == "1":
            continue
