from turtle import *
import time
from random import *
start = time.time()
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

## CLASS and FUNCTION DEFINITIONS ###

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
        self.score = 0
        self.bullets = []
        screen.onkeypress(self.turn_left, left_key)
        screen.onkeypress(self.turn_right, right_key)
        screen.onkeypress(self.fire, fire_key)

    def fire(self):
        if len(self.bullets) < 5 :
           self.bullets.append(Bullet(self))

    def turn_left(self):
        self.left(10)

    def turn_right(self):
        self.right(10)

class Block(Turtle):
    def __init__(self, x, y, color,blocks):
        super().__init__()
        self.ht()
        self.pu()
        self.color(color)
        self.speed(0)
        self.hues = ["dead","red","orange", color]
        self.shape("square")
        self.goto(x,y)
        self.st()
        self.health = 3
        self.blocks = blocks

    def hit(self,blocks,player,scores):
        self.health -= 1 
        if self.health == 0:
            self.die()
            player.score += 1
        else:
            self.color(self.hues[self.health])

    def die(self):
        self.ht()
        self.blocks.remove(self)

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
            self.setheading(180 - (self.heading()))
        if self.xcor() < -150:
            self.setheading(180 - (self.heading()))
        elif self.heading() == 0:
            self.heading(180)
        if self.ycor() > 200:
            self.die()
        if self.ycor() < -200:
            self.die()

    def die(self):
        self.ht()
        if self in self.player.bullets:
            self.player.bullets.remove(self)

class Score(Turtle):
    def __init__(self,x,y, Player):
        super().__init__()
        self.ht()
        self.color("orange")
        self.pu()
        self.goto(x,y)
        self.player = player
        self.write(f"Score: {self.player.score}")

    def update_score(self):
        self.clear()
        self.write(f"Score: {self.player.score}")





def new_row():
    for x in range(-130, 140, 20):
        if len(blocks)%3==0:
            blocks.append(Block(x,190,"lightblue",blocks))
        elif len(blocks)%3==1:
            blocks.append(Block(x,190,"blue",blocks))
        elif len(blocks)%3==2:
            blocks.append(Block(x,190,"darkblue",blocks))

             
def update():
    global start
    if time.time() - start > 3:
        start = time.time()
        for block in blocks:
            block.goto(block.xcor(), block.ycor() - 20)
    for player in players:
        for score in scores:
            for bullet in player.bullets:
                bullet.move()
                for block in blocks:
                    if bullet.distance(block) < 20:
                        block.die(player,score,blocks)
                    else:
                        bullet.die()
                        block.hit(player, score, blocks)
                        score.update_score()


    screen.ontimer(update, 30)


### PROGRAM ###

screen = Screen()
screen.bgcolor("teal")
screen.setup(600,600)
screen.listen()
playing_area()
p1 = Player(-75, -175, "red","red",screen, "d", "a","w",True)
p2 = Player(75,-175,"blue","blue",screen, "Right","Left","Up",True)
score1 = Score (200,-200)
score2 = Score (-230,-200)
bullets = []
blocks = []
players = [p1,p2]

# start = time.time()
screen.tracer(0)
for y in range(190, 100, -20):
    for x in range(-130, 140, 20):
        if len(blocks)%3==0:
            blocks.append(Block(x,y,"lightblue",blocks))
        elif len(blocks)%3==1:
            blocks.append(Block(x,y,"blue",blocks))
        elif len(blocks)%3==2:
            blocks.append(Block(x,y,"darkblue",blocks))
screen.tracer(1)
update()
print("Thank you mr yin for this class it was very fun. I hope you have a good summer")
screen.exitonclick()