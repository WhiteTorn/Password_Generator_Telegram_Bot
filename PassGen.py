import random

import xkcdpass.xkcd_password as xp

delimiters_numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
delimiters_full = ["!", "$", "%", "^", "&", "*", "-", "_", "+", "=",
                   ":", "|", "~", "?", "/", ".", ";"] + delimiters_numbers


words = xp.locate_wordfile()  # Searching For Word File
wordlist = xp.generate_wordlist(wordfile=words, min_length=4, max_length=10)  # Creating List


# Weak Password
def weak():
    return xp.generate_xkcdpassword(wordlist, numwords=2, delimiter="")

# Normal Password
def normal():
    return xp.generate_xkcdpassword(
        wordlist, numwords=3, random_delimiters=True, valid_delimiters=delimiters_numbers)

# Strong Password
def strong():
    return xp.generate_xkcdpassword(
        wordlist, numwords=4, random_delimiters=True, valid_delimiters=delimiters_full
    )

def random_capitalisation(s, chance):
    new_str = []
    for i, c in enumerate(s):
        new_str.append(c.upper() if random.random() < chance else c)
    return "".join(new_str)


print(random_capitalisation(strong(), 5/10.0))
