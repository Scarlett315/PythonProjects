import turtle
import math

s = turtle.getscreen()
t = turtle.Turtle()
i = input("number of loops ")
t.speed(0)


def square(length):
    t.penup()
    t.back(length/2)
    t.left(90)
    t.forward(length/2)
    t.pendown()
    for e in range(4):
        t.right(90)
        t.forward(length)


def circles(radius):
    t.penup()
    t.back(radius)
    t.pendown()
    t.right(90)
    t.circle(radius)

def backToHome():
    t.penup()
    t.home()

r = 20

for e in range(int(i)):
    d = r*2
    circles(r)
    backToHome()
    r = math.sqrt(d*d/2)
    square(d)
    backToHome()

turtle.getscreen()._root.mainloop()


