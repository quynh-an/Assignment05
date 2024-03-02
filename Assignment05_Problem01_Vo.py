#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar  1 18:54:08 2024

@author: tandyllc
"""

class BasicMathOperations:
    def __init__(self, fName, lName):
        self.fName = fName
        self.lName = lName
        
    def greet_user(self):
        print(f"Hello, {self.fName} {self.lName}")
        
    
def greet_user(user):
    return user.greet_user()
    
user1 = input("Enter your first and last name, separated by a space: ")
user1_fName = user1.split()[0]
user1_lName = user1.split()[1]
user1 = BasicMathOperations(user1_fName, user1_lName)
user1.greet_user()