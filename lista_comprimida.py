from faulthandler import disable


par = [i for i in range(1,50) if i % 2 == 0]

impar = [i for i in range(1,50) if i % 2 != 0]

disct_comprimido = {i: i**2 for i in range(1, 21) if i % 2 == 0}



print('PAR=> ',par)
print('IMPAR=> ', impar)
print('DISCT=> ', disct_comprimido)