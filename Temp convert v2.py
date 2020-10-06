# -*- coding: utf-8 -*-
"""
Created on Fri Sep 25 09:44:24 2020

@author: TechnoVixen-Natani aka Fayth
"""


# converting Fahrenheit to Celsius
def f_to_c(temp_f):
    temp_c = (temp_f - 32) * 5 / 9
    return temp_c


# converting Celsius to Fahrenheit
def c_to_f(temp_c):
    temp_f = temp_c * 9 / 5 + 32
    return temp_f


# converting Fahrenheit to Kelvin
def f_to_k(temp_f):
    temp_k = (temp_f - 32) * 5 / 9 + 273.15
    return temp_k


# converting Celsius to Kelvin
def c_to_k(temp_c):
    temp_k = temp_c + 273.15
    return temp_k


# converting Kelvin to Fahrenheit
def k_to_f(temp_k):
    temp_f = (temp_k - 273.15) * 9 / 5 + 32
    return temp_f


# converting kelvin to Celsius
def k_to_c(temp_k):
    temp_c = temp_k - 273.15
    return temp_c


# function to display all temperatures
def all_temps(user_temp_f, user_temp_c, user_temp_k):
    print("\nThe temperature in Fahrenheit is:", round(user_temp_f, 2))
    print("\nThe temperature in Celsius is:", round(user_temp_c, 2))
    print("\nThe temperature in Kelvin is:", round(user_temp_k, 2))


# menu prompt for user with loop so they can choose to keep trying other temps.
menu_main = ("\nWhich temperature are you converting from?\n"
             "Please select from list\n"
             "1.Fahrenheit\n"
             "2.Celsius\n"
             "3.Kelvin\n"
             "4.Quit\n")
while True:
    command_main = input(menu_main).lower().strip()
    if command_main == '1':
        user_temp_f = float(input('Please enter your temperature:'))
        user_temp_c = f_to_c(user_temp_f)
        user_temp_k = f_to_k(user_temp_f)
        all_temps(user_temp_f, user_temp_c, user_temp_k)

    elif command_main == '2':
        user_temp_c = float(input('Please enter your temperature:'))
        user_temp_k = c_to_k(user_temp_c)
        user_temp_f = c_to_f(user_temp_c)
        all_temps(user_temp_f, user_temp_c, user_temp_k)

    elif command_main == '3':
        user_temp_k = float(input('Please enter your temperature:'))
        user_temp_f = f_to_k(user_temp_k)
        user_temp_c = c_to_k(user_temp_k)
        all_temps(user_temp_f, user_temp_c, user_temp_k)
        print()
    elif command_main == '4':
        print('Thank you for using my Temperature converter, have a nice day!')
        break

    else:
        print('Command not recognized, please check your input and try again.')
print()
