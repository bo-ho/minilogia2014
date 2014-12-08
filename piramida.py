from turtle import *
from math import *


def trójkacik():
    fillcolor("aqua")
    begin_fill()
    for i in range(3):
        right(120)
        forward(60)
    end_fill()


def szesciokat():
    fillcolor("yellow")
    begin_fill()
    left(90)
    for s in range(6):
        forward(60)
        right(60)
    end_fill()


def czesc():
    right(60)
    trójkacik()
    left(90)
    szesciokat()


def piramida():
    left(90)
    up()
    forward(sqrt(420*420-(420/2)*(420/2))/2)
    left(150)
    forward(60)
    down()
    for i in range(3):
        czesc()
        left(240)
        forward(120)
    right(60)
    trójkacik()
    right(120)
    forward(4*60)
    right(60)
    forward(120)
    left(240)
    for i in range(2):
        czesc()
        left(240)
        forward(120)
    right(60)
    trójkacik()
    right(120)
    forward(120)
    right(60)
    forward(120)
    left(240)
    czesc()
    left(240)
    forward(120)
    right(60)
    trójkacik()
    left(180)
    forward(120)
    left(180)
    trójkacik()
    forward(60)
    right(60)
    forward(60)
    left(120)
    trójkacik()
    up()
    right(60)
    forward(120)
    down()
    left(60)
    trójkacik()
    up()
    back(120)
    down()
    trójkacik()

