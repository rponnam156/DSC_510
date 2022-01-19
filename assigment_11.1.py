# DSC 510
# Week 11
# Programming Assignment Week 11
# Author Rajendra Prasad Ponnam
# 11/09/2021

# Change#:1
# Change(s) Made: Exception handling code added in main method. 71-76.
# Date of Change: 11/09/2021
# Author: Rajendra Prasad Ponnam
# Change Approved by: Michael Eller
# Date Moved to Production: 11/09/2021

import locale
import sys

locale.setlocale(locale.LC_ALL, 'en_CA.UTF-8')


class CashRegister(object):
    '''
        This is the cash register class.
    '''

    def __init__(self):
        self.total_price = 0
        self.item_count = 0

    def add_item(self, price):
        '''
            This method will keep track of the number of items in the cart.
        :param price: string
        :return:
        '''
        self.total_price += float(price)
        self.item_count += 1

    def get_total(self):
        '''
            This method will return the total price.
        :return: int
        '''
        return self.total_price

    def get_count(self):
        '''
            This method will return the items count.
        :return: int
        '''
        return self.item_count


def main():
    '''
    This is main method of the program.
    :return:
    '''

    # create an object of type CashRegister
    register = CashRegister()
    user_resp = True

    # print welcome message
    print("Welcome to shopping world!")
    while user_resp:

        # read the user input choice.
        user_resp = input("Would you like to add another item to the cart Y or N: ").upper()

        if user_resp == "Y":
            try:
                # read the price value from user.
                price = input("What is the price of the item?: ")
            except ValueError as e:
                print(e)
                sys.exit(1)

            # call the add_item function from the CashRegister class.
            register.add_item(price)
        else:
            # print the results
            print("Total number of items in the cart: {items_count}".format(items_count=register.get_count()))
            print("Total amount is: {total_cost}".format(total_cost=str(locale.currency(register.get_total()))))
            user_resp = False

if __name__ == "__main__":
    main()