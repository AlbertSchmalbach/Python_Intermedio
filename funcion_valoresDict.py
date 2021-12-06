def valoresDict(**valores):
    for key, values in valores.items():
        print(f'{key}:{values}')


def main():

    valoresDict(SENA='Servicio Nacional de Aprendizaje', ICA='Instituto Nacional Agropecuario')

if __name__== '__main__':
    main()