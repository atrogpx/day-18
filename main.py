from turtle import Turtle, Screen
import random
tim = Turtle()
screen = Screen()
colors = ["indigo", "snow", "orange red", "yellow", "dark olive green", "lime", "medium aquamarine", "pale turquoise", "navy", "light slate gray"]
for x in range(2, 11):
    tim.color(random.choice(colors))
    for _ in range(x):
        tim.forward(100)
        angle = 360 / x
        tim.right(angle)
screen.exitonclick()
