from Clear import clearConsole

def palindrome(cadena):
    assert len(cadena)>0, 'No se puede ingresar una cadena vacia' 
    texto =(cadena == cadena[::-1]) 
    if texto == True:
        return f'{cadena} es palindromo'
    else:
        return f'{cadena} no es palindromo'
       
     

clearConsole()
print(palindrome('olo'))