# Hello, this code is from Dr. Angela Yu's course, which you can find on Udemy: https://www.udemy.com/course/100-days-of-code/
# This is my version of the program.

from tkinter import *

def convert_mile_to_km():
    label_result['text'] = float(entry_mile.get()) * 1.609344

root = Tk()
root.title('Mile to Kilometer Converter')

entry_mile = Entry(width=15)
entry_mile.grid(column=1, row=0)

label_is_equal_to = Label(text='is equal to')
label_is_equal_to.grid(column=0, row=1)

button_calculate = Button(text='Calculate', command=convert_mile_to_km)
button_calculate.grid(column=1, row=2)

label_result = Label()
label_result.grid(column=1, row=1)

unit_result = Label(text='Km')
unit_result.grid(column=2, row=1)

root.mainloop()