# DSC 510
# Week 3
# Programming Assignment Week 3
# Author Rajendra Prasad Ponnam
# 09/14/2021

# Change#:1
# Change(s) Made: Added if else condition for calculating installation cost 26-38 added
# Date of Change: 09/14/2021
# Author: Rajendra Prasad Ponnam
# Change Approved by: Michael Eller
# Date Moved to Production: 09/20/2021

# print welcome message
import sys

print("Welcome to fiber optic cable cost calculator")

# Reading company name from user
company_name = input("Enter company name : ")

try:
    # Reading the user input number of feet's fiber optic cable required
    fiber_optic_cable_length = float(input("Enter number of feet's fiber optic cable required: "))
except ValueError as e:
    print(e)
    sys.exit()

# calculating installation cost based on the number of feet's of fiber option cable
try:
    if fiber_optic_cable_length > 0 and fiber_optic_cable_length <= 100:
        charges = 0.87
    elif fiber_optic_cable_length > 100 and fiber_optic_cable_length <= 250:
        charges = 0.80
    elif fiber_optic_cable_length > 250 and fiber_optic_cable_length <= 500:
        charges = 0.70
    elif fiber_optic_cable_length >= 500:
        charges = 0.50
    else:
        print("Required fiber optic cable length number must be >  0")
        sys.exit()
    installation_cost = fiber_optic_cable_length * charges

except Exception as e:
    print("Exception occurred in the program")
    raise e

# Printing the receipt
print("Company name: {company_name}".format(company_name=company_name))
print("Number of feet's of fiber optic cable to be installed: {}".format(fiber_optic_cable_length))
print("Total cost: ${installation_cost}".format(installation_cost=installation_cost))


