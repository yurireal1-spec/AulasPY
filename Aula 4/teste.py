import os
continuar= "sim"

while continuar.lower() == "sim":
    os.system('cls')
    base= float(input("base: "))
    altura= float(input("altura: "))

    print('A area do triangulo é {}'.format(base * altura))
    continuar= input('deseja continuar? : ')
