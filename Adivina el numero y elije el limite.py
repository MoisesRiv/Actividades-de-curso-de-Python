# -*- coding: utf-8 -*-
import random

def run():
    num_chosen = int(input('Ingresa el numero máximo: '))
    number_found = False
    random_number = random.randint(0, num_chosen)

    you_lost = random_number -1    

    while not number_found:
        number = int(input('Intenta adivinar cual es el número aleatorio: '))

        if number == random_number:
            print('Felicidades. Encontraste el número')
            number_found = True
        elif number > random_number:
            print('El número es más pequeño')
        else:
            print('El número es más grande')



if __name__ == '__main__':
    run()