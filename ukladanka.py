from turtle import *
from random import *

def klocek():
    fillcolor(random(), random(), random())
    begin_fill()
    forward(10)
    left(90)
    forward(10)
    right(90)
    forward(10)
    right(90)
    forward(10)
    left(90)
    forward(10)
    right(90)
    forward(10)
    right(90)
    forward(10)
    left(90)
    forward(10)
    left(90)
    forward(10)
    right(90)
    forward(20)
    right(90)
    forward(10)
    right(90)
    forward(10)
    left(90)
    forward(10)
    left(90)
    forward(10)
    right(90)
    forward(10)
    right(90)
    forward(20)
    left(90)
    forward(10)
    right(90)
    forward(10)
    right(90)
    forward(10)
    left(90)
    forward(10)
    end_fill()
    up()
    left(90)
    forward(30)
    left(180)
    down()


def dojście(do):
    up()
    left(90)
    forward(40)
    right(90)
    forward(do*30+30)
    down()

def układanka(ilosc):
    left(180)
    for i in range(1,ilosc+1):
        j=2*i-1
        for m in range(j):
            klocek()
        dojście(j)



