import turtle
import time


pen = turtle.Turtle()
pen.shape("turtle")
pen.speed(10000)


def drawMosaic(color, numberOfSides, size, numberOfIterations):
    pen.color(color)
    pen.width(100)
    pen.pensize(10)
    for i in range(0, numberOfIterations):
        for j in range(0, numberOfSides):
            pen.forward(size)
            pen.left(360 / numberOfSides)
        pen.left(360 / numberOfIterations)


drawMosaic("pink", 100, 10, 3)

time.sleep(30)
