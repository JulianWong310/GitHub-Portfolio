"""
2025/12/03
⭐Project: Turtle Pattern Blanket
This project uses Python Turtle
to draw a colorful blanket filled with fun shapes.
The picture includes:
•  A pink blanket background
•	A cyan square
•	A  blue circle
•	A red flower made with repeated arcs
•	A yellow star
•	A light green triangle
•  Sign my name
"""

import turtle
t = turtle.Turtle()
t.speed(3)
# Set the pen size to 3
t.pensize(3)

# --- Draw and fill a rectangular blanket ---
# Set the colors:
# outline: brown, fill: pink
t.color("brown","pink")
t.begin_fill()
# Move to the starting point (-210, 180)
t.penup()
t.goto(-210,180)
t.pendown()
# Draw and fill the rectangle
t.goto(210,180)
t.goto(210,-180)
t.goto(-210,-180)
t.goto(-210,180)
t.end_fill()

# --- Draw and fill a square ---
# Set the colors
t.color("brown","cyan")
# Move to the starting point (155, 110)
t.begin_fill()
t.penup()
t.goto(155,110)
t.pendown()
# Draw a filled square (using a for-loop)
t.right(180)
for i in range(4):
    t.forward(50)
    t.left(90)
t.end_fill()

# --- Draw and fill a circle ---
# Set the colors
t.color("brown","blue")
# Move to the starting point (135, -50)
t.penup()
t.goto(135,-50)
t.pendown()
# Draw a filled circle
t.begin_fill()
t.circle(30)
t.end_fill()

# --- Draw and fill a flower ---
t.color("brown","red")
t.penup()
t.goto(0,6)
t.pendown()
t.begin_fill()
for i in range(5):
    t.circle(30)
    t.left(72)
t.end_fill()

# --- Draw and fill a star ---
t.color("brown","yellow")
t.penup()
t.goto(-90,92)
t.pendown()
t.begin_fill()
for i in range(5):
    t.forward(70)
    t.left(144)
t.end_fill()

# --- Draw and fill a triangle ---
t.color("brown","lightgreen")
t.penup()
t.goto(-90,-115)
t.pendown()
t.begin_fill()
t.right(60)
for i in range(3):
    t.forward(65)
    t.left(120)
t.end_fill()

# --- sign my name at the bottom of the picture  ---
t.penup()
t.goto(160, -260)
t.color("black")
t.write("Julian Wong", font=("French Script MT", 28, "normal"))

turtle.done()