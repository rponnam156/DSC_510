# # DSC 510
# # Week 6
# # Programming Assignment Week 6
# # Author Rajendra Prasad Ponnam
# # 10/04/2021
#
# # Change#:1
# # Change(s) Made: main function added in the program 14-41.
# # Date of Change: 10/05/2021
# # Author: Rajendra Prasad Ponnam
# # Change Approved by: Michael Eller
# # Date Moved to Production: 10/05/2021
#
# def main():
#     '''
#     This is the main function function of the program.
#     It will read the series of temperature values  from user input and print the min, max temperature values
#     and number of values in the temperature list.
#     :return: None
#     '''
#     # Empty temperature list
#     temperatures_ll = []
#
#     while True:
#         # Enter the series of temperature values with space delimiter
#         # Example 70 80 73
#
#         print('Enter the temperature values in °F (or Enter q to quit)')
#
#         # read the user input
#         user_input = input("Enter the input:")
#         if user_input == 'q':
#             break
#         else:
#             try:
#                 # convert user input series of values to list and append to temperature list
#                 temperatures_ll.extend(list(map(float, user_input.strip().split())))
#             except ValueError as ex:
#                 print(ex)
#                 break
#             # Print the values.
#             print(f'\nLargest temperature value in the temperature list is : {max(temperatures_ll)}°F')
#             print(f'Smallest temperature value in the temperature list is :  {min(temperatures_ll)}°F')
#             print(f'Number of values in the temperature list is : {len(temperatures_ll)}\n')
#
#
# if __name__ == "__main__":
#     print("Welcome to the largest and smallest temperature determination program")
#     main()

# class Test(object):
#     def __init__(self):
#         self.first = "ABC"
#         self.last = "XYX"
#
#     def fullname(self):
#         return '{} {}'.format(self.first,self.last)
#
# print(Test().fullname())
#
#
# import locale
# import sys
#
# locale.setlocale(locale.LC_ALL, 'en_CA.UTF-8')
# print(str(locale.currency(10)))


'''
Here an example of what I'm looking for, for your output.  Notice the fields.  You should have at least the current temp, high temp, low temp, pressure, humidity, and cloud cover elements in your output.  Think about the type of data a normal person would want when they look up weather.  Odds are they want more than just the current temp.




Do not display temp in Kelvin, this would be considered unreadable right?  I don't know anyone who looks at kelvin temps.

Do make this pretty, this is a big project and something you could showcase to others

Make sure you're not rigid with the input from a user.  If a user types in y and you wanted Y that should be ok.  Think about the user experience.

Think about punctuation and grammar for your prompts.

Have nicely defined try blocks (these are required).  DO NOT put huge blocks of code in a try block.

Make sure your main is properly defined.

If you're unsure about something ask.

Make sure you allow the user to enter in a zip code and a city name. (it's ok to hard code the country to us.

Make sure that if a user enters in Omaha it evaluates to the right Omaha.

Have fun with this assignment.


Would you like to lookup weather data by US City or zip code? Enter 1 for US City 2 for zip: 1
Please enter the city name: omaha
Please enter the state abbreviation: ne
Would you like to view temps in Fahrenheit, Celsius, or Kelvin.
Enter 'F' for Fahrenheit, 'C' for Celsius, 'K' for Kelvin: f



Current Weather Conditions For Omaha
Current Temp: 41.23 degrees
High Temp: 44.55 degrees
Low Temp: 37.29 degrees
Pressure: 1009hPa
Humidity: 54%
Cloud Cover: Full Cloud Cover



Would you like to perform another weather lookup? (Y/N)y



Would you like to lookup weather data by US City or zip code? Enter 1 for US City 2 for zip: 2
Please enter the zip code: 68136
Would you like to view temps in Fahrenheit, Celsius, or Kelvin.
Enter 'F' for Fahrenheit, 'C' for Celsius, 'K' for Kelvin: f



Current Weather Conditions For Omaha
Current Temp: 40.71 degrees
High Temp: 44.49 degrees
Low Temp: 36.73 degrees
Pressure: 1009hPa
Humidity: 55%
Cloud Cover: Full Cloud Cover



Would you like to perform another weather lookup? (Y/N)
'''

state_codes_ll = ['AL', 'AK', 'AS', 'AZ', 'AR', 'CA', 'CO', 'CT', 'DE', 'DC', 'FL', 'GA', 'GU', 'HI', 'ID', 'IL', 'IN',
                  'IA', 'KS', 'KY', 'LA', 'ME', 'MD', 'MA', 'MI', 'MN', 'MS', 'MO', 'MT', 'NE', 'NV', 'NH', 'NJ', 'NM',
                  'NY', 'NC', 'ND', 'MP', 'OH', 'OK', 'OR', 'PA', 'PR', 'RI', 'SC', 'SD', 'TN', 'TX', 'UT', 'VT', 'VI',
                  'VA', 'WA', 'WV', 'WI', 'WY']
y = []
for x in state_codes_ll:
    y.append(x.lower())

print(y)
