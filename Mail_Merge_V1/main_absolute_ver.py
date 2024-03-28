# Hello, this code is from Dr. Angela Yu's course, which you can find on Udemy: https://www.udemy.com/course/100-days-of-code/
# This is my version of the program.

#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

letter_file_path = r'\anala\Github\Python_Snippets\Mail_Merge_V1\Input\Letters\starting_letter.txt'
with open(letter_file_path, mode='r') as letter_data:
    letter = letter_data.read()

names_file_path = r'\anala\Github\Python_Snippets\Mail_Merge_V1\Input\Names\invited_names.txt'
with open(names_file_path, mode='r') as names_data:
    names_str = names_data.read()

names_list = names_str.split('\n')

letters_saving_route = r'\anala\Github\Python_Snippets\Mail_Merge_V1\Output\ReadyToSend_absolute_ver'

for name in names_list:
    new_letter = letter.replace("[name]", name)
    with open(f'{letters_saving_route}\{name}.txt', mode='w') as new_letter_data:
        new_letter_data.write(new_letter)