def leerFile():
    person = dict()
    with open('datos.txt', 'r', encoding='utf-8') as datos:

        names = datos.readlines()
        datos.close()
        print(names)
        names = list(names[0])
        
        for name in names:
            print(name)


leerFile()


        

