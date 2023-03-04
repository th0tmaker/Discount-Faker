# import regular expression operations
import re


# convert text as string into list of individual words
def text2words(txt):
    # find all sequences of characters in a text that match pattern "\b[\w'.-]+\b" where:
    # r"" -> pattern needs to be in raw string format to avoid backslashes ('\') being treated as escape characters
    # b\ -> represents word boundary, where word chars (letters, digits, underscore) meet non-word chars
    # [\w'.-] -> represents a group that consists all word chars, apostrophe('), dot(.), hyphen(-)
    # + -> quantifier that denotes 'one or more' instances of chars inside our group instead of individual instances
    words = re.findall(r"\b[\w'.-]+\b", txt)
    return words


# iterate through words list and tally up the words inside a dictionary
def tally_into_dict(words):
    word_count = {}
    # for every item in the words list
    for word in words:
        # if item not found in dictionary
        if word not in word_count:
            # put word inside as key and ascribe value 1
            word_count[word] = 1
        else:
            # if item already in dictionary, match existing key and increment value by 1
            word_count[word] += 1

    return word_count


# sort dictionary from most frequent to the least frequent word
def sort_by_word_freq(word_count):
    # turn word_count dictionary content into key-value pair of tuples by using .items() method
    # sort by key, where key is 2nd element in tuple (index[0] = word, index[1] = freq) by using lambda anon function
    # reverse=True -> turn sort order from ascending into descending
    sorted_words = sorted(word_count.items(), key=lambda x: x[1], reverse=True)
    return sorted_words


# print result of sorted words in desired format
def print_result(sorted_words):
    # for item in pos[0] and item in pos[1] in sorted_words tuple
    for word, freq in sorted_words:
        print("{}: {}".format(word, freq))  # [0] in 1st curly bracket, [1] in 2nd curly bracket


# text for testing code
text = """With a wicked gleam in his eye, Dr.LeQuack set to work, creating a complex and convoluted contraption that
       even Courage wouldn't be able to stop. With a fierce determination, Dr.LeQuack crept through the streets of
       Nowhere, searching for Courage. When he found the trembling canine, he activated his device - a mishmash of
       whirling gears and spinning     blades that were surely going to threaten the well-being of his nemesis."""

final_words = text2words(text)
final_word_count = tally_into_dict(final_words)
final_sorted_words = sort_by_word_freq(final_word_count)

print_result(final_sorted_words)
