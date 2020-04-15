# -*- coding: utf-8 -+-
import turtle

def main():
    window = turtle.Screen()
    moy = turtle.Turtle()

    make_square(moy)
    turtle.mainloop()

def make_square(moy):
    length = int(input('Tamaño de cuadrado:'))
    for i in range(4):
        make_line_and_turn(moy, 100)
    
def make_line_and_turn(moy, length):
    moy.forward(length)
    moy.left(90)


if __name__ == '__main__':
    main()