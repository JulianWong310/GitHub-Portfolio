"""
2025/12/01
Turtle Pattern Blanket
This project uses Python Turtle and functions to draw a colorful blanket filled with fun shapes.
The picture includes:
	•	⭐ An orange star
	•	🔵 A yellow circle
	•	🟥  A cyan square
	•	🌸 A blue flower made with repeated arcs
	•	🔺 A red triangle
	•	🎀 A light green blanket background
	•	✏️ The "Colorful Blanket"text
"""

import turtle
t = turtle.Turtle()
t.speed(10)

# draw and paint a rectangle blanket
def blanket():
    t.color("green","lightgreen")
    t.pensize(4)
    t.penup()
    t.goto(-220, 170) # let the turtle moves to the point (-220,170).
    t.pendown()

    t.begin_fill()
    t.goto(220,170)
    t.goto(220, -170)
    t.goto(-220, -170)
    t.goto(-220,170)
    t.end_fill()

# draw and paint a square
def square():
    t.color("black","cyan")
    t.begin_fill()
    for i in range(4):
        t.forward(50)
        t.right(90)
    t.end_fill()

# draw and paint a circle
def circle():
    t.color("black","yellow")
    t.begin_fill()
    t.circle(25)
    t.end_fill()

# draw and paint a star
def star():
    t.color("black","orange")
    t.begin_fill()
    for i in range(5):
        t.forward(60)
        t.right(144)
    t.end_fill()

# draw and paint a triangle
def triangle():
    t.color("black","red")
    t.begin_fill()
    for i in range(3):
        t.forward(60)
        t.right(120)
    t.end_fill()

# draw and paint a flower
def flower():
    t.color("black","blue")
    t.begin_fill()
    for i in range(5):
        t.circle(43)
        t.right(72)
    t.end_fill()

# put all the shapes in the blanket
def place_shapes(draw_func, x, y):
    t.penup()
    t.goto(x, y)
    t.setheading(0) # facing right
    t.pendown()
    draw_func()

# call all the functions
blanket()
place_shapes(square,110, 100)
place_shapes(circle,130, -110)
place_shapes(star,  -152,  -80)
place_shapes(triangle , -157, 100)
place_shapes(flower,5,  0)

# write a message on the top of the picture
t.penup()
t.goto(0, 200)
t.color("green")
# writing text does not need to use pendown()
t.write("Colorful Blanket", align="center", font=("Bell MT", 28, "bold"))

turtle.done()