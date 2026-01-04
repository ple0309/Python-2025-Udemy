import turtle as turtle_module
import random

# #Using the code below to get the list of color from image.
# #Then put them into list_color list.
# import colorgram
#
# colors = colorgram.extract('image.jpg', 30)
# color_list = []
# for i in colors:
#     new_color = (i.rgb.r, i.rgb.g, i.rgb.b)
#     color_list.append(new_color)
# print(color_list)

tim = turtle_module.Turtle()
tim.speed("fastest")
tim.penup()
tim.hideturtle()
turtle_module.colormode(255)
list_color = [(251, 251, 249), (252, 248, 250), (246, 251, 248), (243, 246, 250), (223, 151, 97), (224, 63, 96), (121, 167, 200), (41, 112, 146), (116, 182, 149), (239, 213, 80), (206, 134, 156), (48, 118, 80), (139, 75, 56), (149, 65, 99), (175, 152, 62), (233, 88, 75), (44, 157, 197), (173, 184, 221), (240, 164, 199), (46, 170, 119), (159, 215, 155), (51, 57, 91), (158, 203, 211), (237, 172, 153), (70, 130, 195), (236, 214, 14), (41, 53, 77), (41, 81, 44), (72, 78, 43), (196, 21, 62)]


#Setting up the start position (0,0) because the point will start
#at the center of the screen. So moving it toward Southwest.
tim.setheading(225)  #180 + 45 (halfway to get the (x,y) like (0,0)
tim.forward(300)     #each gap is 50 so 5 gaps will be 250.
                     #but adding 50 to gain more space.
tim.setheading(0)    #turning back the start point at (0,0)
number_of_dots = 100

for dot_count in range(1,number_of_dots + 1):
    tim.dot(20,random.choice(list_color))
    tim.forward(50)

    if dot_count % 10 == 0:
        tim.setheading(90)
        tim.forward(50)
        tim.setheading(180)
        tim.forward(500)
        tim.setheading(0)    #turning back the start point at (0,0)


screen = turtle_module.Screen()
screen.exitonclick()