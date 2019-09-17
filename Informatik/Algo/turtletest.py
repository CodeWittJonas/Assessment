import turtle
import time

jonas = turtle.Turtle()
jonas.color("#00ffe5")
jonas.shape("turtle")
jonas.speed(0)
jonas.pendown()

seiten = 0

while True:
    jonas.forward(1)
    jonas.right(1)
    seiten += 1



time.sleep(50)
