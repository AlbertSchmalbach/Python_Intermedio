def numDescent(numero):
    if numero > 0:
        print(numero)
        return numDescent(numero-1)

        
def run():

    numDescent(7)

if __name__ == '__main__':
    run()