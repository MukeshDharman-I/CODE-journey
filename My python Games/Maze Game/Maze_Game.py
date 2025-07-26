import turtle
import pyttsx3
engine = pyttsx3.init()
rate = engine.getProperty('rate')
volume = engine.getProperty('volume')
print(f"Volume : {volume} \nRate : {rate}")
engine.setProperty('rate',140)
engine.setProperty('volume',6.0)
voices=engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)
icon=turtle.Turtle()
apple=turtle.Turtle()
apple.hideturtle()
icon.hideturtle()
icon.speed(0)
apple.speed(0)
maze=turtle.Screen()

maze.bgpic("maze.gif")
turtle.addshape("icon.gif")
icon.shape("icon.gif")
turtle.addshape("apple.gif")
apple.shape("apple.gif")

icon.up()
icon.goto(-380,0)
icon.showturtle()
apple.up()
apple.goto(380,0)
apple.showturtle()


def up():
    icon.setheading(90)
    icon.forward(10)    
def down():
    icon.setheading(270)
    icon.forward(10)
def left():
    icon.setheading(180)
    icon.forward(10)
def right():
    icon.setheading(0)
    icon.forward(10)

turtle.listen()

inn = "I need Food , Help me to reach That Apple . I am hungry"
engine.say(inn)
engine.runAndWait()

turtle.onkey(right,"Right")
turtle.onkey(left,"Left")
turtle.onkey(up,"Up")
turtle.onkey(down,"Down")
while True:
    turtle.update()
    if icon.distance(apple)<10:
        maze.bgpic("finish.gif")
        apple.hideturtle()
        icon.hideturtle()
        inn = "winner Winner Apple Dinner"
        engine.say(inn)
        engine.runAndWait()
    
turtle.done()
