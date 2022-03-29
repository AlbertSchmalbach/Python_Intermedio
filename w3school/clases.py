class Perro:
    contadorPerro = 0
    def __init__(self, raza, peso):
        Perro.contadorPerro+=1
        self.id = Perro.contadorPerro
        self.raza = raza
        self.peso = peso
        

    def __str__(self):
        print(f'RAZA: {self.raza} PESO: {self.peso}')


class myCan(Perro):
    def __init__(self,raza, peso, nombre):
        super().__init__(raza, peso)
        self.nombre = nombre

    def __str__(self):
        return f' ID: {self.id} \n NOMBRE: {self.nombre} \n RAZA: {self.raza}\n PESO: {self.peso}kg'


myCan1 = myCan('Border Colly', 20, 'Firulais')
myCan2 = myCan('Doberman', 30, 'Baltor')

print(myCan1)
print()
print(myCan2)