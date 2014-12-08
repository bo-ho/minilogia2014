from turtle import *


def drzewo(dlugosc, rzad):
    forward(dlugosc)
    if rzad>1:
        left(45)
        drzewo(dlugosc/2,rzad-1)
        right(90)
        drzewo(dlugosc/2,rzad-1)
        left(45)
    back(dlugosc)

rzad = numinput("Drzewo binarne", "Który poziom?", 4, minval=1, maxval=10)
speed(0)
left(90)
drzewo(100, rzad)
done()