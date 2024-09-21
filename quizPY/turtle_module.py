'''from turtle import Turtle,Screen
obj.shape("turtle")
obj.color("green")
#obj.fillcolor("yellow")
obj.turtlesize(2)

for i in range(0,15):
    obj.forward(10)
    obj.penup()
    obj.forward(10)
    obj.pendown()'''
from turtle import *
import random
from turtle import Turtle,Screen
obj=Turtle()
colours=['red','blue','green','black','purple','yellow','pink','grey']
for sides in range(3,15):
    obj.shape("turtle")
    obj.setx(-100)  # Move the turtle to the left edge of the screen
    

    obj.color(random.choices(colours))
    #obj.color("green")
    #sides=8
    for i in range(sides): 
        angle=360/sides
        obj.forward(100)
        obj.right(angle)

















screen=Screen()
screen.exitonclick()