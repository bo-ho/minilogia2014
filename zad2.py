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

def kwadrat(boczek):
    for g in range(4):
        forward(boczek)
        right(90)
    forward(boczek)


def niebieski(boczek):
    fillcolor("blue")
    begin_fill()
    kwadrat(boczek)
    end_fill()


def zielony(boczek):
    fillcolor("green")
    begin_fill()
    kwadrat(boczek)
    end_fill()



def iksik(boczek):
    left(45)
    niebieski(boczek)
    zielony(boczek)
    niebieski(boczek)
    left(180)
    up()
    forward(boczek)
    down()
    right(90)
    forward(boczek)
    left(180)
    niebieski(boczek)
    zielony(boczek)
    niebieski(boczek)


def oblicz_boczek(bok_wzorka):
    bok_kwadratu = bok_wzorka / 4
    boczek = bok_kwadratu / sqrt(8)
    return boczek


def pozycja_poczatkowa(bok_wzorka):
    up()
    forward(bok_wzorka/2)
    right(90)
    forward(bok_wzorka / 4)
    down()


def linie(bok_wzorka):
    right(90)
    forward(bok_wzorka)
    right(180)
    forward(bok_wzorka / 4)
    right(90)
    forward(bok_wzorka / 4)
    left(180)
    forward(bok_wzorka)
    right(180)
    forward(bok_wzorka / 4)
    right(90)
    forward(bok_wzorka / 4)
    left(180)
    forward(bok_wzorka)
    left(180)
    forward(bok_wzorka / 4)
    right(90)
    forward(bok_wzorka / 4)
    left(180)
    forward(bok_wzorka)


def polksiezyce(bok_wzorka):
    fillcolor("green")
    begin_fill()
    forward(bok_wzorka/8)
    right(90)
    forward(bok_wzorka/8)
    left(90)
    forward(bok_wzorka/4)
    left(90)
    forward(bok_wzorka/8)
    right(90)
    forward(bok_wzorka/8)
    right(90)
    forward(bok_wzorka/4)
    right(90)
    forward(bok_wzorka/2)
    right(90)
    forward(bok_wzorka/4)
    right(90)
    end_fill()




def motyw(bok_wzorka):
    boczek = oblicz_boczek(bok_wzorka)
    pozycja_poczatkowa(bok_wzorka)
    for t in range(4):
        forward(bok_wzorka/4)
        right(90)
        forward(bok_wzorka)
        right(90)
        forward(boczek/(6/4))
        right(90)
        iksik(boczek)
        up()
        right(45)
        forward(boczek/(6/4))
        right(90)
        down()
    linie(bok_wzorka)
    right(90)
    polksiezyce(bok_wzorka)
    forward(bok_wzorka*(3/4))
    right(90)
    forward(bok_wzorka/4)
    polksiezyce(bok_wzorka)
    forward(bok_wzorka*(3/4))
    right(90)
    forward(bok_wzorka/4)
    polksiezyce(bok_wzorka)
    forward(bok_wzorka*(3/4))
    right(90)
    forward(bok_wzorka/4)
    polksiezyce(bok_wzorka)
    forward(bok_wzorka*(3/4))
    right(90)
    forward(bok_wzorka/4)
    right(90)
    forward(bok_wzorka/4)
    left(90)
    forward(bok_wzorka/8)
    right(90)
    iksik(boczek*2)




testuj(2)
done()