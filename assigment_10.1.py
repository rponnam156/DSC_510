# DSC 510
# Week 10
# Programming Assignment Week 10
# Author Rajendra Prasad Ponnam
# 11/07/2021

# Change#:1
# Change(s) Made:
# Date of Change: 11/07/2021
# Author: Rajendra Prasad Ponnam
# Change Approved by: Michael Eller
# Date Moved to Production: 11/07/2021

import sys

import requests

# print welcome message
print("Hello, Welcome to the GET request program that display the Chuck Norris Jokes \n")
user_input = 'y'

# while loop to call the chucknorris get API based on the user input.
while True:

    if user_input.lower() == 'y':
        # call the chucknorris get API
        req_joke = requests.get("https://api.chucknorris.io/jokes/random")
    else:
        # print thank you message
        print("\nThank you, come back again when you want another joke")
        break
    data = req_joke.json()

    # print the result.
    print("\n\n{}".format(data.get('value')))
    try:
        # Read the user input value.
        user_input = input("\nWould you like to see another joke? (Y/N):")
    except ValueError as ex:
        print(ex)
        sys.exit(1)
