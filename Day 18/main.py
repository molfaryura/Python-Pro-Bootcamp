import turtle

import random

#import colorgram

turtle.colormode(255)

my_turtle = turtle.Turtle()

my_turtle.hideturtle()
my_turtle.penup()
my_turtle.speed(0)

#colors = colorgram.extract('./Day 18/image.jpg', 15)

#rgb_colors = [tuple(color.rgb) for color in colors]

color_list = [(226, 231, 235), (57, 106, 146), (133, 92, 60), (223, 201, 113), (223, 233, 229),
              (235, 226, 205), (219, 151, 70), (149, 179, 201), (193, 145, 170), (213, 93, 61),
              (139, 80, 105), (238, 224, 233), (65, 106, 90), (136, 181, 138), (187, 79, 119)]



my_turtle.setheading(225)
my_turtle.forward(300)
my_turtle.setheading(0)

for i in range(1, 101):
    my_turtle.dot(25, random.choice(color_list))
    my_turtle.forward(50)

    if i % 10 == 0:
        my_turtle.setheading(90)
        my_turtle.forward(50)
        my_turtle.setheading(180)
        my_turtle.forward(500)
        my_turtle.setheading(0)
    else:
        continue


screen = turtle.Screen()
screen.exitonclick()
