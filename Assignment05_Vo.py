#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar  1 18:54:08 2024

@author: tandyllc
"""

class BasicMathOperations:
    def __init__(self):
        pass
    
    # greet user    
    def greet_user(self, fName, lName):
        return print(f"Hello, {fName} {lName}!")
    
    # add numbers
    def add_numbers(self, num1, num2):
        sum = num1 + num2
        return sum
    
    # perform operations
    def perform_operations(self, num1, num2, operator):
        if operator == "+":
            result = num1 + num2
        elif operator == "-":
            result = num1 - num2
        elif operator == "/":
            result = num1 / num2
        else:
            result = num1 * num2
        return result
        
def main():
    instance1 = BasicMathOperations()
    print(""""
You can chose to do any of the following.
          
1) Greet the user
2) Add numbers
3) Perform a math operation
4) Square a number
5) Find the factorial
6) Counting
7) Compute the hypotenuse
8) Area of a rectangle
9) Power of a number
10) Type of argument
          
""")
    while True:
        selection = input("Please make a selection based on the number of the options: ")
        try: 
            selection = int(selection)
        except ValueError:
            print("Invalid input. You must select a single number 1-10.")
            continue
        if 1 <= selection <= 10:
            if selection == 1:
                user1 = input("Enter your first and last name, separated by a space: ")
                user1_fName = user1.split()[0]
                user1_lName = user1.split()[1]
                instance1.greet_user(user1_fName, user1_lName)
                break
            elif selection == 2:
                q2_num1 = input("Enter a number: ")
                q2_num2 = input("Enter a number to add to your first number: ")
                
            elif selection == 3:
                break
            elif selection == 4:
                break
            elif selection == 5:
                break
            elif selection == 6:
                break
            elif selection == 7:
                break
            elif selection == 8:
                break
            elif selection == 9:
                break
            else:
                break
        else:
            print("Invalid input. You must select a number between 1 and 10.")
        
    return print("Thanks for doing a task!")
                
main()


    



