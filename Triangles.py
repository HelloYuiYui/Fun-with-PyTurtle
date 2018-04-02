
from turtle import *
import random
import time

def tria():
    showturtle()
    title("Triangle")

    #assigning random coordinates for each corner of the triangle.
    coor1X = random.randint(-300, 300)
    coor1Y = random.randint(-300, 300)

    coor2X = random.randint(-300, 300)
    coor2Y = random.randint(-300, 300)

    coor3X = random.randint(-300, 300)
    coor3Y = random.randint(-300, 300)

    begin_fill()

    #Setting up the environment.
    bgcolor("#ffebc6")
    speed(10)
    color("black", "yellow")
    pensize(2)

    #drawing the triangle
    penup()
    setpos(coor1X, coor1Y)
    pendown()
    setpos(coor2X, coor2Y)
    setpos(coor3X, coor3Y)
    setpos(coor1X, coor1Y)
    time.sleep(0.2)
    clear()

    end_fill()

while True:
    tria()