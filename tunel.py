from turtle import *

def tunel(bok):
    forward(bok/2)
    for lm in range(4):
        left(90)
        forward(bok)
    back(bok/2)
    if (bok > 20):
        tunel(bok-20)

tracer(0)
tunel(200)
update()
done()
