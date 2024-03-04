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
        while True:
            q2_num1 = input("Enter a number: ")
            # checing for period is checking for float
            if '.' in q2_num1:
                # test out float if not float and not int, then invalid input
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
            # see if input is an integer
            else:
                 try:
                     q2_num1 = int(q2_num1)
                     # if it is an integer then ask for next number to add, test float or int again
                     while True:
                         try:
                             q2_num2 = input("Enter a number to add to your first number: ")
                             # check if float or int, print error if neither
                             # break loop if either
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
        # find the sum
        num_sum = round(q2_num1 + q2_num2, 4)
        # return the sum
        return print("The sum of your numbers is", num_sum)
    
    # 3: perform operations
    def perform_operations(self, num1, num2, operator):
        # perform opersation based on *, /, -, +
        # return result
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
        # calculate the square, input number can be float or int round number and return
        square_value = round(number_to_square * number_to_square, 6)
        return square_value
    
    # 5: compute factorial
    def factorial(self):
        # set factorial to one, since all start there
        factorial_value = 1
        while True:
            # ask for a value to find the factorial
            q5_num = input("Enter a value to find its factorial. It must be a positive integer. ")
            # value must be above 0 and an int
            # if not above 0, then try again
            if float(q5_num) <= 0:
                print("Invalid input. Must be positive integer.")
            else:
                # test if it is an int
                # if nto, then invalid input
                try:
                    q5_num = int(q5_num)
                    # circulate through 1 to the value itself and multiply for factorial
                    for i in range(1, q5_num+1):
                        factorial_value = factorial_value * i 
                    break
                except:
                    print("Invalid input") 
        return print("The value of this factorial is", factorial_value)
    
    # 6: counting from and to a number
    def counting(self, start_num, end_num):
        print("Let's start counting!")
        # iterate from starting num to ending number and print to count
        for number in range(start_num, end_num +1):
            print(number)
            number = number + 1

    # 7: calculate hypotenuse
    def calculateHypotenuse(self, base, perpendicular):
        # square the base
        base_squared = self.calculateSquare(base)
        # square the perpendicular
        perpendicular_squared = self.calculateSquare(perpendicular)
        # find hypotenuse and return
        hypotenuse = (base_squared + perpendicular_squared) ** 0.5
        return hypotenuse
    
    # 8: area of a rectangle
    def rectangular_area(self, width, height):
        # use width and height to multiply and find area
        area = width * height
        return area
            
    # 9: power of a number
    def number_power(self, base, exponent):
        # calculate power
        power = base ** exponent
        return round(power, 4)
    
    # 10: type of argument
    def argument_type(self, argument):
        argument_type = type(argument)
        return print("The argument type is", argument_type)
        
# ============================================        
def main():
    # Create an Instance of this Class
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
        # ask user for a choice task
        selection = input("Please make a selection based on the number of the options: ")
        try: 
            # make sure selection is a valid number
            selection = int(selection)
        except ValueError:
            print("Invalid input. You must select a single number 1-10.")
            continue
        if 1 <= selection <= 10:
            if selection == 1:
                # ask for first and last name
                while True:
                    user1 = input("Enter your first and last name, separated by a space: ")
                    # ensure there is a first and last name, no more, no less
                    # loop through if input invalid
                    if 0 < len(user1.split()) <= 2:
                        try:
                            fName = user1.split()[0]
                            lName = user1.split()[1]
                            instance.greet_user(fName, lName)
                            break
                        except:
                            print("Invalid input. Must only put first and last name.")
                    else:
                        print("Invalid input. Must only put first and last name.")
                break
            elif selection == 2:
                # call add numbers
                instance.add_numbers()
                break
            elif selection == 3:
                while True:
                    # make sure only the four operators are used
                    valid_operators = [ "+", "-", "/", "*"]
                    # as for input and operators
                    equation = input("Enter a basic math equation using numbers and the +, -, /, * operators. Separate each with a space. " )
                    try:
                        # split user input into num1, num2, and operator
                        equation_parts = equation.split()
                        q3_num1 = float(equation_parts[0])
                        input_operator = equation_parts[1]
                        q3_num2 = float(equation_parts[2])
                        # check a valid operator is used
                        if input_operator in valid_operators:
                            instance.perform_operations(q3_num1, q3_num2, input_operator)
                            break
                        else:
                            print("Operators must be +, -, /, or *. Try again.")
                    # if the input was incorrectly formatted, then circle back and ask again
                    except:
                        print("Invalid input. Please follow the directions.")
                break
            elif selection == 4:
                while True:
                    # ask for user input
                    number_to_square = input("Enter a number to find its square: ")
                    try:
                        # check if it is a float
                        if '.' in number_to_square:
                            try:
                                # try to convert to float then square the number, break loop
                                number_to_square = float(number_to_square)
                                square_value = instance.calculateSquare(number_to_square)
                                break
                            except:
                                # if not a float, then invalid input
                                print("Invalid input. Only numbers allowed.")
                        # try to see if it is an int
                        else:
                            try:
                                # if an int, sqaure it in the method, break loop
                                number_to_square = int(number_to_square)
                                square_value = instance.calculateSquare(number_to_square)
                                break
                            except:
                                # if cannot square an int, then invalid input and ask again 
                                print("Invalid input. Only numbers allowed.")
                    except:
                        print("Enter a valid number to square")
                print(f"The square of {number_to_square} is", square_value)
                break
            elif selection == 5:
                # use the factorial method of instance
                instance.factorial()
                break
            elif selection == 6:
                while True:
                    # ask for start and end number
                    q6_startnum = input("Enter an integer to start counting! ")
                    q6_endnum = input("Enter an integer to end your counting! ")
                    # make sure those are counting integers
                    # if not, then invalid and ask again
                    try:
                        q6_startnum = int(q6_startnum)
                        q6_endnum = int(q6_endnum)
                        # use instance counting method
                        instance.counting(q6_startnum, q6_endnum)
                        break
                    except: 
                        print("Invalid input. Try again. You will need two integers.")
                print("All done counting!")
                        
                break
            elif selection == 7:
                while True:
                    # ask for base
                    base = input("Enter a value for the base of your triangle: ")
                    try:
                        # test if base can be a float
                        base = float(base)
                        if base > 0:
                            # if base is valid length, ask for perpendicular
                            while True:
                                perpendicular = input("Enter a value for the perpendicular of your triangle: ")
                                try:
                                    # see if the perpendicular is a valid float
                                    perpendicular = float(perpendicular)
                                    # calculate hypotenuse method
                                    print("The hypotenuse is", instance.calculateHypotenuse(base, perpendicular))
                                    break
                                except:
                                    print("Please enter a number value.")
                            break
                        else:
                            # if base is negative, it won't work
                            print("Invalid base value. Must be a number greater than 0.")
                    except:
                        print("Please enter a valid value for the base.")
                break
            elif selection == 8:
                while True:
                    # ask for width
                    q8_width = input("Enter the width of your rectangle: ")
                    # test if negative
                    try: 
                        # try to make width a float
                        q8_width = float(q8_width)
                        if q8_width > 0:
                            while True:
                                # if it can be a positive float, means it is valid
                                try:
                                    # ask for height
                                    q8_height = input("Enter the height of your rectangle: ")
                                    q8_height = float(q8_height)
                                    if q8_height > 0:
                                        print("The area of your rectangle is", instance.rectangular_area(q8_width, q8_height))
                                        break
                                    else:
                                        print("All lengths must be positive.")
                                except:
                                     print("Invalid height.") 
                            break
                        else:
                            print("Lengths are only positive numbers.")
                    except:
                        print("Invalid width.")
                # Assigned values for area
                q8_pt2_width = 10
                q8_pt2_height = 6
                # PRint to use the values and area
                print("Program assigned width is", q8_pt2_width)
                print("Program assigned  height is", q8_pt2_height)
                print("The area of the 10 x 6 second rectangle is", instance.rectangular_area(q8_pt2_width, q8_pt2_height))
                break
            elif selection == 9:
                print("Given two numbers, we are going to find the power of a number.")
                while True:
                    q9_base = input("Enter a value for the base number for which to find the power: ")
                    try:
                        # check if the base is an integer
                        # do this so that not everything is turned into a float if unnecessary
                        q9_base = int(q9_base)
                        while True: 
                            try:
                                # ask for a power
                                q9_exponent = input("Enter a power to which you will raise the base: ")
                                # evaluate what is given, in case it is a fraction
                                q9_exponent = eval(q9_exponent)
                                power_value = instance.number_power(q9_base, q9_exponent)
                                print(f"{q9_base} to the power of {q9_exponent} is", power_value)
                                break
                            except:
                                 print("The power must be a number.")
                        break
                    except ValueError:
                        try:
                            q9_base = float(q9_base)
                            while True: 
                               try:
                                   # ask for a power
                                   q9_exponent = input("Enter a power to which you will raise the base: ")
                                   # evaluate what is given, in case it is a fraction
                                   q9_exponent = eval(q9_exponent)
                                   power_value = instance.number_power(q9_base, q9_exponent)
                                   print(f"{q9_base} to the power of {q9_exponent} is", power_value)
                                   break
                               except:
                                    print("The power must be a number.")
                            break
                        except:
                            # if the base isn't a float
                            print("Invalid base number.")
                    except:
                        # if base isn't an int or a float
                        print("Invalid base number.")

                break
            else:
                # question 10, find the type of argument
                # ask for an input
                input_argument = input("Enter an argument to find its type: ")
                # call the function, pass the BasicMathOperations class instance to use later
                question10(input_argument, instance)
                break
        else:
            print("Invalid input. You must select a number between 1 and 10.")
   
    print(" ")    
    return print("Thanks for doing a task!")

# ============================================    

def question10(input_argument, instance):
    # check if the input is a digit --> int
    if input_argument.isdigit():
        instance.argument_type(int(input_argument))
    # if there is a point in the string, check if it is a float
    elif '.' in input_argument:
        try:
            instance.argument_type(float(input_argument))
        # if not a float, put it through to the type method (will come out string)
        except ValueError:
            instance.argument_type(input_argument)
    # if there is a + or - in it, it could be a complex number
    elif '+' in input_argument or '-' in input_argument:
        try:
            # check if complex
            instance.argument_type(eval(complex(input_argument)))
        except ValueError:
            instance.argument_type(input_argument)
    # curly brackets could mean set or dictionary
    elif '{' in input_argument and '}' in input_argument:
        # evaluate if it is a dictionary, if not, print message of why it might not be
        # put through the argument type method
        if ':' in input_argument:
            try:
                input_argument = eval(input_argument)
                instance.argument_type(input_argument)
            except NameError:
                print("If you meant to make a dictionary, perhaps you forgot quotes around strings.")
                instance.argument_type(input_argument)
        else:
         # evaluate if it is a set, if not, print message of why it might not be
         # put through the argument type method
            try:
                instance.argument_type(eval(input_argument))
            except NameError:
                print("If you meant to make a set, perhaps you forgot quotes around strings.")
                instance.argument_type(input_argument)
    # straight brackets could mean list
    elif '[' in input_argument and ']' in input_argument:
        try:
            instance.argument_type(eval(input_argument))
        # if don't put quotes around strings, it will not be a list
        except NameError:
            "If you were trying to make a list, check the quotes around strings."
            instance.argument_type(input_argument)
    elif '(' in input_argument and ')' in input_argument:
        # if it has () it could be a tuple, check if it is with eval
        try:
            if ',' in input_argument:
                instance.argument_type(eval(input_argument))
            else:
                instance.argument_type(input_argument)
        except NameError:
            print("If you meant to make a tuple, perhaps you forgot quotes around strings.")
            instance.argument_type(input_argument)
    else:
        instance.argument_type(input_argument)


# ===============================================

main()


    



