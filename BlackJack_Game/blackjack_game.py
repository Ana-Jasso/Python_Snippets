# Hello, this code is from Dr. Angela Yu's course, which you can find on Udemy: https://www.udemy.com/course/100-days-of-code/
# This is my version of the program.

# Credits for ASCII Art
# Drawing: https://ascii.co.uk/art/gavel
# Text: https://ascii.co.uk/art/auction

def display_Ascii_text():
    print('''
    _     _            _    _            _    
    | |   | |          | |  (_)          | |   
    | |__ | | __ _  ___| | ___  __ _  ___| | __
    | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
    | |_) | | (_| | (__|   <| | (_| | (__|   < 
    |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\ 
                           _/ |                
                          |__/
    ''')

display_Ascii_text()

# Assuming that we have an infinite deck
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10] # The value of 11 can change based on whether the result is above or below 21.