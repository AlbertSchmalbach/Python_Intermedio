class Persona():
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
    
    def __str__(self):
        return f'Persona:\nNombre=>{self.nombre}\nEdad=> {self.edad} \n' 
      
 #Herencia        
class Empleado(Persona):
    def __init__(self,nombre, edad, sueldo):
        super().__init__(nombre, edad)
        self.sueldo = sueldo
    
    def __str__(self):
        return f'Empleado {super().__str__()}Sueldo=> {self.sueldo}' 
        
