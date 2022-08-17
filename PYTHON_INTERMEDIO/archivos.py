def operacion():
    numeros = []
    with open('./archivos/numeros.txt', 'r', encoding='utf-8') as file:
        for n in file:
            numeros.append(int(n))
    
    suma = 0
    for i in numeros:
        suma+= i

    cuadrado = [n**2 for n in numeros]

    def printer():
        with open('./archivos/resultados.txt', 'w', encoding='utf-8') as f:
            n = 0
            for d in cuadrado:
                linea = str(numeros[n]) + ' al cuadrado es: ' + str(d)
                f.write(linea)
                f.write("\n")
                n+=1
                

    printer()
    print(suma)
    print(cuadrado)


def main():
    operacion()
if __name__ == '__main__':
    main()