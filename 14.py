from turtle import *


def trojkat(bok):
    left(30)
    for i in range(3):
        forward(bok)
        right(120)



def zad4():
    bok=100
    zmienna=bok*0.2
    left(90)
    for i in range(5):
        trojkat(bok)
        right(30)
        bok=bok-zmienna

zad4()
done()