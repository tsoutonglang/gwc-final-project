from turtle import *
from PIL import Image
import math
import time

willyimage = "willy (1).gif"
starfishimage="starfish.gif"
screen = Screen()
screen.addshape(starfishimage)



bubbletitle = Turtle()
bubble = "speechtitle.gif"
screen.addshape(bubble)
bubbletitle.shape(bubble)

starfishes = []
DEFAULT_Y = -150

def create_starfish(x):
    if len(starfishes) < 3:
        new_turtle = Turtle()
        new_turtle.shape(starfishimage)
        new_turtle.setpos(x, DEFAULT_Y)
        starfishes.append(new_turtle)

willy =Turtle()

screen.bgcolor("lightblue")

screen.addshape(willyimage)
willy.shape(willyimage)


create_starfish(10)
create_starfish(20)
create_starfish(50)

# Name your Turtle.
willy.penup()

setup(700,700)
willy.setpos(-150,-150)
bubbletitle.setpos(-100, -100)




### Write your code below:








# Close window on click.
mainloop()
exitonclick()
