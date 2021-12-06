def calcular_total(s,i):
    v_impuesto = s * i/100
    total = s + v_impuesto
    print(f'Tu sueldo con impuesto es ${total}')


def main():
    sueldo = float(input('Ingrese su sueldo: $'))
    impuesto = float(input('Impuesto aplicado: '))

    calcular_total(sueldo, impuesto)

if __name__ == '__main__':
    main()