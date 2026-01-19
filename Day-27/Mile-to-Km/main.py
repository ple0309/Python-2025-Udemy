from tkinter import *

window = Tk()
window.title("Mile to Km Converter")
window.config(padx=20, pady=20)

miles_input = Entry(width=10)
miles_input.grid(column=1, row=0)

miles = Label(text="Miles")
miles.grid(column=2,row=0)

is_equal = Label(text="is equal to")
is_equal.grid(column=0, row=1)

converted = Label(text="0")
converted.grid(column=1, row=1)

km = Label(text="Km")
km.grid(column=2, row=1)

def calculate():
    m = int(miles_input.get())
    k = m * 1.6
    converted.config(text=str(int(k)))

button = Button(text="Calculate",width=10, command=calculate)
button.grid(column=1, row=2)

window.mainloop()