from turtle import *

def kwardacik(bok,kolor):
    fillcolor(kolor)
    begin_fill()
    for i in range(4):
        forward(bok)
        left(90)
    up()
    forward(bok)
    down()
    end_fill()


def zygzak(bok,kolor):
    for t in range(11):
        kwardacik(bok,kolor)
    left(90)
    for u in range(10):
        kwardacik(bok,kolor)
    left(90)
    for l in range(9):
        kwardacik(bok,kolor)
    left(90)
    for k in range(6):
        kwardacik(bok,kolor)
    left(90)
    for m in range(5):
        kwardacik(bok,kolor)
    left(90)
    for j in range(2):
        kwardacik(bok,kolor)
    left(90)


def zygzak2(bok,kolor):
    for t in range(10):
        kwardacik(bok,kolor)
    right(90)
    back(bok)
    for u in range(9):
        kwardacik(bok,kolor)
    right(90)
    back(bok)
    for l in range(8):
        kwardacik(bok,kolor)
    right(90)
    back(bok)
    for k in range(5):
        kwardacik(bok,kolor)
    right(90)
    back(bok)
    for m in range(4):
        kwardacik(bok,kolor)
    right(90)
    back(bok)
    for j in range(2):
        kwardacik(bok,kolor)
    right(90)
    back(bok)


def c_zygzak1(bok):
    zygzak(bok,"blue")
    right(90)
    up()
    forward(6*bok)
    right(90)
    forward(4*bok)
    left(180)
    down()
    zygzak(bok,"red")

def c_zygzak2(bok):
    zygzak2(bok,"blue")
    left(90)
    up()
    forward(5*bok)
    left(90)
    forward(bok*4)
    left(180)
    down()
    zygzak2(bok,"red")


def cały(bok):
    c_zygzak1(bok)
    up()
    left(180)
    forward(bok*4)
    right(90)
    forward(bok*16)
    right(90)
    down()
    c_zygzak2(bok)
    up()
    left(180)
    forward(bok*4)
    right(90)
    forward(5*bok)
    right(90)
    down()

def dosrodkowanie(bok):
    up()
    forward(300-11*bok)
    left(90)
    forward(11.5*bok)
    down()


def motyw(liczba_zygzakow):
    bok = 600/(liczba_zygzakow*22+23)
    dosrodkowanie(bok)
    for mz in range(2):
        for l in range(liczba_zygzakow):
            cały(bok)
        up()
        left(90)
        forward(bok)
        down()
        cały(bok)
        up()
        left(90)
        forward(bok)
        down()




tracer(0)
motyw(20)
#
# left(90)
# forward(600)
done()