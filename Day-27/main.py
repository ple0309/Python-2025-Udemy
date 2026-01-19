#********************** Advanced Python Arguments *************************
# *args: Many Positional Arguments
# Unlimited Arguments: can print each arguments like add(1,2,3,4,5,.....)
# def add(*args):
#     for n in args:
#         print(n)
#**************************************************************************
# **kwargs: many Keyword Arguments (Type dict)
# It will loop through each keyword arguments
# def calculate(**kwargs):
#     print(kwargs)
# Example output: {'add':3,'multiply':5} when input calculate(add=3,multiply=5)
#**************************************************************************
#Using tkinter to set up window console.
from tkinter import *

window = Tk()
window.title("My First GUI Program")
window.minsize(width=500, height= 300)
#Add padding like in CSS
window.config(padx=20,pady=20)

#Label
my_label = Label(text="I Am a Label", font=("Arial", 24, "bold"))
my_label.config(text="New Text")
my_label.grid(column=0, row=0)

# #both way the same
# my_label["text"] = "New Text"
# my_label.config(text="New Text")

#Button
def button_clicked():
    new_text = input.get()
    my_label.config(text=new_text)

button = Button(text="Click Me",command=button_clicked)
button.grid(column=1, row=1)

new_button = Button(text="New Button")
new_button.grid(column=2, row=0)

#Entry
input = Entry(width=10)
print(input.get())
input.grid(column=3, row=2)

#Label, Button, Entry, Text, Spinbox, Scale, Checkbutton, Radiobutton, Listbox

#**************************************************************************
#Defaul Value in write method will show when we hover in it.
#However, pack method above will show dict values and **kw.
# import turtle
#
# tim = turtle.Turtle()
# tim.write()

window.mainloop()

#************************** Additional Information ****************************
#******************************************************************************
# my_label.pack(side="left") or right
# my_label.place(x=0,y=0) will work with x and y

#Each position will go like diagonal.
# my_label.grid(column=0, row=0)
# my_label.grid(column=1, row=1)
# my_label.grid(column=2, row=2)