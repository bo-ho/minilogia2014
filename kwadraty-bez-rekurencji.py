from turtle import *

def kwadrat(bok):
    for i in range(4):
        forward(bok)
        left(90)

def kwadraty():
    for i in range(10):
        up()
        bok = 400 - 40*i
        for j in range(2):
            forward(bok/2)
            left(90)
        down()
        kwadrat(bok)
        up()
        for j in range(2):
            forward(bok/2)
            left(90)

kwadraty()
done()
