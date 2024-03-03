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
    
    # square number
    def calculateSquare(self, number):
        square_value = number**2
        return square_value
    
    # compute factorial
    def factorial(self, q5_number):
        factorial_value = 1
        for i in range(1, q5_number+1):
            factorial_value = factorial_value * i 
        return factorial_value
    
    # counting from and to a number
    def counting(self, q6_number1, q6_number2):
        print("Let's start counting!")
        for number in range(q6_number1, q6_number2 +1):
            print(number)
            number = number + 1
            
    # calculate hypotenuse
    def calculateHypotenuse(self, base, perpendicular):
        base_squared = self.calculateSquare(base)
        perpendicular_squared = self.calculateSquare(perpendicular)
        hypotenuse = (base_squared + perpendicular_squared) ** 0.5
        return hypotenuse
    
    # area of a rectangle
    def rectangular_area(self, width, height):
        area = width * height
        return area
            
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
                        print("Invalid input. Please follow the directions.")
                break
            elif selection == 4:
                while True:
                    number_to_square = input("Enter a number to find its square: ")
                    try:
                        if '.' in number_to_square:
                            number_to_square = float(number_to_square)
                            print(f"The squared value of {number_to_square} is", instance.calculateSquare(number_to_square))
                        else:
                            number_to_square = int(number_to_square)
                            print(f"The squared value of {number_to_square} is", instance.calculateSquare(number_to_square))
                        break
                    except:
                        print("Enter a valid number to square")
                break
            elif selection == 5:
                while True:
                    q5_num = input("Enter a value to find its factorial. It must be a positive integer. ")
                    if float(q5_num) <= 0:
                        print("Invalid input. Must be positive integer.")
                    else:
                        try:
                            q5_num = int(q5_num)
                            print("The factorial of this number is", instance.factorial(q5_num))
                            break
                        except:
                            print("Invalid input") 
                break
            elif selection == 6:
                while True:
                    q6_num1 = input("Enter an integer to start counting! ")
                    q6_num2 = input("Enter an integer to end your counting! ")
                    try:
                        q6_num1 = int(q6_num1)
                        q6_num2 = int(q6_num2)
                        instance.counting(q6_num1, q6_num2)
                        print(" ")
                        print("All done counting!")
                        break
                    except: 
                        print("Invalid input. Try again.")
                break
            elif selection == 7:
                while True:
                    base = input("Enter a value for the base of your triangle: ")
                    try:
                        base = float(base)
                        if base > 0:
                            while True:
                                perpendicular = input("Enter a value for the perpendicular of your triangle: ")
                                try:
                                    perpendicular = float(perpendicular)
                                    print("The hypotenuse is", instance.calculateHypotenuse(base, perpendicular))
                                    break
                                except:
                                    print("Please enter a number value.")
                            break
                        else:
                            print("Invalid base value. Must be a number greater than 0.")
                    except:
                        print("Please enter a valid value for the base.")
                break
            elif selection == 8:
                while True:
                    q8_width = input("Enter the width of your rectangle: ")
                    try: 
                        q8_width = float(q8_width)
                        while True:
                            try:
                                q8_height = input("Enter the height of your rectangle: ")
                                q8_height = float(q8_height)
                                print("The area of your rectangle is", instance.rectangular_area(q8_width, q8_height))
                                break
                            except:
                                 print("Invalid height.") 
                        break
                    except:
                        print("Invalid width.")
                break
            elif selection == 9:
                break
            else:
                break
        else:
            print("Invalid input. You must select a number between 1 and 10.")
   
    print(" ")    
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


    



