class Empleado:

    def __init__(self, nombre, ci, cargo, salario, supervisor) -> None:
        self.nombre = nombre
        self.ci = ci
        self.cargo = cargo
        self.salario = salario
        self.supervisor = supervisor
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
        Sector.lista_sectores.append(self)

    lista_sectores = []


class Equipo:

    def __init__(self, sector) -> None:
        self.sector = sector
        self.team_leader = None
        self.empleados = []
        self.puntos = 0
        Equipo.lista_equipos.append(self)

    lista_equipos = []
