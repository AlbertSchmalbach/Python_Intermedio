from Clear import clearConsole

def run():
    #lista de diccionario
    products_electronics = [
        {'nombre':'Smart Tv','precio':800000, 'garantia':'1 año'},
        {'nombre':'Celular Samsung S5','precio':500000, 'garantia':'2 años'},
        {'nombre':'Laptop lenovo','precio':1800000, 'garantia':'2 años'},
        {'nombre':'Auricolares Sony','precio':85000, 'garantia':'6 meses'},
        {'nombre':'ventilador Samuray','precio':120000, 'garantia':'1 año'}
    ]


    # diccionario de lista
    numeros = {
        'pares':[2, 4,6,8,10,12],
        'impares':[1,3,5,7,9,11]
    }

    clearConsole()

    for producto in products_electronics:
        for key, value in producto.items():
            print(key, " = ", value)
           


if __name__=='__main__':
    run()