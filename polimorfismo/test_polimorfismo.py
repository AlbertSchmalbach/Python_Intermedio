from Empleado import Empleado
from Gerente import Gerente

def imprimir_detalles(objeto):
    #print(objeto)
    print(type(objeto))
    if isinstance(objeto, Gerente):
        print(objeto.departamento)


empleado1 = Empleado('Said', 1200000)
imprimir_detalles(empleado1)

gerente1 = Gerente('Alberto', 2500000, 'Contabilidad')
imprimir_detalles(gerente1)
