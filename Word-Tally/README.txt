PROGRAM USED FOR FINDING OUT HOW MANY TIMES A WORD APPEARS IN A TEXT...

This is a Python script that counts the frequency of each word in a given text and outputs the final tally in descending order of frequency. It uses regular expressions to split the text into individual words and a dictionary to store the frequency count of each word. The program is comprised of four functions:

a.) text2words(text): Takes a string of text as input and returns a list of individual words in the text.
b.) word_tally(words): Uses a list of words as input and returns a dictionary containing the frequency count of each word.
c.) sort_by_word_freq(word_count): Has a dictionary of word frequency counts as input and returns a list of tuples sorted in descending order of frequency.
d.) print_result(sorted_words): Takes a list of tuples sorted by word frequency as input and prints the result in the format "word: frequency".

To use the program, simply provide a text input to the text variable and run the program. The output will show the frequency count of each word in the text, with the most frequent words listed first.