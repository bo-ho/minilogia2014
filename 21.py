from turtle import *
from math import *

def trojkacik():
    fillcolor("olive")
    begin_fill()
    forward(20)
    left(90)
    forward(20)
    left(135)
    forward(sqrt(800))
    end_fill()
    right(45)


def wiatraczek():
    for i in range(2):
        trojkacik()
        trojkacik()
        right(90)
    left(90)
    up()
    forward(40)
    left(90)
    down()


def dosrodkowanie(ilosc):
    up()
    forward(ilosc*40/2-20)
    left(90)
    forward(ilosc*40/2-20)
    right(90)
    down()


def wiatraki(ilosc):
    left(90)
    dosrodkowanie(ilosc)
    for k in range(ilosc):
        for e in range(ilosc):
            wiatraczek()
        up()
        right(180)
        forward(40)
        right(90)
        forward(ilosc*40)
        right(90)
        down()

speed(0)
wiatraki(10)
done()
