from Clear import clearConsole

#Defino la clase
class Persona:
    def __init__(self, nombre, apellido, sexo, edad):
        self.nombre = nombre
        self.apellido = apellido
        self.sexo = sexo
        self.edad = edad
    
    #Defino un metodo para la clase
    def mostrarDatos(self):
        print(f'NOMBRE COMPLETO: {self.nombre} \n SEXO: {self.sexo} \n EDAD: {self.edad}')

#Limpiar la consola.
clearConsole()

#Entrada de datos
name = input('Nombre Completo: ')
lastname = input('Apellidos: ')
sex = input('Sexo: ')
age = int(input('Edad: '))

print()
#Creando objeto de la clase Persona()
persona1 = Persona(name, lastname, sex, age)

#Limpiar la consola.
clearConsole()

#Imprimo valores del objeto
#print('NOMBRE: ',persona1.nombre, persona1.apellido)
#print('SEXO: ', persona1.sexo)
#print('EDAD: ', persona1.edad)

#mando a llamar el metodo de la clase
persona1.mostrarDatos()