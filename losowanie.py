from turtle import *
from random import *
from math import *

def plot():
    left(90)
    for k in range(5):
        kolor=["green","red"]
        fillcolor(kolor[randint(0,1)])
        begin_fill()
        for i in range(2):
            forward(80)
            left(90)
            forward(20)
            left(90)
        end_fill()
        up()
        right(90)
        forward(20)
        left(90)
        down()


def kwardat(bok):
    for i in range(4):
        forward(bok)
        left(90)


def przejscie(liczba):
    up()
    forward(50/liczba)
    left(90)
    forward(50/liczba)
    right(90)
    down()

def tarcza():
    left(90)
    liczba=randint(2,7)
    bok=100
    for m in range(liczba):
        pencolor(random(),random(),random())
        kwardat(bok)
        przejscie(liczba)
        bok=bok-100/liczba
