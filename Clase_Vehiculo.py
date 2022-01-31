class Vehiculo():
    def __init__(self, color, ruedas):
        self.color = color
        self.ruedas = ruedas
        
    def __str__(self):
        return f'(Vehiculo):\nColor=>{self.color}\nRuedas=> {self.ruedas} \n' 
    

class Coche(Vehiculo):
    def __init__(self, color, ruedas, velocidad):
        super().__init__(color, ruedas)
        self.velocidad = velocidad
        
    def __str__(self):
        return f'Coche{super().__str__()}Velocidad=>{self.velocidad}'
    
class Bicicleta(Vehiculo):
    def __init__(self, color, ruedas, tipo):
        super().__init__(color, ruedas)
        self.tipo = tipo
        
    def __str__(self):
        return f'Bicicleta{super().__str__()}Tipo=>{self.tipo}'
    
    
#Pruebas 
#Clase vehiculo
Vehiculo1 = Vehiculo('Gris', 4)
print(Vehiculo1)
print(30 * '*')
#Clase coche
coche1 = Coche('Blue',4, '200km/h')
print(coche1)
print(30 * '*')
#Clase Bicicleta
bicicleta1 = Bicicleta('Plateado', 2, 'Montaña')
print(bicicleta1)
print(30 * '*')             
              