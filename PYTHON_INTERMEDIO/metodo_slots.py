class MiClase(object):
    def __init__(self, nombre, identificador):
        self.nombre = nombre
        self.identificador = identificador
        self.iniciar()


# El segundo código reducirá el uso de RAM.
class MiClase(object):
    __slots__ = ['nombre', 'identificador']
    def __init__(self, nombre, identificador):
        self.nombre = nombre
        self.identificador = identificador
        self.iniciar()