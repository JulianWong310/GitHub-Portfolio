"""
2025/11/30
Use Python Turtle to draw and paint a carpet
Practice for-loop
"""
import turtle
qwerty = turtle.Turtle() # name turtle qwerty

# draw and paint the background of the big carpet
qwerty.color("pink")
qwerty.begin_fill()
qwerty.forward(120)
qwerty.left(90)
qwerty.forward(120)
qwerty.left(90)
qwerty.forward(315)
qwerty.left(90)
qwerty.forward(315)
qwerty.left(90)
qwerty.forward(315)
qwerty.left(90)
qwerty.forward(195)
qwerty.left(90)
qwerty.forward(120)
qwerty.right(180)
qwerty.end_fill()

# draw and paint the first small square on the carpet
qwerty.color("cyan")
qwerty.begin_fill()
qwerty.forward(120)
qwerty.left(90)
qwerty.forward(120)
qwerty.left(90)
qwerty.forward(120)
qwerty.left(90)
qwerty.forward(120)
qwerty.end_fill()

# make a space between two squares
qwerty.penup()
qwerty.forward(75)
qwerty.pendown()

# draw and paint the second square on the carpet
qwerty.color("red")
qwerty.begin_fill()
for i in range(4): # simplify steps using a for loop
    qwerty.forward(120)
    qwerty.left(90)
qwerty.end_fill()

# make a space between two squares
qwerty.penup()
qwerty.right(90)
qwerty.forward(75)
qwerty.pendown()

# draw and paint the third square on the carpet
qwerty.color("green")
qwerty.begin_fill()
for i in range(4):
    qwerty.forward(120)
    qwerty.left(90)
qwerty.end_fill()

# make a space between two squares
qwerty.right(90)
qwerty.penup()
qwerty.forward(75)
qwerty.pendown()

# draw and paint the forth square on the carpet
qwerty.color("yellow")
qwerty.begin_fill()
for i in range(4):
    qwerty.forward(120)
    qwerty.left(90)
qwerty.end_fill()

# draw and paint the center square in the carpet
qwerty.color("black")
qwerty.begin_fill()
qwerty.right(90)
for i in range(4):
    qwerty.forward(75)
    qwerty.right(90)
qwerty.end_fill()

turtle.done()
