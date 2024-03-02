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
        num_sum = float(num1) + float(num2)
        return print("The sum of your numbers is", num_sum)
    
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
        return print("The result of the operation is", result)
# ============================================        
def main():
    instance = BasicMathOperations()
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
                instance.greet_user(user1_fName, user1_lName)
                break
            elif selection == 2:
                nums = question2()
                print(nums)
                q2_num1 = nums[0]
                q2_num2 = nums[1]
                instance.add_numbers(q2_num1, q2_num2)
                break
            elif selection == 3:
                while True:
                    valid_operators = [ "+", "-", "/", "*"]
                    equation = input("Enter a basic math equation using numbers and the +, -, /, * operators. Separate each with a space. " )
                    try:
                        equation_parts = equation.split()
                        q3_num1 = float(equation_parts[0])
                        input_operator = equation_parts[1]
                        q3_num2 = float(equation_parts[2])
                        if input_operator in valid_operators:
                            instance.perform_operations(q3_num1, q3_num2, input_operator)
                            break
                        else:
                            print("Operators must be +, -, /, or *. Try again.")
                    except:
                        print("Invalid math question.")
                                
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

# ============================================    
            
def question2():
    nums_list = []
    while True:
        try:
            q2_num1 = float(input("Enter a number: "))
        except:
            print("Invalid input. Please enter only a number.")  
            continue
        while True:
            try:
                q2_num2 = float(input("Enter a number to add to your first number: "))
                break
            except:
                print("Invalid input. Please enter only a number.") 
        break
    nums_list.append(q2_num1)
    nums_list.append(q2_num2)    
    return nums_list

# ============================================    
    

main()


    



