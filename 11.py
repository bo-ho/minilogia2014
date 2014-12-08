from turtle import *

def kwadracik():
    for i in range(4):
        forward(10)
        left(90)
    up()
    right(90)
    forward(10)
    left(90)
    down()


def zad1():
    left(90)
    for a in range(8):
        for p in range(a):
            kwadracik()
        up()
        right(90)
        forward(10)
        left(90)
        down()


zad1()
done()