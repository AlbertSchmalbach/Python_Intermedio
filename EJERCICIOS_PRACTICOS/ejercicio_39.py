""" Haz un programa que pida al usuario una cantidad de euros, una tasa de interes y un numero de años. Muestra por pantalla en cuanto se habra convertido el capital inicial transcurridos esos años si cada año se aplica la tasa de interes introducida.
Recuerda que un capital de C euros a un interes del x por cien durante n años se convierten en C · (1 + x/100)n euros.
(Prueba tu programa sabiendo que una cantidad de 10 000 E al 4.5% de interes anual se convierte en 24 117.14 E al cabo
de 20 años.) """

cant_euros = 10000
tasa_int = 4.5
years = 20



capital_end = (1 + tasa_int/100)**years

print(f'El capital transcurridos {years} es: {capital_end} euros')