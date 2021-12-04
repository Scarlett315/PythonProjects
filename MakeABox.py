import turtle


def rect(length, width):
    for e in range(2):
        turtle.forward(length)
        turtle.right(90)
        turtle.forward(width)
        turtle.right(90)

def cut(height, width):
    turtle.forward(1/2*height)
    turtle.penup()
    turtle.forward(width)
    turtle.pendown()
    turtle.forward(1/2*height)
    turtle.penup()
    turtle.back(height + width)

def makeABox(length,width,height):

    #Rectangle
    lengthOfBox = (2*length) + (2* height)
    widthOfBox = height + width
    turtle.penup()
    turtle.back(lengthOfBox/2)
    turtle.pendown()
    rect(lengthOfBox, widthOfBox)

    #Cuts/Folds
    turtle.penup()
    turtle.goto(- (lengthOfBox / 2), 0)

    turtle.pendown()
    turtle.forward(length)
    turtle.right(90)
    cut(height, width)

    turtle.left(90)

    turtle.forward(height)
    turtle.right(90)
    turtle.pendown()
    cut(height, width)

    turtle.left(90)

    turtle.forward(length)
    turtle.right(90)
    turtle.pendown()
    cut(height, width)

    turtle.penup()
    turtle.goto(-lengthOfBox/2, -height/2 )
    turtle.pendown()
    turtle.setheading(0)
    turtle.forward(lengthOfBox)

    turtle.penup()
    turtle.goto(-lengthOfBox / 2, -height / 2 - width)
    turtle.pendown()
    turtle.setheading(0)
    turtle.forward(lengthOfBox)

    #Tab
    turtle.penup()
    turtle.goto(-lengthOfBox / 2, -height / 2)
    turtle.pendown()
    turtle.setheading(270)
    rect(width, height/4)



makeABox(120, 120, 120)

turtle.getscreen()._root.mainloop()


