
from turtle import *
import random

#setting up the environment.
bgcolor("#ffebc6")
color("blue", "yellow")
speed(10)

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

dots()