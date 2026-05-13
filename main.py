from turtle import *
from time import *
from random import *

def playing_area():
    pen = Turtle()
    pen.ht()
    pen.speed(0)
    pen.color('white')
    pen.begin_fill()
    pen.goto(-150, -200)
    pen.goto(150, -200)
    pen.goto(150, 200)
    pen.goto(-150, 200)
    pen.goto(-150, -200)
    pen.end_fill()

### CLASS and FUNCTION DEFINITIONS ###

class Player(Turtle):
    def __init__(self, x, y, color, player_color, screen, right_key, left_key, fire_key,alive):
        super().__init__()
        self.ht()
        self.speed(0)
        self.color(color)
        self.player_color = color
        self.penup()
        self.goto(x, y)
        self.setheading(90)
        self.shape("turtle")
        self.bullets = []
        self.alive = True
        self.st()
        screen.onkeypress(self.turn_left, left_key)
        screen.onkeypress(self.turn_right, right_key)
        screen.onkeypress(self.fire, fire_key)

    def fire(self):
        self.bullets.append(Bullet(self))

    def turn_left(self):
        self.left(10)

    def turn_right(self):
        self.right(10)

class Block(Turtle):
    def __init__(self, x, y, color):
        super().__init__()
        self.ht()
        self.pu()
        self.color(color)
        self.speed(0)
        self.shape("square")
        self.goto(x,y)
        self.st()



class Bullet(Turtle):
    def __init__(self, player):
        super().__init__()
        self.ht()
        self.speed(0)
        self.color(player.player_color)
        self.penup()
        self.goto(player.xcor(), player.ycor())
        self.setheading(player.heading())
        self.shape("triangle")
        self.player = player
        self.st()
    def move(self):
        self.forward(10)
        if self.xcor() > 150:
            self.setheading()
            self.player.bullets.remove(self)
        if self.xcor() < -150:
            self.setheading()
            self.player.bullets.remove(self)
        if self.ycor() < -200:
            self.setheading()
            self.player.bullets.remove(self)
        if self.ycor() < 200:
            self.setheading()
            self.player.bullets.remove(self)

    def die(self):
        self.ht()
        self.player.bullets.remove(self)








### PROGRAM ###
screen = Screen()
screen.bgcolor("teal")
screen.setup(600,600)
screen.listen()
playing_area()

bullets = []
blocks = []
p1 = Player(-75, -175, "red","red",screen, "d", "a","w",True)
p2 = Player(75,-175,"blue","blue",screen, "Right","Left","Up",True)
for y in range(190, 100, -20):
    for x in range(-130, 140, 20):
        if len(blocks)%3==0:
            blocks.append(Block(x,y,"lightblue"))
        elif len(blocks)%3==1:
            blocks.append(Block(x,y,"blue"))
        elif len(blocks)%3==2:
            blocks.append(Block(x,y,"darkblue"))
while p1.alive and p2.alive:
    for bullet in bullets:
        bullet.move()
    


screen.exitonclick()