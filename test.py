from turtle import *
from PIL import Image
import math
import time
import random

willyimage = "willy (1).gif"
starfishimage="starfish.gif"
screen = Screen()
screen.addshape(starfishimage)



bubbletitle = Turtle()
bubble = "speechtitle.gif"
screen.addshape(bubble)
bubbletitle.shape(bubble)
bubble2 = "speechtitle2.gif"
screen.addshape(bubble2)
bubbletitle.shape(bubble2)

starfishes = []
DEFAULT_Y = -150

def create_starfish(x):
    if len(starfishes) < 3:
        new_turtle = Turtle()
        new_turtle.penup()
        new_turtle.shape(starfishimage)
        new_turtle.setpos(x, DEFAULT_Y)
        starfishes.append(new_turtle)


def hide_bubble(bubs,bubs2):
        new_bubble = Turtle()
        new_bubble.penup()
        new_bubble.shape(bubs)
        bubbletitle.ht()
        time.sleep(3)
        bubbletitle.ht()
        new_bubble.shape(bubs2)
        time.sleep(3)
        bubbletitle.ht()


willy =Turtle()

screen.bgcolor("lightblue")

screen.addshape(willyimage)
willy.shape(willyimage)


create_starfish(100)
create_starfish(200)
create_starfish(300)

# Name your Turtle.
willy.penup()

setup(700,700)
willy.setpos(-240,-150)
bubbletitle.setpos(0, -80)
hide_bubble(bubble,bubble2)

def stop():
    willy.speed(10)

def up():
    willy.forward(10)
    willy.speed(6)

screen.onkey(up, "Up")
screen.onkeyrelease(stop, "Up")
screen.listen()






# Close window on click.
mainloop()
