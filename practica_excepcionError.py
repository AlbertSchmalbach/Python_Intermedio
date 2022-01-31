from Clear import clearConsole

def validaCorreo(correo):
    
    if ('@' in correo and '.' in correo) and ('gmail' in correo or 'outlook' in correo or 'yahoo' in correo or 'hotmail' in correo):
        print('formato de correo valido')
    else:
        print('formato invalido')
    

def run():
    clearConsole()
    try:
        correo = input('Por favor, ingrese su correo: ')
        if not correo.isspace():
            validaCorreo(correo)
    except:
        print('No se puede dejar vacio')

   
    

if __name__ == '__main__':
    run()