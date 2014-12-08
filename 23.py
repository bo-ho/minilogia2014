from turtle import *

def stempek():
    stamp()
    right(90)
    up()
    forward(10)
    down()
    left(90)


def doprowadzenie(wieloks):
    up()
    forward(wieloks * 20 / 2)
    left(90)
    forward(wieloks * 20 / 2)
    right(90)
    down()


def musztra():
    wieloks=15
    left(90)
    ilosc=1
    doprowadzenie(wieloks)
    for i in range(wieloks):
        for t in range(ilosc):
             stempek()
        ilosc=ilosc+1
        up()
        back(15)
        left(90)
        forward(ilosc*10)
        right(90)
        down()



