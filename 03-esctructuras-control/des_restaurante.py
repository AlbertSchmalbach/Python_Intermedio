# Entrada 
consumo = float(input('Ingrese el consumo del cliente: '))

if consumo >= 0:
    #Proceso 
    if consumo >= 10000 and consumo <= 20000:
        # Descuento de 10%
        dato_descuento = '10%'
        descuento = consumo * 0.10
    elif consumo > 20000 and consumo <= 100000:
        #Descuento de 20%
        dato_descuento = '20%'
        descuento = consumo * 0.20
    elif consumo > 200000:
        #Descuento de 30%
        dato_descuento = '30%'
        descuento = consumo * 0.30


    monto_descuento = consumo - descuento
    IVA = monto_descuento * 0.19 
    total_pagar = monto_descuento + IVA

    #Salida de datos 
    print('='*30)
    print('----- FACTURA DE CONSUMO -----')
    print('Descuento que se aplica:', dato_descuento)
    print('='*30)
    print('Consumo: ', consumo)
    print('Descuento: ', descuento)
    print('Monto con descuento: ', monto_descuento)
    print('IVA: ', IVA)
    print('Total a Pagar: ', total_pagar)
    print('='*30)

else:
    print('Error al Ingresar el consumo')