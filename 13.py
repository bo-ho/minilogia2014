from turtle import*
def kwardacik(bok):
    for i in range(2):
        forward(bok)
        left(90)
        forward(10)
        left(90)
    up()
    left(90)
    forward(20)
    right(90)
    down()


def zad3():
    left(90)
    for p in range(1,11):
        kwardacik(p*10)

zad3()
done()