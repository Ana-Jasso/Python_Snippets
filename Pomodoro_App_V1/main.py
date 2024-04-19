# Hello, this code is from Dr. Angela Yu's course, which you can find on Udemy: https://www.udemy.com/course/100-days-of-code/
# This is my version of the program.

from tkinter import *
import math

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = '#416D19' #"#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 1
SHORT_BREAK_MIN = 1
LONG_BREAK_MIN = 20
CHECKMARK_STR = '✔'
checkmarks = ''
reps = 0
timer = None

# ---------------------------- TIMER RESET ------------------------------- # 

def reset_timer():
    global reps
    root.after_cancel(timer)
    timer_label.config(text='Timer', fg=RED)
    canvas.itemconfig(timer_text, text='00:00')
    checkmark_label.config(text='')
    reps = 0

# ---------------------------- TIMER MECHANISM ------------------------------- # 

def start_timer():
    global reps
    reps += 1
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    if reps % 8 == 0:
        timer_label.config(text='Long Break', fg=GREEN)
        count_down(long_break_sec)
    elif (reps % 2 == 0):
        timer_label.config(text='Short Break', fg=YELLOW)
        count_down(short_break_sec)
    else:
        timer_label.config(text='Work', fg=RED)
        count_down(work_sec)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 

def count_down(count):
    global checkmarks
    global reps
    global timer
    count_min = math.floor(count / 60)
    count_sec = count % 60
    canvas.itemconfig(timer_text, text= f'{"{:02d}".format(count_min)}:{"{:02d}".format(count_sec)}')
    if count > 0:
        timer = root.after(1000, count_down, count -1)
    else:
        if (reps>=1) and not (reps % 2 == 0):
            checkmarks += '✔'
        checkmark_label.config(text=checkmarks)
        start_timer()

# ---------------------------- UI SETUP ------------------------------- #

root = Tk()
root.title('Pomodoro')
root.config(padx=100, pady=50, bg=PINK)

# TITLE TEXT
timer_label = Label(text='Timer', fg=RED, bg=PINK, font=(FONT_NAME, 60))
timer_label.grid(column=1, row=0)

# CANVAS
# IMG
canvas = Canvas(width=200, height=224, bg=PINK, highlightthickness=0)
tomato_img = PhotoImage(file=r'Pomodoro_App_V1\tomato.png')
canvas.tomato_img = tomato_img
canvas.create_image(100, 112, image=canvas.tomato_img)
# TEXT
timer_text = canvas.create_text(100, 130, text='00:00', fill='white', font=(FONT_NAME, 35, 'bold'))
canvas.grid(column=1, row=1)

# START BUTTON
star_button = Button(text='Start', command=start_timer)
star_button.grid(column=0, row=2)

# RESET BUTTON
reset_button = Button(text='Reset', command=reset_timer)
reset_button.grid(column=2, row=2)

# CHECKMARK LABEL
checkmark_label = Label(text=checkmarks, fg=GREEN, bg=PINK)
checkmark_label.grid(column=1, row=3)

root.mainloop()