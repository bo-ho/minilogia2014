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

def kwiatek():
    down()
    right(90)
    fillcolor("yellow")
    begin_fill()
    circle(100)
    end_fill()
    right(60)
    forward(100)
    right(120)
    for b in range(12):
        wybranie_koloru()
        begin_fill()
        forward(100)
        for i in range(3):
            right(120)
            forward(100)
        right(30)
        end_fill()


def wybranie_koloru():
    wybrany = randint(1, 3)
    if wybrany == 1:
        wybrany = "red"
    elif wybrany == 2:
        wybrany = "orange"
    elif wybrany == 3:
        wybrany = "yellow"
    fillcolor(wybrany)


def kwiatki():
    up()
    left(180)
    forward(201)
    right(90)
    forward(100)
    right(180)
    kwiatek()
    up()
    right(60)
    forward(100)
    right(30)
    forward(100)
    left(90)
    forward(400)
    left(90)
    forward(100)
    left(180)
    down()
    kwiatek()

koloreczek = "green"
def kolor():
    global koloreczek
    if koloreczek == "yellow" :
        koloreczek = "green"
    elif koloreczek == "green" :
        koloreczek = "yellow"





def baszta(podstawa):
    fillcolor("brown")
    begin_fill()
    right(90)
    forward(podstawa*5)
    right(90)
    forward(podstawa)
    right(90)
    forward(podstawa)
    left(90)
    forward(podstawa*6)
    left(90)
    forward(podstawa)
    right(90)
    forward(podstawa*2)
    right(90)
    forward(podstawa)
    right(90)
    forward(podstawa)
    left(90)
    forward(podstawa)
    left(90)
    forward(podstawa)
    right(90)
    forward(podstawa)
    right(90)
    forward(podstawa)
    left(90)
    forward(podstawa)
    left(90)
    forward(podstawa)
    right(90)
    forward(podstawa)
    right(90)
    forward(podstawa*2)
    right(90)
    forward(podstawa)
    left(90)
    forward(podstawa*6)
    left(90)
    forward(podstawa)
    right(90)
    forward(podstawa)
    end_fill()

def przesun_w_lewo(liczba):
    podstawa=45
    szerokosc=0
    for k in range(liczba):
        szerokosc=szerokosc+podstawa+podstawa*5
        podstawa=podstawa*(6/9)
    szerokosc=szerokosc-podstawa/(6/9)
    return szerokosc

def baszty(liczba):
    podstawa = 45
    left(180)
    up()
    forward(((przesun_w_lewo(liczba))/2-podstawa*5))
    left(90)
    forward(202)
    down()
    for i in range(liczba):
        baszta(podstawa)
        up()
        left(180)
        forward(podstawa)
        right(90)
        forward(podstawa+podstawa*(6/9)*5)
        right(90)
        podstawa=podstawa*(6/9)
        down()

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

testuj(2)

done()