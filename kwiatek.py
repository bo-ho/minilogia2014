from turtle import *


def platki():
    up()
    fillcolor("orangered")
    begin_fill()
    circle(120)
    left(180)
    circle(120)
    right(90)
    circle(120)
    right(180)
    circle(120)
    end_fill()
    down()


def srodek(ilosc):
    up()
    forward(60)
    down()
    left(90)
    fillcolor("yellow")
    begin_fill()
    circle(60)
    end_fill()
    left(90)
    up()
    forward(60)
    down()
    for i in range(ilosc):
        up()
        forward(60)
        down()
        forward(45)
        right(90)
        fillcolor("black")
        begin_fill()
        circle(15)
        end_fill()
        right(90)
        forward(45)
        up()
        forward(60)
        down()
        right(180)
        right(360/ilosc)


def kwiatek(ilosc):
    platki()
    srodek(ilosc)


kwiatek(5)