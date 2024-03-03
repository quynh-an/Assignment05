#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar  1 18:54:08 2024

@author: tandyllc
"""

class BasicMathOperations:
    def __init__(self):
        pass
    
    # 1: greet user    
    def greet_user(self, fName, lName):
        return print(f"Hello, {fName} {lName}!")
    
    # 2: add numbers
    def add_numbers(self):
        nums_list = []
        while True:
            q2_num1 = input("Enter a number: ")
            if '.' in q2_num1:
                try:
                    q2_num1 = float(q2_num1)
                    while True:
                        try:
                            q2_num2 = input("Enter a number to add to your first number: ")
                            if '.' in q2_num2:
                                try:
                                    q2_num2 = float(q2_num2)
                                    break
                                except:
                                    print("Invalid input. Please enter only a number.")
                                    continue
                            else:
                                try:
                                    q2_num2 = int(q2_num2)
                                    break
                                except:
                                    print("Invalid input. Please enter only a number.")  
                                    continue
                        except:
                            print("Invalid input. Please enter only a number.") 
                except:
                    print("Invalid input. Please enter only a number.")  
                    continue
            else:
                 try:
                     q2_num1 = int(q2_num1)
                     while True:
                         try:
                             q2_num2 = input("Enter a number to add to your first number: ")
                             if '.' in q2_num2:
                                 try:
                                     q2_num2 = float(q2_num2)
                                     break
                                 except:
                                     print("Invalid input. Please enter only a number.")
                                     continue
                             else:
                                 try:
                                     q2_num2 = int(q2_num2)
                                     break
                                 except:
                                     print("Invalid input. Please enter only a number.")  
                                     continue
                         except:
                             print("Invalid input. Please enter only a number.") 
                 except:
                     print("Invalid input. Please enter only a number.")  
                     continue  
            break
        nums_list.append(q2_num1)
        nums_list.append(q2_num2) 
        q2_num1 = nums_list[0]
        q2_num2 = nums_list[1]
        num_sum = q2_num1 + q2_num2
        return print("The sum of your numbers is", num_sum)
    
    # 3: perform operations
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
    
    # 4: square number
    def calculateSquare(self, number_to_square):
        square_value = round(number_to_square * number_to_square, 6)
        return square_value
    
    # 5: compute factorial
    def factorial(self):
        factorial_value = 1
        while True:
            q5_num = input("Enter a value to find its factorial. It must be a positive integer. ")
            if float(q5_num) <= 0:
                print("Invalid input. Must be positive integer.")
            else:
                try:
                    q5_num = int(q5_num)
                    for i in range(1, q5_num+1):
                        factorial_value = factorial_value * i 
                    break
                except:
                    print("Invalid input") 
        return print("The value of this factorial is", factorial_value)
    
    # 6: counting from and to a number
    def counting(self):
        print("Let's start counting!")
        while True:
            q6_num1 = input("Enter an integer to start counting! ")
            q6_num2 = input("Enter an integer to end your counting! ")
            try:
                q6_num1 = int(q6_num1)
                q6_num2 = int(q6_num2)
                for number in range(q6_num1, q6_num2 +1):
                    print(number)
                    number = number + 1
                print(" ")
                print("All done counting!")
                break
            except: 
                print("Invalid input. Try again.")
            
    # 7: calculate hypotenuse
    def calculateHypotenuse(self, base, perpendicular):
        base_squared = self.calculateSquare(base)
        perpendicular_squared = self.calculateSquare(perpendicular)
        hypotenuse = (base_squared + perpendicular_squared) ** 0.5
        return hypotenuse
    
    # 8: area of a rectangle
    def rectangular_area(self, width, height):
        area = width * height
        return area
            
    # 9: power of a number
    def number_power(self, base, exponent):
        power = base ** exponent
        return power
    
    # 10: type of argument
    def argument_type(self, argument):
        argument_type = type(argument)
        return print("The argument type is", argument_type)
        
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
                fName = user1.split()[0]
                lName = user1.split()[1]
                instance.greet_user(fName, lName)
                break
            elif selection == 2:
                instance.add_numbers()
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
                            try:
                                number_to_square = float(number_to_square)
                                square_value = instance.calculateSquare(number_to_square)
                                break
                            except:
                                print("Invalid input. Only numbers allowed.")
                        else:
                            try:
                                number_to_square = int(number_to_square)
                                square_value = instance.calculateSquare(number_to_square)
                                break
                            except:
                                print("Invalid input. Only numbers allowed.")
                    except:
                        print("Enter a valid number to square")
                print(f"The square of {number_to_square} is", square_value)
                break
            elif selection == 5:
                instance.factorial()
                break
            elif selection == 6:
                instance.counting()
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
                print("Given two numbers, we are going to find the power of a number.")
                question9(instance)
                break
            else:
                input_argument = input("Enter an argument to find its type: ")
                question10(input_argument, instance)
                break
        else:
            print("Invalid input. You must select a number between 1 and 10.")
   
    print(" ")    
    return print("Thanks for doing a task!")

# ============================================    

def question10(input_argument, instance):
    if input_argument.isdigit():
        instance.argument_type(int(input_argument))
    elif '.' in input_argument:
        try:
            instance.argument_type(float(input_argument))
        except ValueError:
            instance.argument_type(input_argument)
    elif '+' in input_argument or '-' in input_argument:
        try:
            instance.argument_type(eval(complex(input_argument)))
        except ValueError:
            instance.argument_type(input_argument)
    elif '{' in input_argument and '}' in input_argument:
        if ':' in input_argument:
            try:
                input_argument = eval(input_argument)
                instance.argument_type(input_argument)
            except ValueError:
                instance.argument_type(input_argument)
        else:
            try:
                instance.argument_type(set(input_argument))
            except ValueError:
                instance.argument_type(input_argument)
    elif '[' in input_argument and ']' in input_argument:
        try:
            instance.argument_type(list(input_argument))
        except ValueError:
            instance.argument_type(input_argument)
    elif '(' in input_argument and ')' in input_argument:
        try:
            input_argument = input_argument.lstrip('(')
            input_argument = input_argument.lstrip(')')
            if ',' in input_argument:
                instance.argument_type(tuple(input_argument))
            else:
                instance.argument_type(input_argument)
        except ValueError:
            instance.argument_type(input_argument)
    else:
        instance.argument_type(input_argument)


# ===============================================

def question9(instance):
        while True:
            q9_base = input("Enter a value for the base number for which to find the power: ")
            try:
                q9_base = int(q9_base)
                while True: 
                    try:
                        q9_exponent = input("Enter a power to which you will raise the base: ")
                        q9_exponent = int(q9_exponent)
                        power_value = instance.number_power(q9_base, q9_exponent)
                        print(f"{q9_base} to the power of {q9_exponent} is", power_value)
                        break
                    except:
                         print("The power must be an integer.")
                break
            except ValueError:
                try:
                    q9_base = float(q9_base)
                    while True: 
                       try:
                           q9_exponent = input("Enter a power to which you will raise the base: ")
                           q9_exponent = int(q9_exponent)
                           power_value = instance.number_power(q9_base, q9_exponent)
                           print(f"{q9_base} to the power of {q9_exponent} is", power_value)
                           break
                       except:
                            print("The power must be an integer.")
                    break
                except:
                    print("Invalid base number.")
            except:
                print("Invalid base number.")

# ===============================================

main()


    



