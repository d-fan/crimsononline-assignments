def swapchars(instring):
    lettercount = [0] * 26

    # Count the occurance of each character
    for c in instring:
        if (c.isalpha()):
            lettercount[ord(c.upper()) - ord('A')] += 1

    # Find the most and least common
    most = 0
    least = len(instring)
    most_index = 0
    least_index = 0
    for index,count in enumerate(lettercount):
        if (count > most):
            most = count
            most_index = index
        if (count < least and count > 0):
            least = count
            least_index = index
    c_most =( chr(ord('A') + most_index), chr(ord('a') + most_index))
    c_least= (chr(ord('A') + least_index),chr(ord('a') + least_index))

    # Perform the replacements
    outstring = ""
    for i,c in enumerate(instring):
        if (c.upper() == c_most[0]):
            outstring += c_least[c.islower()]
        elif (c.upper() == c_least[0]):
            outstring += c_most[c.islower()]
        else:
            outstring += c

    return outstring
