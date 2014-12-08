from turtle import *
from random import *


def zabek(bok):
    fillcolor(random(), random(), random())
    begin_fill()
    forward(bok)
    left(30)
    forward(bok/2)
    left(120)
    forward(bok/2)
    right(120)
    forward(bok)
    left(120)
    forward(bok)
    right(120)
    forward(bok/2)
    left(120)
    forward(bok/2)
    left(30)
    forward(bok)
    left(90)
    forward(bok/2)
    left(90)
    forward(bok/2)
    right(90)
    forward(bok)
    right(90)
    forward(bok/2)
    left(90)
    forward(bok/2)
    end_fill()
    up()
    left(180)
    forward(bok)
    right(90)
    forward(bok/2)
    left(180)
    down()



def dosrodkowanie(ilosc,bok):
    left(90)
    up()
    forward(350-bok*2)
    right(90)
    down()




def dojście(bok):
    up()
    right(90)
    forward(bok*2)
    left(90)
    down()

def pilka(ilosc):
    left(90)
    bok=700/(ilosc*2+1)
    dosrodkowanie(ilosc,bok)
    for k in range(ilosc):
        zabek(bok)
        zabek(bok)
        dojście(bok)



