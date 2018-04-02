
from turtle import * 

#setting up the environment.
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

circles()