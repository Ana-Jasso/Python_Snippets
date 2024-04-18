# Hello, this code is from Dr. Angela Yu's course, which you can find on Udemy: https://www.udemy.com/course/100-days-of-code/
# This is my version of the program.

from tkinter import *

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
CHECKMARK_STR = '✔'

# ---------------------------- TIMER RESET ------------------------------- # 

# ---------------------------- TIMER MECHANISM ------------------------------- # 

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 

# ---------------------------- UI SETUP ------------------------------- #

root = Tk()
root.title('Pomodoro')
root.config(padx=100, pady=50, bg=PINK)

# TITLE TEXT
timer_label = Label(text='Timer', fg=RED, bg=PINK, font=(FONT_NAME, 60))
timer_label.grid(column=1, row=0)

# IMG
canvas = Canvas(width=200, height=224, bg=PINK, highlightthickness=0)
tomato_img = PhotoImage(file=r'Pomodoro_App_V1\tomato.png')
canvas.tomato_img = tomato_img
canvas.create_image(100, 112, image=canvas.tomato_img)
canvas.create_text(100, 130, text='00:00', fill='white', font=(FONT_NAME, 35, 'bold'))
canvas.grid(column=1, row=1)

# START BUTTON
star_button = Button(text='Start')
star_button.grid(column=0, row=2)

# RESET BUTTON
reset_button = Button(text='Reset')
reset_button.grid(column=2, row=2)

checkmark_button = Button(text=CHECKMARK_STR, fg=GREEN, bg="white")
checkmark_button.grid(column=1, row=3)

root.mainloop()