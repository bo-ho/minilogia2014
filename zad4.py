from turtle import *
from math import *
from random import *

# funkcja testuj() do testowania rozwiązania
def testuj(n):
    a = 499
    b = 796
    reset()

    tracer(0)
    if n == 1: kwiatki()
    if n == 2: motyw(400)
    if n == 3: baszty(3)
    if n == 4: mozaika(4)

    pu();
    home();
    pd()
    pu();
    fd(b / 2);
    pd()
    lt(90)
    color("red")
    for i in range(2):
        fd(a // 2);
        lt(90)
        fd(b);
        lt(90)
        fd(a // 2)
    rt(90)
    pu();
    bk(b / 2);
    pd()
    color("black")
    update()

    tracer(1)
    nazwa = "zad" + str(n) + ".gif"
    addshape(nazwa)
    zolw_test = Turtle()
    zolw_test.shape(nazwa)
    zolw_test.speed(0)
    zolw_test.pu()
    zolw_test.ondrag(zolw_test.goto)


#tutaj jest miejsce na Twoje rozwiązania zadania

koloreczek = "green"
def kolor():
    global koloreczek
    if koloreczek == "yellow" :
        koloreczek = "green"
    elif koloreczek == "green" :
        koloreczek = "yellow"

def kształcik():
    global koloreczek
    for g in range(4):
        kolor()
        fillcolor(koloreczek)
        begin_fill()
        for i in range(2):
            left(45)
            forward(10)
            right(45)
            forward(20)
            right(45)
            forward(10)
            right(135)

        end_fill()
        up()
        forward(34)
        right(90)
        down()

def mozaika(ilość):
    bok = 34
    left(90)
    up()
    forward(bok*(ilość/2))
    right(90)
    forward(bok*((ilość/2)/2))
    down()
    for q in range(ilość):
        for d in range(ilość):
            kształcik()
            right(90)
            up()
            forward(bok)
            left(90)
            down()
        right(180)
        up()
        forward(bok)
        right(90)
        forward(bok*ilość)
        right(90)
        down()

testuj(4)
done()