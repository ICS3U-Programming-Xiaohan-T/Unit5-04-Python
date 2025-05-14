#!/usr/bin/env python3
# Created by: Xiaohan
# Created on: May 14, 2025
# This program will calculate the result for users by getting numbers and operations.


# Function called calculator that includes numbers and operators
def calculator(num1, num2, operator):
    if operator == "+":
        return num1 + num2
    elif operator == "-":
        return num1 - num2
    elif operator == "*":
        return num1 * num2
    elif operator == "/":
        if num2 != 0:
            return num1 / num2
        else:
            return "Error: Division by zero"
    elif operator == "%":
        if num2 != 0:
            return num1 % num2
        else:
            return "Please do not enter 0 in second number"
    else:
        return "Invalid"


def main():
    # Get operator
    operator = input("Enter the operator (+, -, *, /, %): ")

    # Get user numbers as strings
    user_num1 = input("Enter the first number: ")
    user_num2 = input("Enter the second number: ")

    # Try converting to float
    try:
        num1 = float(user_num1)
    except ValueError:
        print("Invalid input. Please enter a valid first number.")
        return

    try:
        num2 = float(user_num2)
    except ValueError:
        print("Invalid input. Please enter a valid second number.")
        return

    # Validate operator using OR
    if (
        operator == "+"
        or operator == "-"
        or operator == "*"
        or operator == "/"
        or operator == "%"
    ):
        result = calculator(num1, num2, operator)
        print("The result is:", result)
    else:
        print("Invalid operator. Please enter one of the following: +, -, *, /, %")


if __name__ == "__main__":
    main()
