from turtle import *

def kwadracik():
    for i in range(4):
        forward(10)
        left(90)

def zad2():
    for a in range(1,8):
        left(90)
        kwadracik()
        right(90)
        for i in range(a):
            up()
            forward(20)
            down()


zad2()
done()