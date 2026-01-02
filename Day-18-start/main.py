# from turtle import Turtle, Screen
# timmy_the_turtle = Turtle()
# timmy_the_turtle.shape("turtle")
# timmy_the_turtle.color("red")

# #Drawing a Square by Turtle
# for _ in range(4):
#     timmy_the_turtle.forward(100)
#     timmy_the_turtle.right(90)


# #Drawing a Dashed Line
# for _ in range(20):
#     timmy_the_turtle.forward(10)
#     timmy_the_turtle.penup()
#     timmy_the_turtle.forward(10)
#     timmy_the_turtle.pendown()


# #Drawing different shapes
# import turtle as t
# import random
# from turtle import Screen
# tim = t.Turtle()
#
# colours = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]
#
# def draw_shape(num_sides):
#     angle = 360 / num_sides
#     for _ in range(num_sides):
#         tim.forward(100)
#         tim.right(angle)
#
# for shape_side_n in range(3,11):
#     tim.color(random.choice(colours))
#     draw_shape(shape_side_n)



# #Drawing different ways
# import turtle as t
# import random
# from turtle import Screen
#
# tim = t.Turtle()
# colours = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]
# directions = [0,90,180,270]
# tim.pensize(15)
# tim.speed("fastest")
#
# for _ in range(200):
#     tim.color(random.choice(colours))
#     tim.forward(30)
#     tim.setheading(random.choice(directions))



#tuple can access like the list but can not change element inside.
import turtle as t
import random
from turtle import Screen

tim = t.Turtle()
t.colormode(255)

def random_color():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    random_color = (r,g,b)
    return random_color

directions = [0,90,180,270]
tim.pensize(15)
tim.speed("fastest")

for _ in range(200):
    tim.color(random_color())
    tim.forward(30)
    tim.setheading(random.choice(directions))


screen = Screen()
screen.exitonclick()




#**** Lesson ******
#Kind of import
#keyword Module
#import turtle
# tim = turtle.Turtle()

#else:
#Keyword Module keyword Thing in module
#from turtle import Turtle
#tim = Turtle()

#Avoid using this style because something making confused.
#from turtle import * // import everything with *
#from random import *

#Aliasing Modules
#keyword Module name keyword alias name
# import turtle as t
# tim = t.Turtle()

#Installing Module
#just install what we need
# import heroes
# print(heroes.gen())

#import villains