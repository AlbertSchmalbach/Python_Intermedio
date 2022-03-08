import math

#CLASE PADRE
class Figura:
    def __init__(self, nombre):
        self.nombre = nombre

    def calc_area(self):
        pass

    def calc_perimetro(self):
        pass
#CLASE RECTANGULO
class Rectangulo(Figura):
    def __init__(self, nombre, base, altura):
        super().__init__(nombre)
        self.base = base
        self.altura = altura

    def calc_area(self):
        return f'{(self.base)*(self.altura)} cm'

    def calc_perimetro(self):
        return f'{2*(self.base)+2*(self.altura)} cm'

    def __str__(self):
        return f'{self.nombre}[base:{self.base} altura:{self.altura}]'

#CLASE CIRCULO
class Circulo(Figura):
    def __init__(self, nombre, radio):
        super().__init__(nombre)
        self.radio = radio

    def calc_area(self):
        return f'{round(math.pi*(math.pow(self.radio,2)),2)} cm'

    def calc_perimetro(self):
        return f'{round(2 * math.pi * self.radio,2)} cm'

    def __str__(self) -> str:
        return f'{self.nombre}[Radio: {self.radio}]'

#METODO PARA PROBAR CLASES
def probar_figura(figura):
    print(figura)
    print('Area: ', figura.calc_area())
    print('Perimetro: ', figura.calc_perimetro())

#PRUEBA
rect1 = Rectangulo('Rectangulo', 4, 8)
probar_figura(rect1)
circle1 = Circulo('Circulo', 4)
probar_figura(circle1)


        