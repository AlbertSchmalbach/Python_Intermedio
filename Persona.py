from Clear import clearConsole

# Defino la clase


class Persona:
    def __init__(self, nombre, apellido, sexo, edad, *valores, **terminos):
        # Encapsulacion(Sugerencia sintaxtica. No tiene efecto sobre el atributo)
        self._nombre = nombre
        self._apellido = apellido
        self._sexo = sexo
        self._edad = edad
        self.valores = valores
        self.terminos = terminos

        #GETTER
    @property
    def nombre(self):
        return self._nombre
        #SETTER
    @nombre.setter
    def nombre(self, nombre):
        self._nombre = nombre
            
    @property
    def apellido(self):
        return self._apellido
        
    @apellido.setter
    def apellido(self, apellido):
        self._apellido = apellido
        
    @property
    def sexo(self):
        return self._sexo
        
    @sexo.setter
    def sexo(self, sexo):
        self._sexo = sexo
            
    @property
    def edad(self):
        return self._edad
        
    @edad.setter
    def edad(self, edad):
        self._edad = edad
            

    # Defino un metodo para la clase
    def mostrarDatos(self):
        print(
            f'NOMBRE COMPLETO: {self._nombre} \n APELLIDO: {self._apellido} \n SEXO: {self._sexo} \n EDAD: {self._edad} \n NOVIAS: {self.valores} \n SUELDO: {self.terminos}')

    def __del__(self):
        print(f'Eliminando: {self._nombre} {self._apellido}')

# Limpiar la consola.
clearConsole()

# Entrada de datos
name = input('Nombre Completo: ')
lastname = input('Apellidos: ')
sex = input('Sexo: ')
age = int(input('Edad: '))

print()
# Creando objeto de la clase Persona()
persona1 = Persona(name, lastname, sex, age, 'Nazly', 'Silvana', 'Maria Fernanda', sueldo=7500000,ubicacion='Magangue')

# Limpiar la consola.
clearConsole()

# Imprimo valores del objeto
#print('NOMBRE: ',persona1.nombre, persona1.apellido)
#print('SEXO: ', persona1.sexo)
#print('EDAD: ', persona1.edad)

if __name__ == '__main__':
    #Modificando el atributo con el settter. No se recomienda mientras lleve un guion, es encapsulado sintaxtico.
    persona1.nombre = 'Juan'
    persona1.apellido = 'Tobias Moretti'
    persona1.edad = 28
    # mando a llamar el metodo de la clase

    #persona1.mostrarDatos()
    print(__name__)
