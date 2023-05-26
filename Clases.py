class Empleado:

    def __init__(self, nombre, ci, cargo, salario, supervisor) -> None:
        self.nombre = nombre
        self.ci = ci
        self.cargo = cargo
        self.salario = salario
        self.supervisor = supervisor
        self.sector = None
        Empleado.dict_empleados[self.ci] = self
    
    #diccionario que guarda todos los empleados, llave: ci, valor: objeto empleado
    dict_empleados = {}

    def __str__(self):
        return f"{self.nombre} ({self.ci}) {self.cargo} - ${self.salario}"


class Sector:

    def __init__(self, nombre) -> None:
        self.nombre = nombre
        self.jefe = None
        self.team_leaders = []
        self.empleados = []
        self.puntos = {}
        Sector.dict_sectores[self.nombre] = self
#Jefe como none porque hay uno solo, team leaders como lista porque puede haber mas de uno
    dict_sectores = {}

    nombre_empresa = "Flin Design"

    def set_empleado(self, empleado):
        self.empleados.append(empleado)

        if empleado.cargo == "Jefe de sector":
            if self.jefe is None:
                self.jefe = empleado
                return "\nJefe de sector establecido"

            self.jefe = empleado
            return "\nJefe de sector modificado"

        if empleado.cargo == "Team leader":
            self.team_leaders.append(empleado)
            return "\nNuevo Team leader"

    def set_puntos(self, año, mes, nuevos_puntos):

        if año not in self.puntos.keys():
            self.puntos[año] = {}

        if mes not in self.puntos[año].keys():
            self.puntos[año][mes] = 0

        self.puntos[año][mes] += nuevos_puntos

    def get_puntos(self, año, mes):

        if año not in self.puntos.keys():
            return 0

        if mes == "13":
            return sum(self.puntos[año].values())

        if mes not in self.puntos[año].keys():
            self.puntos[año][mes] = 0

        return self.puntos[año][mes]
