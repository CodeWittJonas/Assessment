import time
import turtle

pen = turtle.Turtle()
pen.shape("turtle")
pen.speed(0)
pen.color('#aabbbf')

for i in range(20):
    pen.circle(10*i)


print(pen.xcor(), pen.ycor())

time.sleep(10)
