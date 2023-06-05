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
