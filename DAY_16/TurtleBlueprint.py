"""Using the turtle external library"""
from turtle import Turtle, Screen

timmy = Turtle()
print(timmy)
timmy.shape("turtle")
timmy.color("cyan")

timmy.forward(200)
timmy.backward(200)


my_screen = Screen()
print(my_screen.canvheight)
my_screen.exitonclick()





