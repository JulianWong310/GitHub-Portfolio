"""
2025/11/16
use python Turtle to draw a snail
practice for-loop
"""
import turtle as x
x.bgcolor("black") # set background colour
x.shape("turtle") # set pen shape
x.pencolor("blue") # set pen colour
x.speed(100) # set drawing speed
r = 10 # r is the radius of the circle
for i in range(45):
    x.left(10) # the direction and angel of each tilt
    x.circle(r)
    r=r+3
x.done()

