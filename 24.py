from turtle import *
from math import*



def polowka(szerokosc, dlugosc):
    forward(20)
    right(45)
    forward(20*sqrt (2))
    left(45)
    forward(dlugosc)
    left(45)
    forward(20*sqrt (2))
    left(45)
    forward(szerokosc)
    left(45)
    forward(20*sqrt (2))
    left(45)
    forward(dlugosc)
    left(45)
    forward(20*sqrt (2))
    right(45)

def polowka2(szerokosc,dlugosc):
    forward(20)
    right(45)
    forward(20*sqrt (2))
    left(45)
    forward(dlugosc)
    left(45)
    forward(20*sqrt (2))
    left(45)
    forward(szerokosc)
    left(45)
    forward(20*sqrt (2))
    left(45)
    forward(dlugosc)
    left(45)
    forward(20*sqrt(2))
    right(45)


def dosrodkowanie():
    up()
    right(90)
    forward(10)
    left(90)
    back(10)
    down()


def przejscie():
    up()
    right(90)
    forward(10)
    left(90)
    down()

def matryjoszka(dlugosc_dolnej, dlugosc_gornej,szerokosc):
    polowka(szerokosc,dlugosc_gornej)
    polowka2(szerokosc,dlugosc_dolnej)

def matrioszka(ilosc):
    left(90)
    dosrodkowanie()
    szerokosc=20
    dlugosc_gornej=20
    dlugosc_dolnej=20
    for k in range(ilosc):
        matryjoszka(dlugosc_dolnej, dlugosc_gornej, szerokosc)
        dlugosc_gornej=dlugosc_gornej+10
        dlugosc_dolnej=dlugosc_dolnej+20
        szerokosc=szerokosc+20
        przejscie()


matrioszka(3)
done()