import turtle
import pyttsx3
engine = pyttsx3.init()
rate = engine.getProperty('rate')
volume = engine.getProperty('volume')
engine.setProperty('rate',140)
engine.setProperty('volume',6.0)
voices=engine.getProperty('voices')
engine.setProperty('voice',voices[0].id)
#
car1=turtle.Turtle()
car2=turtle.Turtle()
car3=turtle.Turtle()
screen=turtle.Screen()
#
point1=turtle.Turtle()
point2=turtle.Turtle()
point3=turtle.Turtle()
#
point1.hideturtle()
car1.hideturtle()
point2.hideturtle()
car2.hideturtle()
point3.hideturtle()
car3.hideturtle()
car1.speed(0)
car2.speed(0)
car3.speed(0)
point1.speed(0)
point2.speed(0)
point3.speed(0)
#
screen.bgpic("road.gif")
turtle.addshape("car1.gif")
car1.shape("car1.gif")

turtle.addshape("car2.gif")
car2.shape("car2.gif")

turtle.addshape("car3.gif")
car3.shape("car3.gif")
#
point1.penup()
point2.penup()
point3.penup()
point1.goto(570,150)
point2.goto(570,0)
point3.goto(570,-150)
#
car1.penup()
car2.penup()
car3.penup()
car1.goto(-570,150)
car1.showturtle()
car2.goto(-570,0)
car2.showturtle()
car3.goto(-570,-150)
car3.showturtle()
#
def one():
    car1.setheading(0)
    car1.forward(5)
def two():
    car2.setheading(0)
    car2.forward(5)
def three():
    car3.setheading(0)
    car3.forward(5)

turtle.listen()

turtle.onkey(one,"Right")
turtle.onkey(two," ")
turtle.onkey(three,"d")
#
inn = "Ready set Ride"
engine.say(inn)
engine.runAndWait()
#
while True:
    turtle.update()
    if car1.distance(point1)<10:
        screen.bgpic("green.gif")
        car1.hideturtle()
        car2.hideturtle()
        car3.hideturtle()
        inn = "And the winner is Green"
        engine.say(inn)
        engine.runAndWait()
    elif car2.distance(point2)<10:
        screen.bgpic("blue.gif")
        car1.hideturtle()
        car2.hideturtle()
        car3.hideturtle()
        inn = "And the Winner is Blue"
        engine.say(inn)
        engine.runAndWait()
    elif car3.distance(point3)<10:
        screen.bgpic("white.gif")
        car1.hideturtle()
        car2.hideturtle()
        car3.hideturtle()
        inn = "and the winner is White"
        engine.say(inn)
        engine.runAndWait()
#
turtle.done()