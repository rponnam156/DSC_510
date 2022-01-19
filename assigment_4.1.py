# DSC 510
# Week 4
# Programming Assignment Week 4
# Author Rajendra Prasad Ponnam
# 09/25/2021

# Change#:1
# Change(s) Made: Functions in the program 20-32
# Date of Change: 09/25/2021
# Author: Rajendra Prasad Ponnam
# Change Approved by: Michael Eller
# Date Moved to Production: 09/25/2021

import sys
import locale

locale.setlocale(locale.LC_ALL, 'en_CA.UTF-8')


def cost_calculator(feet, price):
    """
    This method is used to calculate the total price.
    :param feet: float
    :param price: float
    :return:  total price <float>
    """

    total_cost = feet * price

    return total_cost


def main():
    '''
    This is the main function of the program.
    :return:
    '''
    print("Welcome to my Fiber Optic Calculator \n"
          "This Program will calculate the installation of Fiber Optic Cable \n")

    # Read the user input value.
    try:
        company_name = input("Please enter your company name: ")
        requested_feet = float(input("Pleae enter the number of feet you'd like installed: "))
    except ValueError as ex:
        print(ex)
        sys.exit()

    if requested_feet > 0 and requested_feet <= 100:
        price = 0.87
    elif requested_feet > 100 and requested_feet <= 250:
        price = 0.80
    elif requested_feet > 250 and requested_feet <= 500:
        price = 0.70
    else:
        price = 0.50

    total_cost = cost_calculator(feet=requested_feet, price=price)

    # printing the required values
    print("The total fiber installation cost for, " + company_name + " is " + str(locale.currency(total_cost)))
    print("Thank you for using my program")


if __name__ == "__main__":
    main()
