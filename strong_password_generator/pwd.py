#!/usr/bin/python3
"""create a password with 12 characters containing alphabets lowercase and uppercase, digits and symbols"""
from string import ascii_letters, digits, punctuation
from random import shuffle, choice


def generate_pwd():
    """generate random password"""
    chars, numb, symb = list(ascii_letters), list(digits), list(punctuation)
    shuffle(numb), shuffle(symb), shuffle(chars)
    lists = numb + symb + chars
    pwd_l = []
    for i in range(12):
        pwd_l.append(choice(lists))
    pwd = "".join(pwd_l)
    return pwd


# usage:
print("here is your generated password:")
pwd = generate_pwd()
print(pwd)
