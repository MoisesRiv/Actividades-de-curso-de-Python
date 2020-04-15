# -*- coding: utf-8 -+-
import turtle

def main():
    window = turtle.Screen()
    moy = turtle.Turtle()
    makeSquare(moy)
    turtle.mainloop()

def makeSquare(moy):
    length = int(input('Tamaño de polígono: '))
    part = int(input('Cantidad de lados: '))
    for i in range(part):
        makeLineAndTurn(moy, length, part)

def makeLineAndTurn(moy, length, part):
    part = 360 / part
    moy.forward(length)
    moy.left(part)

if __name__ == '__main__':
    main()