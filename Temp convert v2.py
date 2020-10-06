# -*- coding: utf-8 -*-
"""
Created on Fri Sep 25 09:44:24 2020

@author: fayth
"""
# prompting user for which temp they know
# so we can figure out which one to use for conversion
menu_main=("Which temperature do you have that you are converting?\n"
           "Please enter only the number\n"
           "1.Fahrenheit\n"
           "2.Celsius\n"
           "3.Kelvin\n")
command_main = input(menu_main).lower().strip()
while True:
    if command_main == '1':
        user_temp_f = input('Please enter your temperature:')
        break
    elif command_main == '2':
        user_temp_c = input('Please enter your temperature:')
        break
    elif command_main == '3':
        user_temp_k =input('Please enter your temperature:')
        break


# converting Fahrenheit to Celsius
# passing variable from above if selected as the base temp to convert to Celsius
def f_to_c():
    temp_c = (temp_f - 32) * 5/9
    return temp_c
temp_f = user_temp_f
temp_c = f_to_c()

# converting Celsius to Fahrenheit
# prompting user for temperature in celsius
def c_to_f():
    temp_f = temp_c * 9/5 +32
    return temp_f
temp_c = user_temp_c or temp_c
temp_f = c_to_f()


# converting Fahrenheit to Kelvins
# passing the function from before as the temp for temp_f
def f_to_k():
    temp_k = (temp_f - 32) * 5/9 + 273.15
    return temp_k
temp_f = user_temp_f or temp_f
temp_k = f_to_k()

# converting kelvin to Fahrenheit
# passing function prior or user input in main menu


menu_prompt= ("Please select what you want to convert to\n"
              "1.Convert to Fahrenheit\n"
              "2.Convert to Kelvin\n"
              "3.Quit\n")
while True:
    command = input(menu_prompt).lower().strip()
    if command == '1':
        print('Temperature in Fahrenheit is:',temp_f)
        print()
    elif command == '2':
        print('Temperature in Kelvin is:',temp_k)
        print()
    elif command == '3':
        break
    else:
        print('Error! Command not recognized! Please check your input and try again')
        print()
