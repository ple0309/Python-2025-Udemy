# # How can we access attribute and method of a class.
# import another_module
# print(another_module.another_variable)
#
# from turtle import Turtle, Screen
#
# #timmy is object and Turtle() will be class in this scenario.
# timmy = Turtle()
# print(timmy)
# timmy.shape("turtle")
# timmy.color("DarkOrange")
# timmy.forward(100)
#
# #in the object it will have attributes and methods to do some.
# #Example:
# #   attributes:
# #       speed = 0
# #       fuel = 32
# #   methods:
# #       def move():
# #           speed = 60
# #       def stop():
# #           speed = 0
#
# my_screen = Screen()
# print(my_screen.canvheight)
# print(my_screen.canvwidth)
# my_screen.exitonclick()

#Practicing
from prettytable import PrettyTable
table = PrettyTable()
table.add_column("Pokemon Name",["Pikachu","Squirtle","Charmander"])
table.add_column("Type", ["Electric", "Water", "Fire"])

table.align = "l"

print(table)


