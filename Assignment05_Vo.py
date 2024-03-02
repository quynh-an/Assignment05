#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar  1 18:54:08 2024

@author: tandyllc
"""

class BasicMathOperations:
    def __init__(self):
        pass
        
    def greet_user(fName, lName):
        print(f"Hello, {fName} {lName}!")
        
    def add_numbers(num1, num2):
        sum = num1 + num2
        return sum
        
    
def greet_user(user):
    user1 = input("Enter your first and last name, separated by a space: ")
    user1_fName = user1.split()[0]
    user1_lName = user1.split()[1]
    BasicMathOperations.greet_user(user1_fName, user1_lName)
    return user.greet_user()
    



