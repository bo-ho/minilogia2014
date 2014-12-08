from turtle import *
from math import *


def polowka(bok):
    forward(bok*14)
    right(135)
    forward(5*bok*sqrt(2))
    right(45)
    forward(bok*4)
    right(45)
    forward(5*bok*sqrt(2))
    left(180)
    wielkosc = 14*bok
    for i in range(5):
        wielkosc = wielkosc-2*bok
        forward(bok*sqrt(2))
        pencolor("green")
        left(45)
        forward(wielkosc)
        back(wielkosc)
        right(45)
        pencolor("black")


def polowka2(bok):
    forward(bok*14)
    left(135)
    forward(5*bok*sqrt(2))
    left(45)
    forward(bok*4)
    left(45)
    forward(5*bok*sqrt(2))
    right(180)
    wielkosc = 14*bok
    for i in range(5):
        wielkosc = wielkosc-2*bok
        forward(bok*sqrt(2))
        pencolor("green")
        right(45)
        forward(wielkosc)
        back(wielkosc)
        left(45)
        pencolor("black")


def cala(bok):
    polowka(bok)
    right(45)
    up()
    forward(bok*5)
    right(90)
    forward(bok*5)
    left(180)
    down()
    polowka2(bok)
    przejście(bok)


def przejście(bok):
    right(135)
    up()
    forward(bok*5)
    right(90)
    forward(bok*5)
    left(180)
    down()


def dojscie(ilosc,bok):
    up()
    left(90)
    forward(ilosc/2*bok*10)
    right(90)
    down()


def harmonijka(ilosc):
    left(90)
    bok=700/(10*ilosc)
    dojscie(ilosc,bok)
    forward(bok*6.5)
    for p in range(4):
        forward(bok)
        left(90)
    back(bok*6.5)
    for k in range(ilosc):
        cala(bok)
    forward(bok*6.5)
    for p in range(4):
        forward(bok)
        right(90)


