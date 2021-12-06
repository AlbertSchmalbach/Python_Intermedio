from Clear import clearConsole
    
def main():
    list_dicts = [
        {'nombre':'Alberto', 'edad': 38},
        {'nombre':'Nazly', 'edad': 27},
        {'nombre':'Jose', 'edad': 40},
        {'nombre':'Saul', 'edad': 24},
        {'nombre':'Maria Fernanda', 'edad': 25}
    ]

    dict_list = {
        'num_par': [2,4,6,8],
        'num_impar':[3,5,7,9],
        'vocales':['a','e','i','o','u'],
        'consonantes':['a','b','c','d','e','f','g','h']
    }

    clearConsole()

    """ for i in list_dicts:
        print(i) """

    """ for key, value in dict_list.items():
        print(key, ' : ' , value) """

    dato = list(filter(lambda nombre: nombre['edad'] > 35, list_dicts))
    print(dato)

if __name__ == '__main__':
    main()