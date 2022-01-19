# DSC 510
# Week 8
# Programming Assignment Week 8
# Author Rajendra Prasad Ponnam
# 10/20/2021

# Change#:1
# Change(s) Made: Exception handling code added in add_word method. 24-29.
# Date of Change: 10/20/2021
# Author: Rajendra Prasad Ponnam
# Change Approved by: Michael Eller
# Date Moved to Production: 10/20/2021

import re


def add_word(word, word_dict):
    '''
    This method will add the words to word_dictionary.
    :param word: string
    :param word_dict: dict
    :return: None
    '''
    try:
        # This will add the word to dict. If word is already existed increase the count of word.
        word_dict[word] += 1
    except KeyError:
        word_dict[word] = 1


def process_line(line, word_dict):
    '''
    This method will replace the special characters in each line and split the word into list
    :param line: string
    :param word_dict: dict
    :return: None
    '''
    # This code will replace the special characters in a given line.
    new_line = re.sub("[^0-9a-zA-Z']+", ' ', line).rstrip()

    # Split thw line with space character.
    word_list = new_line.split(' ')

    # looping the word list and calling add_word method for every word to add the word to word_dict.
    for word in word_list:
        add_word(word.lower(), word_dict)


def pretty_print(word_dict):
    '''
    This method will prinf the result.
    :param word_dict: dict
    :return: None
    '''

    # Print the length of the word_dict.
    print("Length of the dictionary: {word_dict_len}".format(word_dict_len=len(word_dict)))

    # Print the result.
    print('{:20s} {:10s}'.format("Word", "Count"))
    print('--------------------------')

    # Print the word name and it's count.
    for value in sorted(word_dict, key=word_dict.get, reverse=True):
        print('{:13s} {:10d}'.format(value, word_dict[value]))


def main():
    '''
    This is the main function function of the program.
    :return: None
    '''

    # Empty word_dictionary
    word_dict = {}
    file_name = "gettysburg.txt"
    try:
        # Open the file in read mode
        gba_file = open(file_name, "r")

    except OSError:
        print("Error: Sorry, the file {file_name} does not exist.".format(file_name=file_name))
        return 0

    for line in gba_file:
        if not line.isspace():
            process_line(line=line, word_dict=word_dict)

    # Call the pretty_pring method
    pretty_print(word_dict=word_dict)


if __name__ == "__main__":
    main()
