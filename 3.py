from turtle import *

def drzewo(rzad, dlugosc):
    left(90)
    drzewa(rzad, dlugosc)


def drzewa(rzad, dlugosc):
    forward(dlugosc)
    if rzad>1:
        left(120)
        drzewa(rzad-1, dlugosc/2)
        right(120)
        drzewa(rzad-1, dlugosc/2)
        right(120)
        drzewa(rzad-1,dlugosc/2)
        left(120)
    back(dlugosc)


def tunel(bok):
    forward(bok/2)
    for lm in range(4):
        left(90)
        forward(bok)
    back(bok/2)
    if (bok > 20):
        tunel(bok-20)