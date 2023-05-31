class Empleado:

    def __init__(self, nombre, ci, cargo, salario) -> None:
        self._nombre = nombre
        self._ci = ci
        self._cargo = cargo
        self._salario = salario
        self._sector = None
        Empleado.dict_empleados[self.ci] = self

    dict_empleados = {}

    def __str__(self):
        if self.sector is not None:
            return f"{self._nombre} ({self.ci}) {self._cargo} - {self._sector.nombre} - ${self._salario}"
        return f"{self.nombre} ({self.ci}) {self._cargo} - ${self._salario}"

    @property
    def nombre(self):
        return self._nombre

    @property
    def ci(self):
        return self._ci

    @property
    def cargo(self):
        return self._cargo

    @property
    def salario(self):
        return self._salario

    @property
    def sector(self):
        return self._sector

    @sector.setter
    def sector(self, sector):
        self._sector = sector


class Sector:

    def __init__(self, nombre) -> None:
        self._nombre = nombre
        self._jefe = None
        self._team_leaders = []
        self._empleados = []
        self._puntos = {}
        Sector.dict_sectores[self._nombre] = self

    dict_sectores = {}

    nombre_empresa = "Flin Design"

    @property
    def nombre(self):
        return self._nombre

    @property
    def jefe(self):
        return self._jefe

    @property
    def team_leaders(self):
        return self._team_leaders

    @property
    def empleados(self):
        return self._empleados

    @empleados.setter
    def empleados(self, empleado):
        self._empleados.append(empleado)

        if empleado.cargo == "Jefe de sector":
            if self._jefe is None:
                self._jefe = empleado
                print("\nJefe de sector establecido")

            self._jefe = empleado
            print("\nJefe de sector modificado")

        if empleado.cargo == "Team leader":
            self._team_leaders.append(empleado)
            print("\nNuevo Team leader")

    def get_puntos(self, año, mes):

        if año not in self._puntos.keys():
            return 0

        if mes == "13":
            return sum(self._puntos[año].values())

        if mes not in self._puntos[año].keys():
            self._puntos[año][mes] = 0

        return self._puntos[año][mes]

    def set_puntos(self, año, mes, nuevos_puntos):

        if año not in self._puntos.keys():
            self._puntos[año] = {}

        if mes not in self._puntos[año].keys():
            self._puntos[año][mes] = 0

        self._puntos[año][mes] += nuevos_puntos
