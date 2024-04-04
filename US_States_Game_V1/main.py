# Hello, this code is from Dr. Angela Yu's course, which you can find on Udemy: https://www.udemy.com/course/100-days-of-code/
# This is my version of the program.

import turtle
import pandas as pd

# Functions
def get_mouse_click_coor(x,y):
    print(x,y)

# Window
screen = turtle.Screen()
screen.title('U.S. States Game')
image = r'US_States_Game_V1\blank_states_img.gif'
screen.addshape(image)
turtle.shape(image)

# Data
df_US_states = pd.read_csv(r'US_States_Game_V1\50_states.csv')


# While Loop
number_of_states = df_US_states.shape[0]
correct_answers = 0
answers_list = []
states = df_US_states['state'].tolist()

while correct_answers < number_of_states:
    answer_input = screen.textinput(title=f'Guess the state {correct_answers}/{number_of_states}', prompt="What's another state name?").title()
    if answer_input == 'Exit':
        missing_states = [missing_state for missing_state in states if (missing_state not in answers_list)]
        with open(r'US_States_Game_V1\missing_states.txt', 'w') as archivo:
            archivo.write("US states to review:\n")
            for missing_state in missing_states:
                archivo.write(f"{missing_state}\n")
        break
    elif (answer_input in states) and (answer_input not in answers_list):

        x_coor = df_US_states['x'][df_US_states['state']==answer_input].iloc[0]
        y_coor = df_US_states['y'][df_US_states['state']==answer_input].iloc[0]
        coordinates = (x_coor, y_coor)

        t = turtle.Turtle()
        t.hideturtle()
        t.goto(coordinates)
        t.write(answer_input)

        answers_list.append(answer_input)
        correct_answers += 1

screen.title('U.S. States Game -- Result')
turtle.mainloop()