from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
#Using color hunt website to get pattern of colors.
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None

# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    window.after_cancel(timer)

    #timer_text 00:00
    canvas.itemconfig(timer_text,text="00:00")

    #timer_label "Timer"
    timer_label.config(text="Timer")

    #reset check_mark
    check_mark.config(text="")

    global reps
    reps = 0

# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps
    reps += 1

    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    if reps % 8 == 0:
        # If it's the 8th rep:
        count_down(long_break_sec)
        timer_label.config(text="Break",fg=RED)
    elif reps % 2 == 0:
        #If it's 2nd/4th/6th rep:
        count_down(short_break_sec)
        timer_label.config(text="Break",fg=PINK)

    else:
        # If it's the 1st/3rd/5th/7th rep:
        count_down(work_sec)
        timer_label.config(text="Work",fg=GREEN)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    count_min = math.floor(count / 60)
    count_sec = count % 60

    canvas.itemconfig(timer_text,text=f"{count_min:02d}:{count_sec:02d}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        mark = ""
        work_sessions = math.floor(reps/2)
        for _ in range(work_sessions):
            mark += "✔"
        check_mark.config(text = mark)

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady= 50, bg=YELLOW)


#Add the tomato picture
canvas = Canvas(width=200, height=224,bg=YELLOW, highlightthickness=0) #highlightthickness will set the border = 0
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100,112, image=tomato_img) # x and y

#Write the text above the tomato picture
timer_text = canvas.create_text(100,130,text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1,row=1)


#Label
timer_label = Label(text="Timer",font=(FONT_NAME, 40, "bold"), fg=GREEN, bg=YELLOW)
timer_label.grid(column=1, row=0)

check_mark = Label(fg=GREEN, bg=YELLOW)
check_mark.grid(column=1, row=3)

#Button
start = Button(text="Start", highlightthickness=0, command=start_timer)
start.grid(column=0,row=2)

restart = Button(text="Restart",highlightthickness=0, command=reset_timer)
restart.grid(column=2, row=2)


window.mainloop()