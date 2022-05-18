def main():
    list_compress = [i**2 for i in range(1,101) if i % 3 == 0]
    print('Numeros divisibles x 3 elevados al cuadrado: ',list_compress )
    print()
    print("===============================================================================")
    print()
    dict_compress = {i:i**3 for i in range(1,101) if i % 3 == 0 }
    print('Numeros divisibles x 3 elevados al cubo: ', dict_compress)

if __name__ == '__main__':
    main()