"""
Question 1

objectives
    - get more comfortable with Python
    - learn how to handle exceptions
    - work with the file system
"""

import re

def common_words(filename):
    """question 1a

    Write a function that takes a path to a text file as input. The function
    should open the file, count the number of occurrences of each word, and
    return a sorted list of the most common words.
    """

    """This function assumes that 'words' are strings of alphabetical characters, i.e. this function ignores punctuation"""

    return common_words_min(filename, 0)


def common_words_min(filename, min_chars):
    """question 1b

    Modify this function to take a second argument that specifies the
    minimum number of characters long a word can be to be counted.
    """
    wordPattern = re.compile('[a-zA-Z]{' + str(min_chars) + ',}')
    occurance = dict()
    with open(filename, 'r') as f:
        contents = f.read()
    words = wordPattern.finditer(contents)
    for wordMatch in words:
        word = wordMatch.group(0).lower()
        if word in occurance:
            occurance[word] += 1
        else:
            occurance[word] = 1
    return sorted(occurance, key=occurance.get, reverse=True)

def common_words_tuple(filename, min_chars):
    """question 1c

    Modify this function to return a list of tuples rather than just a list
    of strings. Each tuple should be of the format
        (word, number of occurrences)
    Of course, the list of tuples should still be sorted as in part a.
    """
    wordPattern = re.compile('[a-zA-Z]{' + str(min_chars) + ',}')
    occurance = dict()
    with open(filename, 'r') as f:
        contents = f.read()
    words = wordPattern.finditer(contents)
    for wordMatch in words:
        word = wordMatch.group(0).lower()
        if word in occurance:
            occurance[word] += 1
        else:
            occurance[word] = 1
    return sorted(occurance.items(), key=lambda item:item[1], reverse=True)

def common_words_safe(filename, min_chars):
    """question 1d

    Modify your function so that it catches the IOError exception and prints
    a friendly error message.
    """
    wordPattern = re.compile('[a-zA-Z]{' + str(min_chars) + ',}')
    occurance = dict()
    try:
        with open(filename, 'r') as f:
            contents = f.read()
    except IOError as e:
            print "IOError {0}: {1}".format(e.errno, e.strerror)
            return
    words = wordPattern.finditer(contents)
    for wordMatch in words:
        word = wordMatch.group(0).lower()
        if word in occurance:
            occurance[word] += 1
        else:
            occurance[word] = 1
    return sorted(occurance.items(), key=lambda item:item[1], reverse=True)