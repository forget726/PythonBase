import turtle
import random

colorList = ["red", "purple", "skyblue", "yellow", "hotpink", "green", "blue", "black", "darkred"]
t = turtle.Pen()
t.speed(0)
t.pensize(0.3)
t.color("red")
size = 0.5
# t.left(-15)
random.randint(0, 8)
for i in range(24):
    t.circle(100)
    t.left(15)
    t.pensize(size)
    size +=0.5
    # t.color(colorList[random.randint(0, 8)])
turtle.done()