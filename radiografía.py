from radiacionerror import RadiacionError


class Radiografia:
    MAX_DOSIS = 5.0  # Máxima dosis permitida en mSv
    MAX_DURACION = 30  # Máxima duración permitida en segundos

    def __init__(self, dosis: float, duracion: int):
        self.dosis = dosis
        self.duracion = duracion

    @property
    def dosis(self):
        return self._dosis

    @dosis.setter
    def dosis(self, valor):
        if valor < 0 or valor > self.MAX_DOSIS:
            raise RadiacionError("Dosis fuera de rango", valor, self.MAX_DOSIS)
        self._dosis = valor

    @property
    def duracion(self):
        return self._duracion

    @duracion.setter
    def duracion(self, valor):
        if valor < 1 or valor > self.MAX_DURACION:
            raise RadiacionError("Duración fuera de rango", valor, self.MAX_DURACION)
        self._duracion = valor
