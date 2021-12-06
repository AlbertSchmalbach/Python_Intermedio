def suma(*number):
    s=0
    for n in number:
        s+=n
    print(s)

def mult(*values):
    m=1
    for n in values:
        m*=n
    print(m)

def run():
    suma(10,25,30)
    mult(10,200)
if __name__ == '__main__':
    run()