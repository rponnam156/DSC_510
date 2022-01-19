# DSC 510
# Week 5
# Programming Assignment Week 5
# Author Rajendra Prasad Ponnam
# 09/30/2021

# Change#:1
# Change(s) Made: calculate average function added in the program 49-75.
# Date of Change: 10/02/2021
# Author: Rajendra Prasad Ponnam
# Change Approved by: Michael Eller
# Date Moved to Production: 10/02/2021


import sys


def performCalculation(operation_type):
    '''
    This method will perform the calculation based on the user input.
    :param operation_type:  <string>
    :return: None
    '''
    try:
        # Read the user input values.
        number_one = int(input("Enter First Number: "))
        number_two = int(input("Enter Second Number: "))

    except ValueError as ex:
        raise ex

    # Perform the operation based on the user input and print the result.
    if operation_type == '+':
        result = number_one + number_two
        print("Sum of two numbers is = ", result)
    elif operation_type == '-':
        result = number_one - number_two
        print("Subtraction of two numbers is = ", result)
    elif operation_type == '*':
        result = number_one * number_two
        print("Multiplication of two numbers is = ", result)
    elif operation_type == '/':
        try:
            result = number_one / number_two
            print("Division of two numbers is = ", result)
        except ZeroDivisionError as ex:
            raise ex
    else:
        print("Input character is not recognized \n")


def calculateAverage():
    '''
    This method will calculate the average of given numbers.
    :return: none
    '''
    try:
        # denotes total sum of five numbers
        total_sum = 0
        number_of_values = int(input("Enter the number values to calculate their sum and average: "))
        for value in range(number_of_values):
            # take inputs
            num = float(input("Enter number: "))
            # calculate total sum of numbers
            total_sum += num

        # calculate average of numbers
        average = total_sum / number_of_values

        # print average value
        print("Average of numbers =", average)
    except ValueError as ex:
        print(ex)
        sys.exit()


def main():
    '''
    This is the main method of the program.
    :return:  None
    '''
    try:
        while True:
            print("Would you like to perform a calculation (+, -, *, /) or calculate an average")

            # Read the user input value.
            user_choice = input("Enter 1 to perform a calculation and 2 to calculate an Average or Q to Quit: ")

            # calling the functions based on the user input.
            if user_choice == '1':
                user_input_operation = input("Enter specific operation type +, -, *, /: ")
                performCalculation(operation_type=user_input_operation)
            elif user_choice == '2':
                calculateAverage()
            elif user_choice.lower() == 'q':
                break
            else:
                print("Invalid user input")
                break

    except Exception as ex:
        print("Exception occurred in the program and exception is: ", ex)


if __name__ == "__main__":
    main()
