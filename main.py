import turtle
from turtle import Turtle, Screen
from random import randint

screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Which colored turtle do you think would win?")
colors = ["red", "orange", "blue", "yellow", "green", "purple"]
is_race_on = False


def make_turtles():
    l = []
    for i in range(6):
        t = Turtle(shape="turtle")
        t.color(colors[i])
        l.append(t)
    return l


def starting_pos(turtle_list):
    y = 120
    for t in turtle_list:
        t.penup()
        t.goto(-230, y)
        y -= 40
    return


if user_bet in colors:
    is_race_on = True

all_turtles = make_turtles()
starting_pos(all_turtles)

winner=''

while is_race_on:
    for t in all_turtles:
        if t.xcor()>230:
            winner=t.pencolor()
            is_race_on=False
            break
        rd=randint(1,10)
        t.forward(rd)

if(winner==user_bet):
    print("Your bet was right")
else:
    print(f"You lost. {winner.title()} won the race")

t=input()