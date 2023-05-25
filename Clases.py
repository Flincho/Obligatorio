class Empleado:

    def __init__(self, nombre, ci, cargo, salario, supervisor) -> None:
        self.nombre = nombre
        self.ci = ci
        self.cargo = cargo
        self.salario = salario
        self.supervisor = supervisor
        self.sector = None
        Empleado.dict_empleados[self.ci] = self

    dict_empleados = {}


class Sector:

    def __init__(self, nombre) -> None:
        self.nombre = nombre
        self.jefe = None
        self.team_leaders = []
        self.empleados = []

        # Se podría usar un diccionario para guardar los puntos par año y mes
        self.puntos = []
        Sector.dict_sectores[self.nombre] = self

    dict_sectores = {}

    nombre_empresa = "Flin Design"

    def set_empleado(self, empleado):
        self.empleados.append(empleado)

        if empleado.cargo == "Jefe de sector":
            if self.jefe == None:
                self.jefe = empleado
                return "\nJefe de sector establecido"

            self.jefe = empleado
            return "\nJefe de sector modificado"

        if empleado.cargo == "Team leader":
            self.team_leaders.append(empleado)
            return "\nNuevo Team leader"


class Equipo:

    def __init__(self, sector) -> None:
        self.sector = sector
        self.team_leader = None
        self.empleados = []
        self.puntos = 0
        Equipo.lista_equipos.append(self)

    lista_equipos = []
