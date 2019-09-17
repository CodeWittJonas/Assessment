import turtle
import random


def main():
    screen = turtle.Screen()
    alex = turtle.Turtle()
    alex.shape("turtle")
    alex.penup()
    alex.setpos(-300, -10)
    alex.color("red")
    alex.speed(1)
    jonas = turtle.Turtle()
    jonas.shape("turtle")
    jonas.penup()
    jonas.setpos(-300, 0)
    jonas.color("#ffcc00")
    jonas.speed(1)

    jonas.pendown()
    alex.pendown()

    while jonas.xcor() < 300 and alex.xcor() < 300:
        number = random.randint(0, 1)

        if number == 0:
            jonas.forward(random.randint(0, 10))
        else:
            alex.forward(random.randint(0, 10))

    turtle.done()


if __name__ == "__main__":
    main()
