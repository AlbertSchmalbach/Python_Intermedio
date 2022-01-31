from Clear import clearConsole

#CREO LA CLASE
class Rectangulo:

    """
        AREA DE UN RECTANGULO

    """
    #METODO CONSTRUCTOR DE OBJETOS
    def __init__(self, altura, base):
        self.altura = altura
        self.base = base

    #METODO DE LA CLASE
    def calculaArea(self):
        return self.base * self.altura

clearConsole()

b = float(input('La base del rectangulo es: '))
a = float(input('La altura del rectangulo es: '))

#CREAR UN OBJETO RECTANGULO EN BASE A LA CLASE
rectangulo1 = Rectangulo(b,a)

area = rectangulo1.calculaArea()

print(f'El area del rectangulo es: {area}')