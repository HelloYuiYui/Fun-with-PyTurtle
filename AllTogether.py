
#EIA, twwsts, 2 April 2018

#importing needed stuff
from turtle import *
import random
import time

#default screen settings
bgcolor("#ffebc6")
color("blue", "yellow")
speed(10)

def circles():
    while True:
        #to create circles
        fd(10)      #change number to effect height radius of the circles.
        left(5)
        #to change the direction for more fancy shapes than just a single circle.
        if abs(pos()) < 1:
            left(10)        #change the number to effect width between circles.

def dots():
    #hiding turtle and pen to avoid creating unwanted lines between dots.
    penup()
    hideturtle()
    dotnum = 0
    limit = 200 #change number to create more or less dots.
    while dotnum <= limit:
        #random coordinates for dots.
        dotx = random.randint(-300, 300) 
        doty = random.randint(-300, 300)

        #random size for dots.
        dotsize = random.randint(1, 200)
        dotsize = dotsize/10
        goto(dotx, doty)
        dot(dotsize, "black")
        dotnum += 1

        #to stop program when reached to the limit.
        if dotnum > limit:
            done()
            break


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

#asking user which function he/she want. 

while True:
    choice = input("dots = d\ncirles = c\ntriangles = t\n\n")
    if choice == "d":
	    dots()
    elif choice == "c":
	    circles()
    elif choice == "t":
        while True:
            tria()
    else:
        print("\ninvalid input, please try again\n")