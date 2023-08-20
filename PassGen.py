import random
import string

letters = string.ascii_letters
digits = string.digits
special = string.punctuation

pwd_length = 13  # int(input("Please enter lenght of password: "))


def weak():
    alphabet = ''
    for i in range(pwd_length):
        alphabet += random.choice(letters)
    return alphabet


def normal():
    alphabet = ''
    for i in range(pwd_length + 2):
        a = random.choice(letters)
        b = random.choice(digits)
        lst = [a, b]
        alphabet += random.choice(lst)
    return alphabet


def strong():
    alphabet = ''
    for i in range(pwd_length + 4):
        a = random.choice(letters)
        b = random.choice(digits)
        c = random.choice(special)
        lst = [a, b, c]
        alphabet += random.choice(lst)
    return alphabet


print(strong())
