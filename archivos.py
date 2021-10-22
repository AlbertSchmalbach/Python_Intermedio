from list_and_dicts import clearConsole

def read():
    numbers= []

    with open('./archivos/numeros.txt', 'r', encoding='utf-8') as f:
        for line in f:
            numbers.append(int(line))
    numbers.sort()
    print(numbers)


def write():
    #names = ['Alberto', 'Camila', 'Sofia', 'Juan', 'Lisa']
    names = ['Maria Fernanda', 'Andrea']
    with open('./archivos/names.txt', 'a', encoding='utf-8') as f:
        for name in names:
            f.write(name)
            f.write('\n')


def main():
    clearConsole()
    
    write()


if __name__  == '__main__':
    main()