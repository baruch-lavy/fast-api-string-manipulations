import string

def reverse_str(string):
    return string[::-1]

def to_upper(string:str):
    return string.upper()

def without_vowels(str:str):
    clean_str = ''
    for letter in str:
        if letter not in "aeiouAEIOU":
            clean_str += letter
    return clean_str