import turtle
#
red=turtle.Turtle()
blue=turtle.Turtle()
screen=turtle.Screen()
#
r=0
b=0
#
screen.bgpic("Mat.gif")
#
turtle.addshape("red.gif")
turtle.addshape("blue.gif")
red.shape("red.gif")
blue.shape("blue.gif")
red.penup()
blue.penup()
red.goto(0,140)
blue.goto(0,-140)
#
def pushred():
    y=red.ycor()
    red.sety(y+40)
    yx=blue.ycor()
    blue.sety(yx)
def pushred1():
    y=red.ycor()
    red.sety(y+90)
    yx=blue.ycor()
    blue.sety(yx)      
def pushblue():
    y=blue.ycor()
    blue.sety(y-40)
    yx=red.ycor()
    red.sety(yx)
def pushblue1():
    y=blue.ycor()
    blue.sety(y-90)
    yx=red.ycor()
    red.sety(yx)               
#
while True:
    turtle.update()     

    if red.ycor() >= 400:
        red.hideturtle()
        blue.hideturtle()
        screen.bgpic("bluewin.gif")
        break
    if blue.ycor() <= -400:
        red.hideturtle()
        blue.hideturtle()
        screen.bgpic("redwin.gif")
        break 
    def rup():
        red.setheading(90)
        red.forward(12)
    def rdown():
        red.setheading(270)    
        red.forward(12)
        if red.distance(blue) <=140 and red.distance(blue) >=80 :
            pushblue()
        if red.distance(blue) <=81:
            pushblue1()           
    def lup():
        blue.setheading(90)
        blue.forward(12)
        if blue.distance(red) <=140 and blue.distance(red) >=80:
            pushred()
        if blue.distance(red) <=81:
            pushred1()
    def ldown():
        blue.setheading(270)    
        blue.forward(12) 
    turtle.onkey(rup,"w")  
    turtle.onkey(rdown,"s") 
    turtle.onkey(lup,"Up")
    turtle.onkey(ldown,"Down")   

    turtle.listen()
#
turtle.done()