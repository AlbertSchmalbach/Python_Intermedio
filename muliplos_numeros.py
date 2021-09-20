from list_and_dicts import clearConsole

def main():
    lista_multiplos = []

    mult_cuatro = []
    mult_seis = []
    mult_nueve = []

    cant = 10000

    resultado = 0
    [mult_cuatro.append(4*i) for i in range(1, cant+1)]
    [mult_seis.append(6*i) for i in range(1, cant + 1)]
    [mult_nueve.append(9*i) for i in range(1, cant + 1)]

    """ print(mult_cuatro)
    print(mult_seis)
    print(mult_nueve) """

    for a in mult_cuatro:
        for b in mult_seis:
            for c in mult_nueve:
                if a == b == c:
                    lista_multiplos.append(a)

    print(lista_multiplos)

if __name__ == '__main__':
    main()