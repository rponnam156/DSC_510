# DSC 510
# Week 6
# Programming Assignment Week 6
# Author Rajendra Prasad Ponnam
# 10/04/2021

# Change#:1
# Change(s) Made: main function added in the program 14-37.
# Date of Change: 10/05/2021
# Author: Rajendra Prasad Ponnam
# Change Approved by: Michael Eller
# Date Moved to Production: 10/05/2021

def main():
    '''
    This is the main function function of the program.
    It will read the user input temperature values and print the min and max temperature values and
    number of values in the temperature list.
    :return: None
    '''
    # empty temperature list
    temperature_ll = []
    print("Enter the temperature values in fahrenheit (F)")

    # read the user input value
    user_input = input("Enter the temperature value in °F (or Enter q to quit): ")

    while user_input.lower() != 'q':
        try:
            # convert the user input values from string to float
            temperature_ll.append(float(user_input))

            # read the user input values
            user_input = input("Enter the temperature value in °F (or Enter q to quit): ")

        except ValueError as ex:
            print(ex)
            break
    if temperature_ll:
        # print the values.

        print(f'Largest temperature in the temperature list is : {max(temperature_ll)}°F')
        print(f'Smallest temperature in the temperature list is :  {min(temperature_ll)}°F')
        print(f'Number of values in the temperature list is :  {len(temperature_ll)}')


if __name__ == "__main__":
    main()
