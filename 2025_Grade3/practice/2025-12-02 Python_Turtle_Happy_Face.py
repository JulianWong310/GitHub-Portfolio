"""
2025/12/02
I practiced
1) using goto in Turtle.
2) moving the turtle to a new spot.
3) drawing shapes in different places.
4) choosing x and y positions.
5) making my drawing neat and clear.
"""
import turtle
t = turtle.Turtle()
t.speed(10)
t.pensize(3)

t.color("black","yellow")
t.begin_fill()
t.circle(80)
t.end_fill()

t.color("black")
t.penup()
t.goto(-30,90)
t.pendown()
t.begin_fill()
t.circle(10)
t.end_fill()

t.color("black")
t.penup()
t.goto(30,90)
t.pendown()
t.begin_fill()
t.circle(10)
t.end_fill()

t.color("black")
t.penup()
t.goto(-40,60)
t.pendown()

t.setheading(-55)
t.begin_fill()
t.circle(50,120)

turtle.done()
