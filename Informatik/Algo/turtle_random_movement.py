import random
import time
import turtle


def roll_dices():
    dice_one = random.randint(1, 6)
    dice_two = random.randint(1, 6)
    return dice_one + dice_two


def createTurtle():
    kröte = turtle.Turtle()
    kröte.penup()
    kröte.shape("turtle")
    return kröte


if __name__ == "__main__":

    x_index = -700
    y_index = 300
    turtles = []
    for i in range(12):
        kröti = createTurtle()
        kröti.color("blue")
        kröti.speed(0)
        kröti.goto(x_index, y_index)
        kröti.width(30)
        y_index -= 50
        kröti.pendown()
        turtles.append(kröti)

    for i in range(100000):
        turtles[(roll_dices()-1)].forward(1)

time.sleep(30)
