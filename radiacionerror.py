class RadiacionError(Exception):
    def __init__(self, mensaje, valor, limite):
        super().__init__(mensaje)
        self.mensaje = mensaje
        self.valor = valor
        self.limite = limite

    def __str__(self):
        return f"{self.mensaje}. Valor recibido: {self.valor}, límite permitido: {self.limite}"
