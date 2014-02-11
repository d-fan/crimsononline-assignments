from pprint import pprint # pretty print output formatting
from question1 import (common_words, common_words_min, common_words_tuple,
    common_words_safe)
# fill in the rest!

print "==testing question 1=="
print "common_words... ",
pprint(common_words("words.txt"))

print "common_words_min 2... ",
pprint(common_words_min("words.txt", 2))

print "common_words_min 5... ",
pprint(common_words_min("words.txt", 5))

print "common_words_min 9... ",
pprint(common_words_min("words.txt", 9))

print "common_words_tuple w/ min 5... ",
pprint(common_words_tuple("words.txt", 5))

print "common_words_safe... ",
pprint(common_words_safe("words_fail.txt", 5))
print