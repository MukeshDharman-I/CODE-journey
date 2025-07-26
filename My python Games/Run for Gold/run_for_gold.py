import turtle
import random
#
score=0
#
board=turtle.Turtle()
#
bucket=turtle.Turtle()
screen=turtle.Screen()
gold1=turtle.Turtle()
gold2=turtle.Turtle()
gold3=turtle.Turtle()
#
turtle.addshape("Gold.gif")
gold1.shape("Gold.gif")
gold2.shape("Gold.gif")
gold3.shape("Gold.gif")
#
bucket.penup()
bucket.hideturtle()
#
screen.bgpic("screen.gif")
turtle.addshape("bucket.gif")
bucket.shape("bucket.gif")
#
board.penup()
board.goto(400,350)
#bucket
bucket.goto(0,-320)
bucket.showturtle()
def left():
    bucket.setheading(180)
    bucket.forward(60)
def right():
    bucket.setheading(0)
    bucket.forward(60)    
turtle.listen()    
turtle.onkey(left,"Left")
turtle.onkey(right,"Right")
#
gold1.penup()
gold1.hideturtle()
gold1.goto(0,380)
gold1.showturtle()
gold2.penup()
gold2.hideturtle()
gold2.goto(0,380)
gold2.showturtle()
gold3.penup()
gold3.hideturtle()
gold3.goto(0,380)
gold3.showturtle()
#
def move():
    y=gold1.ycor()
    gold1.sety(y-(random.randint(3,7)))
def move1():
    z=gold2.ycor()
    gold2.sety(z-(random.randint(3,7)))
def move2():
    v=gold3.ycor()
    gold3.sety(v-(random.randint(3,7)))        
#    
while True:

    turtle.update()
    move()
    move1()
    move2()
    if gold1.ycor() < -380:
        gold1.hideturtle()
        x=random.randint(-580,580)
        gold1.goto(x,380)
        gold1.showturtle()
    if bucket.distance(gold1) <100:
        score+=1
        board.clear()
        board.write("Score : {} ".format(score),font=("courier",30))
        x=random.randint(-580,580)
        gold1.hideturtle()
        gold1.goto(x,380)
        gold1.showturtle()
    if gold2.ycor() < -380:
        gold2.hideturtle()
        p=random.randint(-580,580)
        gold2.goto(p,380)
        gold2.showturtle()
    if bucket.distance(gold2) <100:
        score+=1
        board.clear()
        board.write("Score : {} ".format(score),font=("courier",30))
        p=random.randint(-580,580)
        gold2.hideturtle()
        gold2.goto(p,380)
        gold2.showturtle()   
    if gold3.ycor() < -380:
        gold3.hideturtle()
        q=random.randint(-580,580)
        gold3.goto(q,380)
        gold3.showturtle()
    if bucket.distance(gold3) <100:
        score+=1
        board.clear()
        board.write("Score : {} ".format(score),font=("courier",30))
        q=random.randint(-580,580)
        gold3.hideturtle()
        gold3.goto(q,380)
        gold3.showturtle()   
    if score==25:
        screen.bgpic("win.gif")
        bucket.hideturtle()
turtle.done()