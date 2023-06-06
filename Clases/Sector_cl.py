class Sector:

    def __init__(self, nombre) -> None:
        self._nombre = nombre
        self._jefe = None
        self._team_leaders = []
        self._empleados = []
        self._puntos = [0 for i in range(12)]
        Sector.dict_sectores[self._nombre] = self

    dict_sectores = {}

    nombre_empresa = "Flin Design"
#
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
            if self._jefe is not None:
                self._empleados.remove(self._jefe)
                self._jefe.cargo = None
                self._jefe = empleado
                print("Jefe de sector modificado\n")

            else:
                self._jefe = empleado
                print("Jefe de sector establecido\n")

        if empleado.cargo == "Team leader":
            self._team_leaders.append(empleado)
            print("Nuevo Team leader\n")

    def get_puntos(self, mes):

        if mes == 13:
            return sum(self._puntos)

        return self._puntos[mes-1]
    
    def set_puntos(self, mes, nuevos_puntos):

        self._puntos[mes-1] += nuevos_puntos
