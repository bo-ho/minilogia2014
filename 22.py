from turtle import *
from math import *


def kwardat(bok):
    for i in range(4):
        forward(bok)
        left(90)


def dosrodkowanie():
    up()
    back(20)
    right(90)
    forward(20)
    left(90)
    down()


def pole(ilosc):
    bok=0
    for ki in range(ilosc):
        bok=bok+40
        kwardat(bok)
        dosrodkowanie()


def posadzka(ilosc):
    dosrodkowanie()
    pole(ilosc)
    up()
    forward(40)
    right(90)
    dosrodkowanie()
    left(135)
    przekatna=40*ilosc*sqrt(2)/2
    forward(przekatna)
    left(45)
    for lk in range(4):
        forward(ilosc*20)
        back(ilosc*20)
        right(90)
    right(45)
    for rd in range(4):
        forward(przekatna)
        back(przekatna)
        right(90)

posadzka(5)
