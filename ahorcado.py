# -*- coding: utf-8 -*-
import random


IMAGES = ['''

    +---+
    |   |
        |
        |
        |
        |
        =========''', '''
        
    +---+
    |   |
    0   |
        |
        |
        |
        =========''', '''
    
    +---+
    |   |
    0   |
    |   |
        |
        |  
        =========''','''

    +---+
    |   |
    0   |  
   /|   |
        | 
        |  
        =========''', '''

    +---+
    |   |
    0   |  
   /|\  |
        | 
        |  
        =========''', '''
        
    +---+
    |   |
    0   |  
   /|\  |
    |   | 
        |  
        =========''', '''
        
    +---+
    |   |
    0   |  
   /|\  |
    |   | 
   /    |  
        =========''', '''
        
    +---+
    |   |
    0   |  
   /|\  |
    |   | 
   / \  |  
        =========''', '''
''']

WORDS = [
    'lavadora',
    'secadora',
    'sofa',
    'gobierno',
    'computadora',
    'coronavirus',
    'familia'
]

def random_word():
    idx = random.randint(0, len(WORDS) - 1)
    return WORDS[idx]

def display_board(hidden_word,tries):
    print(IMAGES[tries])
    print('')
    print(hidden_word)
    print('--- * --- * --- * --- * --- * ---')

def run():
    word = random_word()
    hidden_word = ['-']* len(word)
    tries = 0

    while True:
        display_board(hidden_word, tries)
        current_letter = str(input('Escoge una letra: '))

        letter_indexs = []

        for idx in range(len(word)):
            if word[idx] == current_letter:
                letter_indexs.append(idx)

        if len(letter_indexs) == 0:
            tries += 1
        
            if tries == 7:
                display_board(hidden_word, tries)
                print('')
                print('La palabra correcta era: {}'.format(word))
                print('┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼')
                print('███▀▀▀██┼███▀▀▀███┼███▀█▄█▀███┼██▀▀▀')
                print('██┼┼┼┼██┼██┼┼┼┼┼██┼██┼┼┼█┼┼┼██┼██┼┼┼')
                print('██┼┼┼▄▄▄┼██▄▄▄▄▄██┼██┼┼┼▀┼┼┼██┼██▀▀▀')
                print('██┼┼┼┼██┼██┼┼┼┼┼██┼██┼┼┼┼┼┼┼██┼██┼┼┼')
                print('███▄▄▄██┼██┼┼┼┼┼██┼██┼┼┼┼┼┼┼██┼██▄▄▄')
                print('┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼')
                print('███▀▀▀███┼▀███┼┼██▀┼██▀▀▀┼██▀▀▀▀██▄┼')
                print('██┼┼┼┼┼██┼┼┼██┼┼██┼┼██┼┼┼┼██┼┼┼┼┼██┼')
                print('██┼┼┼┼┼██┼┼┼██┼┼██┼┼██▀▀▀┼██▄▄▄▄▄▀▀┼')
                print('██┼┼┼┼┼██┼┼┼██┼┼█▀┼┼██┼┼┼┼██┼┼┼┼┼██┼')
                print('███▄▄▄███┼┼┼─▀█▀┼┼─┼██▄▄▄┼██┼┼┼┼┼██▄')
                print('┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼')
                print('┼┼┼┼┼┼┼┼██┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼██┼┼┼┼┼┼┼┼┼')
                print('┼┼┼┼┼┼████▄┼┼┼▄▄▄▄▄▄▄┼┼┼▄████┼┼┼┼┼┼┼')
                print('┼┼┼┼┼┼┼┼┼▀▀█▄█████████▄█▀▀┼┼┼┼┼┼┼┼┼┼')
                print('┼┼┼┼┼┼┼┼┼┼┼█████████████┼┼┼┼┼┼┼┼┼┼┼┼')
                print('┼┼┼┼┼┼┼┼┼┼┼██▀▀▀███▀▀▀██┼┼┼┼┼┼┼┼┼┼┼┼')
                print('┼┼┼┼┼┼┼┼┼┼┼██┼┼┼███┼┼┼██┼┼┼┼┼┼┼┼┼┼┼┼')
                print('┼┼┼┼┼┼┼┼┼┼┼█████▀▄▀█████┼┼┼┼┼┼┼┼┼┼┼┼')
                print('┼┼┼┼┼┼┼┼┼┼┼┼███████████┼┼┼┼┼┼┼┼┼┼┼┼┼')
                print('┼┼┼┼┼┼┼┼▄▄▄██┼┼█▀█▀█┼┼██▄▄▄┼┼┼┼┼┼┼┼┼')
                print('┼┼┼┼┼┼┼┼▄▄▄██┼┼█▀█▀█┼┼██▄▄▄┼┼┼┼┼┼┼┼┼')
                print('┼┼┼┼┼┼┼┼▀▀██┼┼┼┼┼┼┼┼┼┼┼██▀▀┼┼┼┼┼┼┼┼┼')
                print('┼┼┼┼┼┼┼┼┼┼▀▀┼┼┼┼┼┼┼┼┼┼┼▀▀┼┼┼┼┼┼┼┼┼┼┼')
                print('┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼')
                print('')
                break

        else: 
            for idx in letter_indexs:
                hidden_word[idx] = current_letter
            
            letter_indexs = []
        try:
            hidden_word.index('-')
        except ValueError:
            print('¡Felicidades! Ganaste. La palabra es:  {}'.format(word))
            print('')  
            print(' _____ _____ _____ _____ _____ _____ _____') 
            print('|   __|  _  |   | |  _  |   __|_   _|   __|') 
            print('|  |  |     | | | |     |__   | | | |   __|') 
            print('|_____|__|__|_|___|__|__|_____| |_| |_____|') 
            print('') 
            break




if __name__ == "__main__":
    print('B I E N V E N I D O S   A   H O R C A D O S')
    run()
       
