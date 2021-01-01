import turtle
import random
from turtle_racer import Racer

screen = turtle.Screen()
screen.screensize(canvwidth=500, canvheight=400)


colours = ['red', 'blue', 'green', 'yellow']
starting_point = [-200, -100, 0, 100]


def setup_race():
    screen.turtles().clear()
    screen.bgpic("finish_line.png")
    for i in range(0, len(colours)):
        racer = turtle.Turtle(shape='turtle')
        racer.penup()
        racer.fillcolor(colours[i])
        racer.goto(x=-300, y=starting_point[i])


def start_race():
    setup_race()
    print('GO!')
    race_on = True
    winner = ''
    while race_on:
        for t_racer in screen.turtles():
            if t_racer.xcor() <= 40:
                t_racer.forward(random.randint(0, 10))
            else:
                race_on = False
                winner = t_racer.fillcolor()
    return winner


def race_process():
    bet = screen.textinput(title='Place your bet!',
                           prompt='Type a which colour turtle do you expect to win (red/blue/green/yellow): ').lower()
    winner = start_race()
    if winner == bet:
        replay = screen.textinput(title='CONGRATS!',
                                  prompt=f'Your {winner} turtle won!\nPlay again? Type \'yes\' or \'no\': ').lower()
    else:
        replay = screen.textinput(title=f'OPS! Your turtle lost',
                                  prompt=f'The {winner} one won.\nWanna try again? Type \'yes\' or \'no\': ').lower()
    screen.clear()
    if replay == 'yes':
        race_process()
    else:
        print('Bye!')


screen.listen()
race_process()
screen.exitonclick()
