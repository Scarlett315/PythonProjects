import turtle



def makePoint(x, slope, inter):
    y = slope*x + inter
    return x, y



screen = turtle.getscreen()
screen.screensize(100, 100)
t = turtle.Turtle()
t.speed(0)
t.hideturtle()

t.back(250)
for e in range(10):
    t.left(90)
    t.forward(5)
    t.back(5)
    t.right(90)
    t.forward(50)
t.left(90)
t.forward(5)

t.penup()
t.home()
t.pendown()

t.left(90)
t.back(250)
for e in range(10):
    t.left(90)
    t.forward(5)
    t.back(5)
    t.right(90)
    t.forward(50)

t.left(90)
t.forward(5)

t.penup()
t.home()
quit = False

while quit == False:
    m = int(input("Slope: "))
    d = int(input("Y intercept: "))

    a = makePoint(-200, m, d)
    b = makePoint(200, m, d)

    print(a)
    print(b)
    t.penup()
    t.goto(a)
    t.pendown()
    t.goto(b)
    t.penup()
    t.home()


    


