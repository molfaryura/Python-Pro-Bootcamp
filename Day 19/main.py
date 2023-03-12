import turtle

import random

screen = turtle.Screen()
screen.setup(width=500, height=400)
user_input = screen.textinput(title="Make your bet", prompt="Which color will win the race? Enter: ")

colors = ['red', 'green', 'blue', 'black', 'orange', 'yellow']

my_turtles = []


x = (500/2-20) * -1
y = (400/2-100) * -1

for _ in range(6):
    my_turtle = turtle.Turtle(shape='turtle')
    my_turtles.append(my_turtle)
    color = random.choice(colors)
    my_turtle.color(color)
    colors.remove(color)

    my_turtle.penup()
    my_turtle.goto(x, y)

    y += 40

continue_race = True

while continue_race:
    for my_turtle in my_turtles:
        my_turtle.forward(random.randint(0, 10))

        if my_turtle.xcor() >= -x:
            continue_race = False
            winner = my_turtle.pencolor()

            if user_input.lower() == winner:
                print(f"You have won. The winner of the race is {winner} turtle!")
                break
            else:
                print(f"You have lost. The winner of the race is {winner} turtle.")
                break

screen.exitonclick()
