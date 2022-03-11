from english_words import english_words_set
from ast import literal_eval
from itertools import product
from string import ascii_lowercase

word_len = literal_eval(input("Enter word Length:"))
contains_words = literal_eval(
    input("Enter comma separated letters contained in the word:")
)
print(english_words_set[:2])
# n_letter_words = [''.join(x) for x in product(ascii_lowercase, repeat=word_len)]
# print(n_letter_words)
