import turtle
from datetime import datetime
import time


screen = turtle.getscreen()
t = turtle.Turtle()
t.speed(0)
t.hideturtle()
screen.tracer(0, 0)

t.left(90)
t.up()
t.forward(250)
t.left(90)
t.down()
t.circle(250)


style = ('Courier', 30, 'normal')


def arrow(length, angle):
    t.home()
    t.left(90)
    t.right(angle)
    t.down()
    t.forward(length)
    t.home()


def drawHands(hour, minute, second):
    arrow(200, second)
    arrow(100, hour)
    arrow(150, minute)

n = 1
a = 30
for e in range(12):
    t.up()
    t.home()
    t.left(90)
    t.up()
    t.forward(205)
    t.right(90)
    t.circle(-220, a)
    t.write(str(n), font = style, align = "CENTER")
    n+=1
    a+=30

while True:
    ti = datetime.now().time()
    h = ti.hour*30 + ti.minute*0.25
    m = ti.minute*6
    se = ti.second*6
    drawHands(h, m, se)
    screen.update()
    time.sleep(1)
    t.penup()
    t.goto(0, -201)
    t.pendown()
    t.fillcolor("white")
    t.pencolor("white")
    t.begin_fill()
    t.circle(201)
    t.end_fill()
    t.pencolor("black")
    t.penup()







turtle.getscreen()._root.mainloop()